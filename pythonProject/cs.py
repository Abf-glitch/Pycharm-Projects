temperature = 46

if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal Temperature")

# A simple Program to return the largest number among three numbers
first = 90
second = 45
third = 69

if first > second and first > third:
    print(first, "is the largest number")
if second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the smallest number")

# Write a python program that checks whether a number is even or odd
num = 68
if num == 0:
    print("the number is odd")
elif num % 2 == 0:
    print("The number" + " " + str(num) + " " + "is even.")
else:
    print("The number" + " " + str(num) + " " + "is odd.")
