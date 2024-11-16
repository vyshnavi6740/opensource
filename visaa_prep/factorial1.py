n=int(input())
if n==0:
    print("1")
else:
    s=1
    for i in range(1,n+1):
        s*=i
    print(s)
