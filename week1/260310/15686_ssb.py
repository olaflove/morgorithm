import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
homes, chickens = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

def distance(home, alive):
    x, y = home
    min_dist = float('inf')
    for chicken in alive:
        cx, cy = chicken
        dist = abs(x - cx) + abs(y - cy)
        min_dist = min(dist, min_dist)
    return min_dist

visited = [False] * (len(chickens) + 1)
alive = []
min_total_dist = float('inf')
def backtrack(start):
    global min_total_dist

    if len(alive) == m:
        total_dist = 0
        for home in homes:
            total_dist += distance(home, alive)
        min_total_dist = min(total_dist, min_total_dist)
        return
    
    for i in range(start, len(chickens)):
        alive.append(chickens[i])
        backtrack(i + 1)
        alive.pop()

backtrack(0)
print(min_total_dist)