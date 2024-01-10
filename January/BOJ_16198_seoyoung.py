n = int(input())
weight = list(map(int, input().split()))

arr = [[0, weight]]
while arr:
    if len(arr[0][1]) == 3: 
        break
    item = arr.pop(0)
    arg_arr = item[1]
    for i in range(1, len(arg_arr)-1):
        new_arr = arg_arr[:i] + arg_arr[i+1:]
        arr.append([item[0]+arg_arr[i-1]*arg_arr[i+1], new_arr])

print(arr)
result = []
for i in arr:
    result.append(i[0])
print(max(result) + weight[0]*weight[n-1])
