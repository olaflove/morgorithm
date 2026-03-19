N, M = map(int, input().split())    # N은 책의 개수, M은 한번에 드는 개수
books = list(map(int, input().split()))
books.sort()    # 최대값 구하기 위한 정렬

max_num = max(abs(books[0]), abs(books[-1]))    # 최대값은 한번만 더하기 위해 따로 추출
ans = 0
cnt = 0

# 1개씩 밖에 책을 못드는 경우
if M == 1:
    for i in books:
        ans += abs(i)*2
    ans -= max_num
    print(ans)
    exit()
        
b_minus = []
b_plus = []

# 양수와 음수를 따로 배열로 구분해둠
for val in books:
    if val < 0:
        b_minus.append(val)
    else:
        b_plus.append(val)

# 절댓값이 큰 것부터 처리해주기 위해 내림차순으로 정렬
b_minus.sort(reverse=True)


# 하나씩 POP해가면서 M에 만족하는 적절하는 인덱스에 해당하는 책만 더해주기
while b_minus:
    tmp = b_minus.pop()
    cnt += 1
    if -tmp != max_num and cnt % M == 1:
        ans += tmp * -2

    elif -tmp == max_num and cnt % M == 1:
        ans += tmp * -1
        
# 마찬가지로 하나씩 POP해가면서 M에 만족하는 적절하는 인덱스에 해당하는 책만 더해주기 
cnt = 0
while b_plus:
    tmp = b_plus.pop()
    cnt += 1
    if tmp != max_num and cnt % M == 1:
        ans += tmp * 2

    elif tmp == max_num and cnt % M == 1:
        ans += tmp
print(ans)