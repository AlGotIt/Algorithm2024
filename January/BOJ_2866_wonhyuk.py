R, C = map(int, input().split())
table = [input() for _ in range(R)]

low, high = 0, R-1
while low <= high:
    mid = (low + high) // 2

    ## mid 부터 마지막열까지의 문자열
    columns = [''.join(table[r][c] for r in range(mid, R)) for c in range(C)]

    if (len(columns) == len(set(columns))):
        ## 중복이 없을 경우 아래부터 중간
        low = mid  + 1
    else:
        ## 중복이 있을 경우 위 중간
        high = mid - 1

## 첫번째열 제거는 포함되지 않음
print(low - 1)