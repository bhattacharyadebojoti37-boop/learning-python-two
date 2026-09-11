#7.	Write a Python program to accept a sentence and find the longest word in the sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)