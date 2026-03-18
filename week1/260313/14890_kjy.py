n,l = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# 한 줄씩 경사로 설치 조건을 만족하는지 확인하는 함수
def check(line):
    used = [False]*n
    i = 0

    while i < n-1 :
        if line[i] == line[i+1] :
            i += 1
        
        elif abs(line[i]-line[i+1]) > 1 :
            return False
        
        elif line[i] - line[i+1] == 1 :
            for j in range(1,l+1) :
                if i+j >= n or line[i+1] != line[i+j] or used[i+j]:
                    return False
                used[j+i] = True
            i += l
        elif line[i] - line[i+1] == -1 :
            for j in range(l):
                if i-j < 0 or line[i] != line[i-j] or used[i-j] :
                    return False
                used[i-j] = True
            i += 1
    return True

ans = 0

# 행 검사
for i in range(n):
    if check(board[i]) :
        ans += 1

# 열 검사
for i in range(n):
    line = [board[j][i] for j in range(n)]
    if check(line):
        ans += 1

print(ans)