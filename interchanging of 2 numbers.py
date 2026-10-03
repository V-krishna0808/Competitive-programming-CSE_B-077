n=int(input())
arr=list(map(int,input().split()))
min_index=0
max_index=0
for i in range(1, n):
    if arr[i]<arr[min_index]:
        min_index=i
    if arr[i]>arr[max_index]:
        max_index=i
arr[min_index],arr[max_index]=arr[max_index],arr[min_index]
print(*arr)
