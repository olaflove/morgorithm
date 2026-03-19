n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
pos_num = []
neg_num = []

ans = 0
for i in range(n):
    if arr[i] > 0 :
        pos_num.append(arr[i])
    else :
        neg_num.append(arr[i])
max_pos = pos_num[-1] if pos_num else 0
max_neg = abs(neg_num[0]) if neg_num else 0
# 거리가 먼 곳의 인덱스부터 0까지의 인덱스 까지 가지고 갈 수 있는 책 만큼 자른다.
for i in range(len(pos_num)-1,-1,-m):
    ans += pos_num[i] * 2

for i in range(0,len(neg_num),m):
    ans += abs(neg_num[i])  *2

ans -= max(max_pos,max_neg)
# 0을 기준으로 양수가 거리가 먼지 음수가 거리가 먼지 확인 
print(ans)