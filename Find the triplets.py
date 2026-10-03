n=int(input())
arr=list(map(int,input().split()))
x=int(input())
arr.sort()
found=False
for i in range(n-2):
    if i>0 and arr[i]==arr[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        s=arr[i]+arr[left]+arr[right]
        if s==x:
            print(arr[i],arr[left],arr[right])
            found=True
            left+=1
            right-=1
            while left<right and arr[left]==arr[left-1]:
                left+=1
            while left<right and arr[right]==arr[right+1]:
                right-=1
        elif s<x:
            left+=1
        else:
            right-=1
if not found:
    print("No Triplet Found")
