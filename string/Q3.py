#3.	Write a Python program to accept a string and count the number of vowels and consonants in it
a=input("Enter a string: ")
a=a.lower()
x="aeiou"
c=v=0
for i in a:
    if i in x:
        v+=1
    elif i.isalpha():
        c+=1
print("No. of vowels: ",v)
print("No. of consonants: ",c)