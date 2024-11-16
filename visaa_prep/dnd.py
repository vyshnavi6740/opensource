n,m=map(int, input().split())
t=0
k=0
s=list(map(int, input().split()))
for i in s:
    if i%m==0:
        t+=i
    else:
        k+=i
print(t-k)
