x,n=map(int, input().split())
t=x*100
k=(n-t)/100
if int(k)<k:
    l=int(k)
    l+=1
else:
    l=k+0
print(int(l))
