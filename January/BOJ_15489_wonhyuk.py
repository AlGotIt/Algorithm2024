R, C, W = map(int, input().split())

triangle = [[1]]

for i in range(1, R + W - 1):
    row = [1]
    for j in range(1, i):
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    row.append(1)
    triangle.append(row)

sum = 0
for i in range(W):
    for j in range(i + 1):
        sum += triangle[R + i - 1][C + j - 1]

print(sum)
