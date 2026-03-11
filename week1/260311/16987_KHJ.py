def solve(idx): # idx는 들어올릴 계란의 위치 인덱스, 0부터 시작한다.

    if idx == N:    # 다음에 쥘 계란이 인덱스 범위 밖이거나 혹은 칠 계란이 없다면이 여기에 포함됨.
        cnt = 0
        for guard, kg in egg_list:
            if guard <= 0:
                cnt += 1
        global max_ans
        if max_ans < cnt:
            max_ans = cnt
        return

    
    if  egg_list[idx][0] <= 0:  # 쥔 계란이 이미 부서진 것이라면
        solve(idx + 1)
        return  # 왜 return 해야됨? 그냥 다음으로 넘어가기 만을 원하니까. 밑에 함수 내용들을 또 수행하면 문제가 됨.
    
    
    for i in range(N):
        # 본인을 치면 안된다
        if i == idx:
            continue
    
        if egg_list[i][0] <= 0:
            solve(idx + 1)
            continue
        # 박치기 시작 무게에 따라서 각 계란의 내구성을 조절
        egg_list[i][0] -= egg_list[idx][1]
        egg_list[idx][0] -= egg_list[i][1]
        # 들어올린 계란의 바로 오른쪽 계란으로 이동
        solve(idx + 1)
        
        # 백트래킹할거니까 다시 원상복구 시켜줘야함.
        egg_list[i][0] += egg_list[idx][1]
        egg_list[idx][0] += egg_list[i][1]
        



N = int(input())    # N은 계란 개수
egg_list = [list(map(int, input().split())) for _ in range(N)]    #(내구도, 무게) 내구도 idx = 0, 무게 idx = 1
max_ans = 0
solve(0)
print(max_ans)