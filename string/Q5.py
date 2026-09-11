#5.	Write a Python program to accept a string and a character, and find how many times the character occurs in the string.
string = input("Enter a string: ")
character = input("Enter a character: ")

string = string.lower()
character = character.lower()

count = 0

for ch in string:
    if ch == character:
        count = count + 1

print("The character occurs", count, "times.")