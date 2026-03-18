import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    s,w = map(int,input().split())
    arr.append([s,w])
ans = 0

def dfs(idx,durable,weight,val):
    global ans
    if idx == n :
        if ans < val :
            ans = max(ans,val)
        return
    hit = False

    for i in range(n):
        if i == idx :
            continue
        
        if arr[idx][durable] <= 0 :
            dfs(idx+1,durable,weight,val)
            return
        
        if arr[i][durable] <= 0 :
            continue
        
        hit = True

        if arr[idx][durable] - arr[i][weight] <= 0 : # 손에 든 계란이 깨졌으면
            
            if arr[i][durable]- arr[idx][weight] <= 0 : # 친 계란이 같이 깨졌으면
                arr[idx][durable] = arr[idx][durable] - arr[i][weight]
                arr[i][durable] = arr[i][durable] - arr[idx][weight]
                dfs(idx+1,durable,weight,val+2)
                arr[idx][durable] = arr[idx][durable] + arr[i][weight]
                arr[i][durable] = arr[i][durable] + arr[idx][weight]
            else : # 친 계란은 안깨졌냐 ?
                arr[idx][durable] = arr[idx][durable] - arr[i][weight]
                arr[i][durable] = arr[i][durable] - arr[idx][weight]
                dfs(idx+1,durable,weight,val+1)
                arr[idx][durable] = arr[idx][durable] + arr[i][weight]
                arr[i][durable] = arr[i][durable] + arr[idx][weight]
        
        else : # 손에 든 계란이 안 깨졌을 때
            if arr[i][durable]- arr[idx][weight] <= 0 : # 친 계란이 깨졌으면
                arr[idx][durable] = arr[idx][durable] - arr[i][weight]
                arr[i][durable] = arr[i][durable] - arr[idx][weight]
                dfs(idx+1,durable,weight,val+1)
                arr[idx][durable] = arr[idx][durable] + arr[i][weight]
                arr[i][durable] = arr[i][durable] + arr[idx][weight]
            else : # 친 계란이 안 깨졌으면 
                arr[idx][durable] = arr[idx][durable] - arr[i][weight]
                arr[i][durable] = arr[i][durable] - arr[idx][weight]
                dfs(idx+1,durable,weight,val)
                arr[idx][durable] = arr[idx][durable] + arr[i][weight]
                arr[i][durable] = arr[i][durable] + arr[idx][weight]
    if not hit :
        dfs(idx+1,durable,weight,val)


dfs(0,0,1,0)
print(ans)