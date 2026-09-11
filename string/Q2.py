#Write a Python program to check whether a given string is a palindrome or not.
string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")