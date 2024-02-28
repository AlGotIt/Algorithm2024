from itertools import combinations

N, L, R, X = map(int, input().split())
q = list(map(int, input().split()))
answer = 0
q.sort()

for n in range(N - 1):
    for i in range(N - 1, n, -1):
        if q[i] - q[n] >= X:
            for j in range(i - n):
                for C in combinations(q[n + 1 : i], j):
                    sum = q[n] + q[i]
                    for c in C:
                        sum += c
                    if L <= sum <= R:
                        answer += 1
print(answer)
