a,b=map(int,input().split())
while b!=0:
    carry=a&b
    a=a^b
    b=carry<<1
print(a)
