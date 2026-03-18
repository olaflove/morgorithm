import sys
input = sys.stdin.readline

n = int(input())
# arr = [tuple(map(int, input().split())) for _ in range(n)]
solid = [0] * n
weight = [0] * n
for i in range(n):
    s, w = map(int, input().split())
    solid[i] = s
    weight[i] = w

def backtrack(now):
    global max_cnt
    if now == n:
        cnt = sum(map(lambda x: x <= 0, solid))
        max_cnt = max(cnt, max_cnt)
        return
    
    # 자기 계란이 깨져있는 경우
    if solid[now] <= 0:
        backtrack(now + 1)
        return

    hit = False
    for i in range(n):
        # 자기 계란 치려는 경우 / 계란이 이미 깨져있는 경우 스킵
        if i == now or solid[i] <= 0:
            continue
        solid[now] -= weight[i]
        solid[i] -= weight[now]
        backtrack(now + 1)
        solid[now] += weight[i]
        solid[i] += weight[now]
        hit = True
    
    # 계란이 모두 깨져있던 경우
    if not hit:
        backtrack(now + 1)

max_cnt = -float('inf')
backtrack(0)
print(max_cnt)