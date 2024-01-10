
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v-D): #U만큼 위로 or D만큼 아래로
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs(S))

# F,S,G,U,D = tuple(map(int, input().split()))

# def solution(F,S,G,U,D):
#   for i in range(F):
#     for j in range(F):
#       if U*i-D*j < 1 or U*i-D*j>F-S:
#         break
#       if U*i-D*j == G-S:
#         return i+j
#   return 'use the stairs'

# print(solution(F,S,G,U,D))

# F, S, G, U, D = tuple(map(int, input().split()))

# def solution(F, S, G, U, D):
#     for i in range(F + 1):
#         for j in range(F + 1):
#             if U * i - D * j == G - S:
#                 return i + j
#             if U*i-D*j < 1 or U*i-D*j>F-S:
#                 continue
#     return 'use the stairs'

# print(solution(F, S, G, U, D))
