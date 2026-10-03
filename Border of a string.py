s=input().strip()
n=len(s)
le,ri=0,n-1
longlen=0
for i in range(1,n):
    if s[:i]==s[n-i:]:
        longlen=i
le=longlen
print(f"{s[0:le]}")
    
