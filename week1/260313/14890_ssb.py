import sys
input = sys.stdin.readline

n, l = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
columns = []
for col in zip(*rows):
    columns.append(list(col))
lists = rows + columns

# 내리막 경사로를 설치해야 할 때 (prev > now)
# - 앞으로 l step이 now와 같은가를 확인
def can_down(idx):
    now = lst[idx]
    for i in range(l):
        if idx+i >= n:
            return False
        if lst[idx+i] == now and not visited[idx+i]:
            visited[idx+i] = True
        else:
            return False
    return True

# 오르막 경사로를 설치해야 할 때 (prev < now)
# - 뒤로 l step이 prev와 같은가를 확인
def can_up(idx):
    now = lst[idx]
    for i in range(1, l+1):
        if idx-i < 0:
            return False
        if lst[idx-i] == now-1 and not visited[idx-i]:
            visited[idx-i] = True
        else:
            return False
    return True

def check(lst):
    prev = lst[0]
    for i in range(1, n):
        if lst[i] == prev:
            continue
        elif lst[i] - prev == 1:
            if not can_up(i):
                return False
        elif lst[i] - prev == -1:
            if not can_down(i):
                return False
        else:
            return False
        prev = lst[i]
    return True

bridge = 0
for lst in lists:
    visited = [False] * n
    if check(lst):
        bridge += 1

print(bridge)