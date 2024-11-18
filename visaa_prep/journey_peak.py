n=int(input())
s=list(map(int, input().split()))
t=0
x=0
for i in range(len(s)):
    x=x+s[i]
    t=max(x,t)
print(t)
