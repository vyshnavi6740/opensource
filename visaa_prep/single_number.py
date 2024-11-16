n=int(input())
l1=list(map(int, input().split()))
l=[]
for i in l1:
    if i not in l:
        l.append(i)
    else:
        l.remove(i)
print(*l)
