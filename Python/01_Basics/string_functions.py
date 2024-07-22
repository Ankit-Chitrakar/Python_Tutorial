# String Fuctions
# Common Function
# Len, Max, Min, Sorted
username = "AnkitChitrakar"

print(len(username)) #returns length -->  14

print(min(username)) # returns min character based on AASCII value --> A
print(max(username)) # returns max character based on AASCII value --> t

print(sorted(username)) # returns character as a list default = ascending but when we gave reverse= TRue then desc
print(sorted(username, reverse=True)) # returns character as a list default = ascending but when we gave reverse= TRue then desc


# __________________________________________________

# 1. Capitalized, Title, Upper, Lower, Swapcase

str = "kolkata is city of joy"

print(str.capitalize())  # capitalized only the firts character of whole string --> Kolkata is city of joy

print(str.title())  # capitalized each word's first character --> Kolkata Is City Of Joy

print(str.upper()) # uppercase all the char --> KOLKATA IS CITY OF JOY

print(str.lower()) # lowercase all the char --> kolkata is city of joy

print(str.swapcase()) # toggle charcater casing --> KOLKATA IS CITY OF JOY

# _____________________________________________________________

# 2. Count

print(str.count('o'))   # returns frequency of character/substring  --> 3
print(str.count("is"))  #--> 1

# ____________________________________________________________

# 3. Find, Index

print(str.find("joy")) # returns starting index of first occerence of that character/substring --> 19

print(str.find("India")) # if the substring/character doesnot presnt in the string then simply returns -1


print(str.index("joy")) # returns starting index of first occerence of that character/substring --> 19

# print(str.index("India")) # give an error when character/substr is not presesnt in tye string so better to use .find()

# _________________________________________________________

# 4. stratswith, endswith

print(str.startswith("kol")) # returns True if not then returns False
print(str.endswith("Jaya")) # returns false if present then print True

# ____________________________________________________

# 5. format 
print("My name is {}. I am {} years old.".format("Ankit Chitrakar", 21))
print("My name is {1}. I am {0} years old.".format("Ankit Chitrakar", 21))
print("My name is {name}. I am {age} years old.".format(name = "Ankit Chitrakar", age = 21))
print("My name is {age}. I am {name} years old.".format(name = "Ankit Chitrakar", age = 21))
print("My name is {age}. I am {weight} years old.".format(name = "Ankit Chitrakar", age = 21, weight = 72))


# ___________________________________________________________________________

# 6. isalnum, inalpha, isdecimal, isdigit, isidentifier

print("ABCD12".isalnum()) # returns true but if we do this "ABCD12@" then print False

print("ABCD".isalpha()) # print True

print("1234".isdigit()) # print True

print("0122".isdecimal()) # print True (0-9)

# __________________________________________________________________________

# 7. Split, Join

str = "My name is Ankit Chitrakar"

print(str.split()) # returns a list with all words splits by " " by default but we change by giving "/", "-" as wish
# ['My', 'name', 'is', 'Ankit', 'Chitrakar']


print(" ".join(['My', 'name', 'is', 'Ankit', 'Chitrakar']) )   #My name is Ankit Chitrakar
print("/".join(['My', 'name', 'is', 'Ankit', 'Chitrakar']) )   #My/name/is/Ankit/Chitrakar
print("-".join(['My', 'name', 'is', 'Ankit', 'Chitrakar']) )   #My-name-is-Ankit-Chitrakar


# __________________________________________________________________

# 8. Replace

str = "My name is Ankit"
print(str.replace("Ankit", "Tiasa")) # My name is Tiasa

str = str.replace("Ankit", "Tiasa")  # also can returns and store this value
print(str)

# ________________________________________________________

# 9. Strip

# this is actually .trim() in js/ java

name = "                          Ankit                             "
print(name)
print(name.strip())  # remove spcaes from first and last
