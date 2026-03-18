def backtrack(ans):
    
    # 방금 추가한 숫자가 수열을 망쳤는지 확인하는 조건문
    #[-1]과 [-2] 비교, [-2:-1]과 [-4:-2]비교 ... 쭉쭉쭉 비교해나가기
    # 만약 비교한 글자들이 서로 같다면 나쁜 수열
    for i in range(1, len(ans) // 2 + 1):  
        if ans[-i:] == ans[-2*i:-i]:
            return
    
    # 원하는 길이에 도달했는지 확인
    if len(ans) == N:
        print(ans)
        # 가장 먼저 찾은 좋은 수열이 가장 작은 좋은 수열이므로 바로 종료시켜야함.
        exit()

    # 1,2,3순으로 수열에 숫자 넣고 재귀 호출
    for i in "123":
        backtrack(ans + i)

                
N = int(input())
ans = ''
backtrack(ans)