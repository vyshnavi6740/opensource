t=int(input())
for i in range(t):
    m,n=map(int, input().split(' '))
    if m>n:
        print(m-n)
    else:
        print("0")
