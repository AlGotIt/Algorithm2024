import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R = map (int, sys.stdin.readline().split ())
tree = [[] for _ in range(N+1)]
visited = [False]*(N+1)
length = [0]*(N+1)
mid = N #기가노드

for i in range(N-1):
    n1, n2, l = map(int, sys.stdin.readline().split())
    tree[n1].append ([n2, l])
    tree[n2].append ([n1, l])


def DFS(node, l): #루트노드부터 시작!
    global mid, N
    visit = tree[node]
    visited[node] = True
    length[node] = l
    for v in visit:
        if mid == N and len(visit) > 2: mid = node
        if not visited[v[0]]:
            DFS(v[0], v[1]+l)

DFS(R,0)
if len(tree[R]) > 1: mid = R
print(length[mid], max(length)-length[mid])