n=int(input())
l=list(map(int, input().split()))
k=int(input())
k=k % len(l)
s=l[-k:]+l[:-k]
print(*s)
