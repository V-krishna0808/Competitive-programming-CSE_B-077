def binary_division(x, y):
    if y == 0:
        return "Division by zero is not possible"
    sign = -1 if(x < 0) ^ (y < 0) else 1
    x,y=abs(x),abs(y)
    low,high=0,max(1,x)
    eps=1e-9
    while high-low>eps:
        mid = (low+high)/2
        if abs(y*mid-x)<eps:
            break
        elif y*mid<x:
            low=mid
        else:
            high=mid
    result=(low+high)/2
    result*=sign
    if abs(result-round(result))<eps:
        return int(round(result))
    else:
        return round(result,6)
x,y=map(float,input().split())
print(binary_division(x,y))
