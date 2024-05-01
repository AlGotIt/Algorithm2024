import sys
input = sys.stdin.readline

N = int(input())
sols = list(map(int, input().split()))
sols.sort()

if sols[0] >= 0:
    print(sols[0], sols[1], sols[2])
elif sols[-1] <= 0:
    print(sols[-3], sols[-2], sols[-1])
else:
    closest_sum = float('inf')
    result = []

    for i in range(N-2):
        left, right = i+1, N-1
        
        while left < right:
            current_sum = sols[i] + sols[left] + sols[right]
            
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = [sols[i], sols[left], sols[right]]
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                break

    print(" ".join(map(str, result)))