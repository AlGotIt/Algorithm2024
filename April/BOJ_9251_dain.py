import sys

input = sys.stdin.readline

sen1 = input().strip().upper()
sen2 = input().strip().upper()

l1 = len(sen1) + 1
l2 = len(sen2) + 1

dp = [[0] * (l2) for _ in range(l1)]

for i in range(1, l1):
    for j in range(1, l2):
        if sen1[i-1] == sen2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])