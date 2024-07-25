# User will input (2numbers).Write a program to swap the numbers

num1 = int(input("Enter num: "))
num2 = int(input("Enter num: "))

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(num1, num2)