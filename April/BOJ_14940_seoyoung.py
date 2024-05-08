from collections import deque

def bfs(start_x, start_y, graph):
    way = [[-1]*m for _ in range(n)] 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    

    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    way[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited: # 그래프 안에 잇고 아직 방문하지 않앗다면
                if graph[nx][ny] == 1: # 갈 수 잇다면
                    visited.add((nx, ny))
                    way[nx][ny] = way[x][y]+1
                    queue.append((nx, ny)) 
                
    return way

def find_start(n, m ,graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return i, j

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

start_x, start_y = find_start(n, m, graph) # 시작점 인덱스 
result = bfs(start_x, start_y, graph)

# 갈 수 없었던 곳은 0으로 변환
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(" ".join(map(str, row)))

