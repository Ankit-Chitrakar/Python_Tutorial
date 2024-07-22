# range function 
# syntax range(including number, excluding number) ==> return a sequence 
x = list(range(1, 11))
print(x)

x = list(range(15)) #starts from 0 to 14
print(x)

x = list(range(1, 10, 2)) # this step is the gap count
print(x) # 1 3 5 7 9

# reverses sequence
x = list(range(10, 0, -1))
print(x) # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# for loop syntax
for i in range(1, 11):
    print(i)

for i in "Kolkata":
    print(i)

# paskal trigangle using nested for loop

# *
# **
# ***
# ****
# *****

n = int(input("Enter row size: "))

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("")

