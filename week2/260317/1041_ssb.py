n = int(input())
a, b, c, d, e, f = map(int, input().split())

if n == 1:
    print(sum([a, b, c, d, e, f]) - max(a, b, c, d, e, f))
    exit()

set1, set2, set3 = set([a, f]), set([b, e]), set([c, d])

# 한 면의 최솟값
one = min(a, b, c, d, e, f)
# 두 면의 합의 최솟값
nxt = 51
if one in set1:
    nxt = min(min(set2), min(set3), nxt)
if one in set2:
    nxt = min(min(set1), min(set3), nxt)
if one in set3:
    nxt = min(min(set1), min(set2), nxt)
two = one + nxt
# 세 면의 합의 최솟값
three = min(set1) + min(set2) + min(set3)

# 한 면: (n-2)(n-2) + 4(n-2)(n-1) = 5n^2-16n+12개
# 두 면: 4(n-2) + 4(n-1) = 8n-12개
# 세 면: 4개
ans = one * (5*(n**2) - 16*n + 12) + two * (8*n - 12) + three * 4
print(ans)