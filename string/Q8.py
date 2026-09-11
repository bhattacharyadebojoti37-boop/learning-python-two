#8.	Write a Python program to remove all spaces from a given string without using the replace() function.
s=input("Enter a string")
print("output:","".join (c for c in s if c !=" "))