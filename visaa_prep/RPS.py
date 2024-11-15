v,c=map(str, input().split(" "))
if v=="S":
    if c=="P":
        print("Vignesh")
    elif c=="R":
        print("Charan")
elif c=="S":
    if v=="P":
        print("Charan")
    elif v=="R":
        print("Vignesh")
else:
    print("NULL")
    
