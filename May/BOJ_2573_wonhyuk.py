import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
visited = [[0] * M for _ in range(N)]

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(r, c):
    stack = [(r, c)]
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = 1
                stack.append((ny, nx))

def melt():
    global arr
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
                        cnt += 1
                tmp[i][j] = max(0, arr[i][j] - cnt)
    arr = tmp

# 빙산 갯수
ice = 1
year = 0

while ice == 1:
    melt()

    ice = 0  # 처음에는 0으로 초기화
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j)
                ice += 1
    
    year += 1
    visited = [[0] * M for _ in range(N)]

if ice == 0:
    print(0)
else:
    print(year)