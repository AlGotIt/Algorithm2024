DP = [[1], [1,1]]
for r in range(2, 31):
    row = [1]
    for c in range(1, r-1):
        row.append(DP[r-1][c-1] + DP[r-1][c])
    row.append(1)
    DP.append(row)
    
R, C, W = map(int, input().split())

gain = 1
answer = 0
for s in range(R, R+W):
    for e in range(C-1, C-1+gain):
        answer += DP[s][e]
    gain += 1

print(answer)