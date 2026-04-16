x=int(input("Enter x: "))
n=int(input("Enter n: "))
s1=s2=s3=s4=0
fact=1
for i in range(0,n+1):
    s1+=x**i
    s2+=((-1)**i)*(x**i)
for i in range(1,n+1):
    s3+=(x**i)/i
    fact*=i
    s4+=(x**i)/fact
print(s1)
print(s2)
print(s3)
print(s4)