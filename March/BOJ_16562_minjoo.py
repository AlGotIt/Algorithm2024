n, m, k = map(int, input().split())
costs = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

def dfs(vertex):
    visited[vertex] = True
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            dfs(curr_v)

# 이미 모든 학생이 친구 관계에 있는 경우 추가 비용 없이 가능
total_cost = sum(costs)
if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")
