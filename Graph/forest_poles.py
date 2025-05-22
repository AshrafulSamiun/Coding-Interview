def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
    return True

def forest_power_grid():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    #print(edges)
    edges.sort(key=lambda x: x[2])
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    total_cost = 0
    count = 0

    for u, v, w in edges:
        if union(parent, rank, u, v):
            total_cost += w
            count += 1

    print(total_cost if count == n - 1 else -1)

# Run the function
forest_power_grid()
