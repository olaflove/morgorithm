n = int(input())
arr = list(map(int, input().split()))

# n == 1 예외
if n == 1:
    print(sum(arr) - max(arr))
else:
    # 마주보는 면 중 작은 값 선택
    a = min(arr[0], arr[5])
    b = min(arr[1], arr[4])
    c = min(arr[2], arr[3])

    one = min(a, b, c)                  # 1면 최소
    two = min(a+b, a+c, b+c)           # 2면 최소
    three = a + b + c                  # 3면 최소

    # 개수
    cnt_three = 4
    cnt_two = 8*n - 12
    cnt_one = (n-2)**2 + 4*(n-2)*(n-1)

    # 정답
    ans = (cnt_one * one) + (cnt_two * two) + (cnt_three * three)
    print(ans)