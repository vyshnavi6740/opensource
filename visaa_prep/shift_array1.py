n=int(input())
l=list(map(int, input().split()))
t=l[0]
l.remove(l[0])
l.append(t)
print(*l)
