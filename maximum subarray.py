n = int(input())
arr = list(map(int, input().split()))

current = maximum = arr[0]

for i in range(1, n):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)
