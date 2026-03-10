from itertools import combinations

def get_data():
    n, m = map(int, input().split())
    houses = []
    stores = []

    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(n):
            if row[c] == 1:
                houses.append((r, c))
            elif row[c] == 2:
                stores.append((r, c))

    return m, houses, stores

def solve(m, houses, stores):
    dist_matrix = []
    for hr, hc in houses:
        dist_matrix.append([abs(hr - sr) + abs(hc - sc) for sr, sc in stores])

    min_city_chicken_dist = float('inf')
    num_stores = len(stores)

    for selected_indices in combinations(range(num_stores), m):
        city_chicken_dist = 0
        
        for house_dist in dist_matrix:
            min_dist = 101
            for idx in selected_indices:
                if house_dist[idx] < min_dist:
                    min_dist = house_dist[idx]
            
            city_chicken_dist += min_dist
            
            if city_chicken_dist >= min_city_chicken_dist:
                break
        
        if city_chicken_dist < min_city_chicken_dist:
            min_city_chicken_dist = city_chicken_dist
        
    return min_city_chicken_dist

def main():
    m, houses, stores = get_data() 
    ans = solve(m, houses, stores)
    print(ans)

if __name__ == "__main__":
    main()