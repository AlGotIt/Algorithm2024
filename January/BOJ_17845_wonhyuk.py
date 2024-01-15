N, K = map(int, input().split())
courses = []

for _ in range(K):
    I, T = map(int, input().split())
    courses.append((I, T))

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, K+1):
    importance, time = courses[i-1]
    for j in range(1, N+1):
        if j - time >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + importance)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[K][N])