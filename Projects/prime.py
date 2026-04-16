n=int(input("Enter number: "))
if n<2:
    print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Composite")
            break
    else:
        print("Prime")