s=str(input())
l=[]
for i in s:
    l.append(i)
t=1
s1=""
for i in range(1,len(l)):
    if l[i-1] == l[i]:
        t+=1
    else:
        s1+=l[i-1]+str(t)
        t=1
s1+=l[len(l)-1]+str(t)   
print(s1)
