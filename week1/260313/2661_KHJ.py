'''
조건
1. 높이가 같다면 건너뛰기
2. 높이 차이가 2이상이라면 가망 없음
3. 현재 높이 < 다음 높이 인 경우 -> 현재 높이 ~ 뒤로 L만큼의 거리 탐색
    i) 인덱스 범위 밖이거나, ii) 이미 경사로가 설치되어 있다거나, iii) 높이가 달라졌다면
    가망 없음
4. 현재 높이 > 다음 높이 인 경우 -> 다음 높이 ~ L만큼의 거리 탐사
    i) 인덱스 범위 밖이거나, ii) 이미 경사로가 설치되어 있다거나, iii) 높이가 달라졌다면
    가망 없음
'''

def check(arr):
    installed = [False] * N
    
    for i in range(N-1):
        if arr[i] == arr[i+1]:
            continue
        
        if abs(arr[i] - arr[i+1]) > 1:
            return False
        
        if arr[i] < arr[i+1]:
            for j in range(i, i-L, -1):
                if j < 0 or installed[j] or arr[i] != arr[j]:
                    return False
                else:
                    installed[j] = True
                    
        elif arr[i] > arr[i+1]:
            for j in range(i+1,i+1+L):
                if j >= N or installed[j] or arr[i+1] != arr[j]:
                    return False
                else:
                    installed[j] = True        
            
    return True
                    
    
N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for y in range(N):
    if check(grid[y]):
        ans += 1

for x in range(N):
    col = [grid[y][x] for y in range(N)]
    if check(col):
        ans += 1
        
print(ans)