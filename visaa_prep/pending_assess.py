x,t,d=map(int, input().split(" "))
tr=x*t
tt=d*24*60
if tr<=tt:
    print("YES")
else:
    print("NO")
