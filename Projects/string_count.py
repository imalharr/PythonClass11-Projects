s=input("Enter string: ")
v="aeiouAEIOU"
vowels=consonants=upper=lower=0
for ch in s:
    if ch.isalpha():
        if ch in v:
            vowels+=1
        else:
            consonants+=1
        if ch.isupper():
            upper+=1
        else:
            lower+=1
print(vowels,consonants,upper,lower)