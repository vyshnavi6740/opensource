v,c,r,x=map(int, input().split(" "))
if v+c>=x:
    print("YES")
elif v+r>=x:
    print("YES")
elif c+r>=x:
    print("YES")
else:
    print("NO")
