tar,N=map(int,input().split())
coins=list(map(int,input().split()))
INF=10**9
arr=[INF]*(tar+1)
parent=[-1]*(tar+1)
arr[0]=0
for i in range(1,tar+1):
    for j in coins:
        if j<=i and arr[i-j]+1<arr[i]:
            arr[i]=arr[i-j]+1
            parent[i]=j
if arr[tar]==INF:
    print(-1)
else:
    result=[]
    x=tar
    while x>0:
        result.append(parent[x])
        x-=parent[x]
    print(arr[tar])
