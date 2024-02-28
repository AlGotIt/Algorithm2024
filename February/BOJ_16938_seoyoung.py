from itertools import combinations

n, l, r, x = map(int, input().split())
items = list(map(int, input().split()))
items.sort()
result = 0

for i in range(2, n+1):
    combos = combinations(items, i)
    for combo in combos:
        n = 0
        for c in combo:
            n += c
        if n >= l and n <= r and (combo[i-1] - combo[0]) >= x:
            result += 1
print(result)