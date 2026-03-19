n, m = map(int, input().split())
books = list(map(int, input().split()))

dist = (
    *sorted([x for x in books if x > 0], reverse=True)[::m],
    *sorted([-x for x in books if x < 0], reverse=True)[::m]
)

print(sum(dist) * 2 - max(dist))