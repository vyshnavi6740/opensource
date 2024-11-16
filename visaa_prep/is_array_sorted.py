s=int(input())
t=list(map(int, input().split(" ")))
k=sorted(t)
if t==k:
    print("true")
else:
    print("false")
