#4.	Write a Python program to count the number of: Alphabets, Digits, Spaces, Special characters in a given string.
st=input("Enter a string: ")
a=d=s=c=0
for i in st:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    else:
        c+=1
print("Alphabet: ",a)
print("Digits: ",d)
print("Space: ",s)
print("Special Characters: ",c)