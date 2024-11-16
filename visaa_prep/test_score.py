x,y,z=map(int,input().split(" "))
tt=x*y
if tt>=z and z%y==0:
    print("YES")
else:
    print("NO")
