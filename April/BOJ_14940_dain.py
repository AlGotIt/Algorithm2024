import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * C for _ in range(R)]
mapping = [list(map(int, input().split())) for _ in range(R)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while(q):
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mapping[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = 0
            if mapping[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
for x in range(R):
    for y in range(C):
        if not mapping[x][y]:
            visited[x][y] = 0
        if mapping[x][y] == 2:
            bfs(x, y)

for line in visited:
    for l in line:
        print(l, end=' ')
    print()