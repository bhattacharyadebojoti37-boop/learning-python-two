#Write a Python program to maintain a list of numbers. Perform the following operations:
#Insert a new number at the end
#Insert a number at a given index
#Delete a number from the list
#Display all even numbers in the list
#Calculate the sum and average of numbers in the list
#Find the maximum and minimum
#Find the average of even numbers only
#Find the average of positive numbers only
#Create an empty list

numbers = []

# Take the number of elements from the user
n = int(input("Enter how many numbers: "))

# Add numbers to the list
for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

# Display the original list
print("Original list:", numbers)


# Insert a new number at the end
x = int(input("Enter number to insert at the end: "))
numbers.append(x)


# Insert a number at a given index
x = int(input("Enter number to insert: "))
pos = int(input("Enter index: "))
numbers.insert(pos, x)


# Delete a number from the list
x = int(input("Enter number to delete: "))

# Check whether the number is present
if x in numbers:
    numbers.remove(x)
else:
    print("Number not found")


# Display the updated list
print("Updated list:", numbers)


# Display all even numbers
print("Even numbers are:")

# Check every number in the list
for x in numbers:

    # Check whether the number is even
    if x % 2 == 0:
        print(x, end=" ")

print()


# Calculate the sum of all numbers
total = sum(numbers)

# Calculate the average
average = total / len(numbers)

print("Sum =", total)
print("Average =", average)


# Find the maximum number
print("Maximum =", max(numbers))

# Find the minimum number
print("Minimum =", min(numbers))


# Find the average of even numbers
even_sum = 0
even_count = 0

# Go through every number
for x in numbers:

    # Check if the number is even
    if x % 2 == 0:

        # Add the even number
        even_sum = even_sum + x

        # Count the even number
        even_count = even_count + 1


# Check if there are any even numbers
if even_count > 0:

    # Calculate the average of even numbers
    print("Average of even numbers =", even_sum / even_count)
else:
    print("No even numbers")


# Find the average of positive numbers
positive_sum = 0
positive_count = 0

# Go through every number
for x in numbers:

    # Check if the number is positive
    if x > 0:

        # Add the positive number
        positive_sum = positive_sum + x

        # Count the positive number
        positive_count = positive_count + 1


# Check if there are any positive numbers
if positive_count > 0:

    # Calculate the average of positive numbers
    print("Average of positive numbers =", positive_sum / positive_count)
else:
    print("No positive numbers")