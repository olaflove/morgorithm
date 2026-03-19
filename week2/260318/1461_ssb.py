n, m = map(int, input().split())
books = sorted(map(int, input().split()))

minus, plus = [], []
for i in range(n):
    if books[i] > 0:
        minus = books[:i]
        plus = books[i:]
        break

def lib(books):
    if books[0] < 0:
        books = sorted(map(abs, books))
    max_dist = books[-1]

    dist = 0
    for i in range(len(books)-1, -1, -m):
        dist += books[i] * 2

    return dist, max_dist

# 책의 좌표가 양수나 음수만 주어진 경우
if not minus or not plus:
    dist, max_dist = lib(books)
    print(dist - max_dist)
else:
    minus_dist, minus_max_dist = lib(minus)
    plus_dist, plus_max_dist = lib(plus)
    dist = min(minus_dist + plus_dist - minus_max_dist, minus_dist + plus_dist - plus_max_dist)
    print(dist)