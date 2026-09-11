#Write a Python program to check whether two strings are anagrams of each other.
st1=input("Enter first string: ")
st2=input("Enter second string: ")
if sorted(st1.lower())==sorted(st2.lower()):
    print("The strings match")
else:
    print("The strings do not match")
