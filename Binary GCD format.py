def gcd(m,n):
    while m!=n:
        if m==0 or n==0:
            return 0
        elif m&1==0:
            m=m>>1
        elif n&1==0:
            n=n>>1
        elif m>n:
            m=m-n
        else:
            n=n-m
    return m
m,n=map(int,input().split())
if m%2==0 and n%2==0:
    print(2*gcd(m,n))
else:
    print(gcd(m,n))
