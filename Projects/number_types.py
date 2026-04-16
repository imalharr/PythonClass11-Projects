num=int(input("Enter number: "))
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
print("Perfect:",s==num)
order=len(str(num))
s=sum(int(d)**order for d in str(num))
print("Armstrong:",s==num)
print("Palindrome:",str(num)==str(num)[::-1])