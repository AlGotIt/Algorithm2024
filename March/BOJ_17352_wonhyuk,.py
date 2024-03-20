import sys

input = sys.stdin.readline

def union(a: int, b: int):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        net[pb] = pa
    else:
        net[pa] = pb

def find(m: int):
    if net[m] is not m:
        net[m] = find(net[m])
    return net[m]

N = int(input())

net = [num for num in range(N)]

for _ in range(N-2):
    a, b = map(int, input().split())
    union(a-1, b-1)

for i in range(1, N):
    if find(0) is not find(i):
        print(1, i+1)
        break