def get_cycle_length(num,cache):
    original=num
    count=1
    while num>1:
        if num in cache:
            count+=cache[num]-1
            break
        if num%2==0:
            num//=2
        else:
            num=3*num+1
        count+=1
    cache[original]=count
    return count
m,n=map(int,input().split())
start=min(m,n)
end=max(m,n)
cache={}
max_cycle=0
for i in range(start,end+1):
    current_length=get_cycle_length(i,cache)
    if current_length>max_cycle:
        max_cycle=current_length
print(f"{m} {n} {max_cycle}")
