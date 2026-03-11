from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
store = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            home.append((r, c))

for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            store.append((r, c))

answer = float('inf')

for selected in combinations(store, M):
    total = 0

    for hr, hc in home:
        min_dist = float('inf')

        for sr, sc in selected:
            dist = abs(hr - sr) + abs(hc - sc)
            if dist < min_dist:
                min_dist = dist

        total += min_dist

    if total < answer:
        answer = total

print(answer)