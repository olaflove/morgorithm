n = int(input())
ans = []

def possible() :
    # 현재 수열이 좋은 수열인지 뒤에서 부터 같은 부분 수열이 반복되는 지 확인한다.
    for i in range(1,len(ans)//2+1) :
        if ans[-i:] == ans[-2*i:-i] :
            return False
    return True

def dfs():
    if len(ans) == n :
        print("".join(map(str,ans)))
        return True
    
    for num in range(1,4):
        ans.append(num)

        if possible() :
            if dfs():
                return True
        ans.pop()
    return False
dfs()