from collections import deque

def solve(n, m, k, positions):
    matrix = [[0] * m for _ in range(n)]
    for x, y in positions:
        matrix[x-1][y-1] = 1
    
    matrix[0][0] = 1
    
    cnt = 0
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        if matrix[x][y] == 0:
            cnt += 1
            matrix[x][y] = 2
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    queue.appendleft((nx, ny))
                elif matrix[nx][ny] == 1:
                    queue.append((nx, ny))
    if matrix[n-1][m-1] == 1:
        return cnt
    else:
        return -1

n, m, k = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(k)]
print(2)
# result = solve(n, m, k, positions)
# print(result)