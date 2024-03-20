import sys

input = sys.stdin.readline

scenario = int(input())

def solver(n: int, rels, pairs):
    net = [num for num in range(n)]

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
    
    for a, b in rels:
        union(a, b)

    for u, v in pairs:
        print(int(find(u) == find(v)))

for i in range(scenario):
    n = int(input())
    k = int(input())
    rels = []
    for _ in range(k):
        a, b = map(int, input().split())
        rels.append((a, b))
    m = int(input())
    pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        pairs.append((u, v))

    print(f"Scenario {i+1}:")
    solver(n, rels, pairs)
    print()
