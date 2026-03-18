N, M = map(int, input().split())
books = list(map(int, input().split()))

minus = []
plus = []

for x in books:
    if x < 0:
        minus.append(-x)   # 절댓값으로 저장
    else:
        plus.append(x)

minus.sort(reverse=True)
plus.sort(reverse=True)

total = 0

# 음수 쪽 묶음 처리
for i in range(0, len(minus), M):
    total += minus[i] * 2

# 양수 쪽 묶음 처리
for i in range(0, len(plus), M):
    total += plus[i] * 2

max_dist = 0
if minus:
    max_dist = max(max_dist, minus[0])
if plus:
    max_dist = max(max_dist, plus[0])

print(total - max_dist)