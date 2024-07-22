# syntax = []

age = [21, 19, 36, 31]
print(age)

# it can store any datatype inside one variable 
intern = ['Ankit Chitrakar', 21, 'python backend']
print(intern)

# string to list (store every characters)

x = 'Ankit'
name = list(x)
print(name)

"""
list are i. Ordered => They maintain ordered of elements
         ii. Mutable ==> List are changeable after creation
         iii. Allow Duplicates => List allow duplicates 
"""

# Accesing 
lang = ['Python', 'Java', 'Javascript', 'CPP']
# print(lang[0])
# print(lang[1])

print(lang[-1]) # accesing last element use -1
print(lang[-3]) # accessing 3rd last element use -3

# Slicing in python

prog = 'Python Program'
progList = list(prog) # ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm']

sliceProg = progList[2: ]
print(sliceProg)
print(progList[5: 10]) # Exclude last index 

# Add element to python List
"""
methods: i. append() --> Automatically add the new element at the end of list
         ii. insert() --> If we add element at any index
"""

myFav = ['Javascript', 'Java', 'Python']
myFav.append('C') # assign this to the end of list at index 3

print(myFav) #['Javascript', 'Java', 'Python', 'C']


"""
when we add multiple item at a time at the end of the list then we use extend()
"""
myFav.extend(["Golang", "Devops", "Ruby"])
print(myFav)

# basic diff btwn append and extend is append only add one element at a time but extend add multiple element at a time in a list


myFav.insert(2, 'CPP')

print(myFav) # ['Javascript', 'Java', 'CPP', 'Python', 'C']



"""
Update List Items

"""
colors = ['Red', 'Yellow', 'Green']

colors[1] = 'Orange'

print(colors) #['Red', 'Orange', 'Green']

"""
Delete an item from a list
i. remove() --> takes the element and delete if the element was not presesnt in the list then give an error
ii. pop()  --> takes index as arguments and delete this index 
                if any argumaent was not pass then automatically pop the last index in the list

"""

num = [2, 4, 7, 9, 11, 13, 14]
num.remove(4)

print(num)  #[2, 7, 9]

remove_element = num.pop(-2)

print("Remove element = ", remove_element, "Num = ",num)  #Remove element =  13 Num =  [2, 7, 9, 11, 14]

remove_ele2 = num.pop()

print("Remove element = ", remove_ele2, "Num = ",num)  #Remove element =  14 Num =  [2, 7, 9, 11]

# List length

print('Length of the List = ', len(num))  #Length of the List =  3

"""
Iterating through a list

i. for in loop

"""

fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

# clear() is used for remove all the list item in single time 
fruits.clear() 

print(fruits)  # []

# index() is return the first occurence of any list

hobby = ['cricket', 'football', 'hockey', 'hockey', 'football', 'handball', 'cricket', 'cricket', 'cricket', 'cricket']

hockeyIndex =  hobby.index('hockey')

print(hockeyIndex) # 2
print(hobby.index('handball')) #5  
# print(hobby.index('handball1')) # if not present then give an error  

# count() is return the total occurence in the list if not presnt then returns 0
 
count = hobby.count('cricket')
print(count)  # 5


count = hobby.count('cricket111')
print(count)  # 5


"""
Sort list --> i. Ascending
              ii. Desc

List Sort --> i. Only number sort
            ii. Contains string sort
"""

prime_numbers = [11, 3, 5, 17, 23]

prime_numbers.sort()  # Ascending

print(prime_numbers) #[3, 5, 11, 17, 23]

prime_numbers.sort(reverse=True)  # Desc    

print(prime_numbers) 


# Contains string sort

cities = ["Tokyo", "London", "Washington D.C", "Kolkata", "Berlin", "Tokyo"]

cities.sort()    # ['Berlin', 'Kolkata', 'London', 'Tokyo', 'Tokyo', 'Washington D.C'

print(f"Dictionary order {cities}")  

cities.sort(reverse=True)   #['Washington D.C', 'Tokyo', 'Tokyo', 'London', 'Kolkata', 'Berlin']
print(f"Dictionary order {cities}") 

# Reverse a List used reverse() method

systems = ['Windows', 'macOS', 'Linux']

# systems.reverse()   #['Linux', 'macOS', 'Windows']

# print(systems)


# Reverse using Slice method
# Syntax: reversed_list = systems[start:stop:step] 
reverseList = systems[::-1]

print(reverseList)



# Shalow copy of a List by copy()

prime = [3, 5, 11]
num1 = prime.copy()

# print(num1)

num1.append(13)
num1.append(17)

print("Main List = ",prime)
print("Copy List = ",num1)

# Copy list by using = operator  (DEEP COPY)

myList = [10, 20, 30, 40, 50]

duplicateList = myList

duplicateList.append(70)
duplicateList.append(60)

myList.insert(2, 15);

print("Main List = ",myList)
print("Copy List = ",duplicateList)

# here by = operator duplicateList points to the same object of myList 
# so when I used to modify on any list (original/duplicate) then the whole list will change 

# ******* For shalow copy we used .copy()  and for Deep copy we used = opearator



# Write a function to find the largest number in a list.

def  find_Largest(numbers):
    if not numbers:
        return None  # check if the list is empty or not
    
    #initialize the max val by first index
    maxi = numbers[0]
    
    #iterate through the list from the 1st index and check if there was any larger value than maxi if yes update this with maxi if not return maxi
    
    for num in numbers[1: ]:
        if num > maxi:
            maxi = num
    
    return maxi

# Test the func find_Largest

tsetList = [2, 6, 3, 9, 12, 70, 3, 2, 15]
largest = find_Largest(tsetList)
print(f"Largest = {largest}")
    
tsetList.append(88)
# Now use the built in funtion

largest_Num = max(tsetList)
print(f"Largest = {largest_Num}")


