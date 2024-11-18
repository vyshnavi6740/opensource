n=int(input())
s=list(map(int, input().split()))
k=int(input())
t=0
for i in range(len(s)):
    if s[i]==k:
        t=i
if t:
    print(t)
else:
    print("-1")
