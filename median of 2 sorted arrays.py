n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
cou=sorted(arr1+arr2)
a=len(cou)
if a%2!=0:
    print(cou[a//2])
if a%2==0:
    print((cou[(a//2)-1] + cou[a//2]) / 2)
