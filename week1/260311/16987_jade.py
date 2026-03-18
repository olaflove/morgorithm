def solve():
    n = int(input())
    sturds = [0] * n
    weights = [0] * n
    for i in range(n):
        sturds[i], weights[i] = map(int, input().split())
    
    max_cnt = 0

    def backtrack(curr, broken_cnt):
        nonlocal max_cnt

        # base condition
        if curr == n:
            if broken_cnt > max_cnt:
                max_cnt = broken_cnt
            return

        # pruning
        if broken_cnt + (n - curr) * 2 <= max_cnt: return

        # skip broken egg
        if sturds[curr] <= 0 or broken_cnt == n - 1:
            backtrack(curr + 1, broken_cnt)
            return
        
        hit_flag = False
        for nxt in range(n):
            if nxt == curr or sturds[nxt] <= 0: continue

            hit_flag = True

            sturds[curr] -= weights[nxt]
            sturds[nxt] -= weights[curr]

            tmp = 0
            if sturds[curr] <= 0: tmp += 1
            if sturds[nxt] <= 0: tmp += 1
            
            backtrack(curr + 1, broken_cnt + tmp)

            sturds[curr] += weights[nxt]
            sturds[nxt] += weights[curr]
        
        # noting to hit
        if not hit_flag:
            backtrack(curr + 1, broken_cnt)

    backtrack(0, 0)
    print(max_cnt)

solve()