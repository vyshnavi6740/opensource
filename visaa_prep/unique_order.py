n=int(input())
s=list(map(int,input().split()))
t=[]
for i in s:
    if i not in t:
        t.append(i)
print(*t)
