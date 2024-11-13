n=int(input())
l=[]
for i in range(n):
    s=int(input())
    l.append(s)
for i in range(len(l)):
    if l[i]>=30:
        print("YES")
    else:
        print("NO")
    
