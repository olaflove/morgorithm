n = int(input())

def dfs(curr_str):
    if len(curr_str) == n:
        print(curr_str)
        exit()
        
    for char in '123':
        nxt = curr_str + char
        for i in range(1, len(nxt) // 2 + 1):
            if nxt[-i:] == nxt[-i * 2:-i]:
                break 
        else:
            dfs(nxt)

dfs('')