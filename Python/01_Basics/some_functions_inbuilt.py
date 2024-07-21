myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print
# input
# type
type(myList) #==> List
# int, float, list, tuple, dict, complex
# abs --> returns absolute value
abs(-4) # returns 4
# pow --> returns power
pow(2, 3) # 8
# min/max
min(myList) # 1
max(myList) # 10
# round --> give round value when no extra parameter was passed but if parameter passed for fload val then . er pore tota didgit thake
round(3.145751654, 2) # 3.14
# divmod --> returns as a tuple (x // y, x % y)
divmod(5, 2) # (2, 1)
# bin/oct/hex --> binary, octal and hexadecimal converstion 
# id --> returns memory address from your pc
print(id(myList)) # 2768040745216
# ord --> returns AASCI value 
print(ord('A')) # returns 65
# len --> returns length of any iterables
len(myList) # 10
# sum --> returns sum of iterables starting value by default is 0
print(sum(myList, start=10)) # 65
# help --> if we want to know any function documentation then we use help
help('sum')