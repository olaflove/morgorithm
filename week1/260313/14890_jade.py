def solve():
    n, l = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]


    def is_road_valid(road):
        placed = [False] * n
        
        for i in range(n - 1):
            if road[i] == road[i + 1]: continue

            diff = road[i] - road[i + 1]

            if abs(diff) > 1: return False
            
            if diff == 1:
                target = road[i + 1]
                for j in range(i + 1, i + 1 + l):
                    if (
                        j >= n 
                        or road[j] != target 
                        or placed[j]
                    ): return False
                    placed[j] = True
        
            if diff == -1:
                target = road[i]
                for j in range(i, i - l, -1):
                    if (
                        j < 0 
                        or road[j] != target 
                        or placed[j]
                    ): return False
                    placed[j] = True

        return True

    count = 0

    for row in grid:
        if is_road_valid(row):
            count += 1
    
    for col in zip(*grid):
        if is_road_valid(col):
            count += 1

    print(count)


if __name__ == "__main__":
    solve()