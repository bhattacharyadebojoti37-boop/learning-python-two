#Write a Python program to find the frequency of every character in a string.
st=(input("Enter a string")).lower()
f={}
for c in st:
    f[c]=f.get(c,0)+1
for c,v in f.items():
    print(c,":",v)