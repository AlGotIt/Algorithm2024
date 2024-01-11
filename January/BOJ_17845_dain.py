import sys

input = sys.stdin.readline
N, K = map(int, input().split())
subjects = [0 for _ in range(K)]

for i in range(K):
    temp = list(map(int, input().split()))
    subjects[i] = temp

dp = [[0] * (N + 1) for _ in range(K + 1)]

for sub in range(1, K + 1):
    for time in range(1, N + 1):
        if subjects[sub - 1][1] > time:
            dp[sub][time] = dp[sub - 1][time]
        else:
            dp[sub][time] = max(
                subjects[sub - 1][0] + dp[sub - 1][time - subjects[sub - 1][1]],
                dp[sub - 1][time],
            )
            
print(dp[K][N])
