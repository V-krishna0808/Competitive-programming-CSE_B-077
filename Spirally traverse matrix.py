m,n=map(int,input().split())
mat=[]
for _ in range(m):
    mat.append(list(map(int, input().split())))
top,bottom=0,m-1
left,right=0,n-1
arr=[]
while top<=bottom and left<=right:
    for j in range(left,right+1):
        arr.append(mat[top][j])
    top+=1
    for i in range(top,bottom+1):
        arr.append(mat[i][right])
    right-=1 
    if top<=bottom:
        for j in range(right,left-1,-1):
            arr.append(mat[bottom][j])
        bottom-=1 
    if left<=right:
        for i in range(bottom,top-1,-1):
            arr.append(mat[i][left])
        left+=1  
print(*arr)
