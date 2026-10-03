n = int(input())
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        current += arr[i]
    else:
        current = arr[i]
    maximum = max(maximum, current)
print(maximum)
