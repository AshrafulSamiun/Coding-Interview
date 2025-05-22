from collections import deque

def doomsday_escape(n, m, doom_time):
    # Direction vectors: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False]*m for _ in range(n)]

    # Start BFS from (0, 0) at time 0
    queue = deque([(0, 0, 0)])  # (i, j, time)
    visited[0][0] = True

    while queue:
        x, y, t = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return "YES"
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nt = t + 1
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and nt < doom_time[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, nt))
    
    return "NO"

# Example usage:
n, m = map(int, input().split())
doom_time = [list(map(int, input().split())) for _ in range(n)]
print(doomsday_escape(n, m, doom_time))  # Output: YES
