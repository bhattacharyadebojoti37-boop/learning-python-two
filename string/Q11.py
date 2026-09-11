#11.	Write a Python program to remove duplicate characters from a string while maintaining the original order.
st=(input("Enter a number: " )).lower()
r=""
for c in st:
    if c not in r:
        r+=c
print("output: ",r)