def countingSort(arr):
    count=[0]* 100
    for num in arr:
        count[num]+=1
    sorted_arr=[]
    for i in range(100):
        sorted_arr.extend([i]*count[i])
    return sorted_arr
n=int(input())
arr=list(map(int,input().split()))
result=countingSort(arr)
print(*result)
