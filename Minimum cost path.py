n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*m for _ in range(n)]
dp[0][0]=a[0][0]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        best=10**18
        if i>0:
            best=min(best,dp[i-1][j])
        if j>0:
            best=min(best,dp[i][j-1])
        if i>0 and j>0:
            best=min(best,dp[i-1][j-1])
        dp[i][j]=a[i][j]+best
print(dp[n-1][m-1])
