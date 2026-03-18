n = int(input())

def is_equal(arr):
    l = len(arr) // 2
    for m in range(1, l+1):
        cnt = 0
        for j in range(-2*m, -m):
            if arr[j] == arr[j+m]:
                cnt += 1
        if cnt == m:
            return True
    return False

arr = []
def backtrack(step):
    if is_equal(arr):
        return
    
    if len(arr) == n:
        print(''.join(map(str, arr)))
        exit()
        return
    
    for i in range(1, 4):
        arr.append(i)
        backtrack(step+1)
        arr.pop()

backtrack(0)