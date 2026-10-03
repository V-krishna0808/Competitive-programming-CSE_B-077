import sys
def solve():
    input=sys.stdin.read
    data=input().split()
    if not data:
        return
    n=int(data[0])
    arr=[int(x) for x in data[1:n+1]]
    total_sum=sum(arr)
    target_count=n//2
    dp=[0]*(target_count+1)
    dp[0]=1  
    for weight in arr:
        for count in range(target_count,0,-1):
            dp[count]|=(dp[count-1]<<weight)
    min_diff=float('inf')
    for s in range(total_sum+1):
        if (dp[target_count]>>s)&1:
            diff=abs((total_sum-s)-s)
            if diff<min_diff:
                min_diff=diff
    print(min_diff)
if __name__=='__main__':
    solve()
