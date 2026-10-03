N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[float('inf')]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if a[i][j]==2:
            dp[i][j]=0
for i in range(N):
    for j in range(M):
        if a[i][j]!=0:
            if i>0:
                dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
            if j>0:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
for i in range(N-1,-1,-1):
    for j in range(M-1,-1,-1):
        if a[i][j]!=0:
            if i<N-1:
                dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
            if j<M-1:
                dp[i][j]=min(dp[i][j],dp[i][j+1]+1)
ans=0
for i in range(N):
    for j in range(M):
        if a[i][j]==1:
            if dp[i][j]==float('inf'):
                print(-1)
                exit()
            ans=max(ans,dp[i][j])
print(ans)
