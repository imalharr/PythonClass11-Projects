import math 
x=int(input());n=int(input()) 
print(sum(x**i for i in range(n+1))) 
print(sum((-1)**i*x**i for i in range(n+1))) 
print(sum(x**i/(i+1) for i in range(n))) 
print(sum(x**i/math.factorial(i) for i in range(n+1))) 
