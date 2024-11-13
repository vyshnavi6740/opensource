n=int(input())
s=1
for i in range(1,n+1):
    for j in range(i):
        print(str(s),end=" ")
        s+=1
        j+=1
    i+=1
    print("")
