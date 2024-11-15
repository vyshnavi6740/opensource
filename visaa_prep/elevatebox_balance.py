n=int(input())
t=list(map(int, input().split(" ")))
for i in range(n):
    s=abs(sum(t[:i])-sum(t[i+1:]))
    print(s,end=" ")
