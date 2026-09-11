#13.	Write a Python program to find the first character in a string that does not occur more than once.
st=input("Eanter:")
fu=None
for c in st:
    if st.count(c)==1:
        fu=c
        break
if fu:
    print("First non-repeted character:",fu)
else:
    print("No non-repeted character found:")