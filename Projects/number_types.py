n=int(input()) 
print("Perfect" if sum(i for i in range(1,n) if n%i==0)==n else "Not Perfect") 
print("Armstrong" if sum(int(d)**len(str(n)) for d in str(n))==n else "Not Armstrong") 
print("Palindrome" if str(n)==str(n)[::-1] else "Not Palindrome") 
