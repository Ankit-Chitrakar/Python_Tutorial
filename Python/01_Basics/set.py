# this is non changeable 
# dont have duplicates value
# this is non ordered

# Create Set

student_id = {112, 113, 116, 119, 220};
print(student_id)

# Mix type of data store
data = {110, True, None, 5.05}

print(data)

print(type(data))  # set

# empty set 
st = set()
print(st)

empty_set = {}  # this is not a set this is dictionary

print(type(empty_set))

num = {2, 4, 5, 2, 4, 7}
print(num)

# Add element to set

num.add(10)
print(num)

# update method is used to add another set or can change existing data

prime_num = {2, 3, 5, 7, 11, 13}

num.update(prime_num)

print(num)

# Remove an element from a set use discard method

num.discard(13)

print(num)

# all() is to ckeck all value is True 
# all() is used to ckeck if the set is empty or not
# all() if any on element is 0 means false then gives false out return value

st = set()  # Hi

st = {1, 2, 3, 4}  # Hi

st = {1, 2, 3, 0}  # Bye

st = {0, 0, 0}  # Bye

if all(st):
    print('Hi')
else:
    print('Bye')    




# any() is to ckeck all value is True 
# any() is used to ckeck if the set is empty or not
# any() if any one element is true then gives true out return value

st = set()  # Bye

st = {1, 2, 3, 4}  # Hi

st = {1, 2, 3, 0}  # Hi

st = {0, 0, 0}  # Bye

if any(st):
    print('Hi')
else:
    print('Bye')    


#sorting  sorted return as a list sorted list

sortedSet = sorted(num)

print(sortedSet)

# sorting in tuple 

myTup = (4, 3, 5, 8, 19, 2, 6, 5, 4)

print(sorted(myTup))

myDict = {
    1: 'One',
    3: 'Three',
    8: 'Eight',
    2: 'Two',
    5: 'Five'
}

print(sorted(myDict))
print(type(sorted(myDict)))  # List 

my_set = {'u', 'i', 'o', 'a', 'e'}
print(sorted(my_set))

# Output: ['a', 'e', 'i', 'o', 'u']

# Desc sort
print(sorted(my_set, reverse=True))

# Sorting based on length of every element

fruits = ['apple', 'kiwi', 'mango', 'watermelon', 'jackfruit', 'guava']
print(sorted(fruits, key=len))    # ['kiwi', 'apple', 'mango', 'guava', 'jackfruit', 'watermelon']


# Difference btwn .sort() and sorted

# sorted() takes elements from original list and returns a new list with sorted element.
# the original string was unchanged 

#.sort() is not returning any sorted string 
# also this will change the original list because it points on same object 

# Union, Intersection, Difference, Symetric differnce

A = {0, 2, 4, 6, 8}; 
B = {1, 2, 3, 4, 5}; 

print("union = ",A | B)   #{0, 1, 2, 3, 4, 5, 6, 8}
print("Intersesctipon = ", A & B) # {2, 4}
print("Differnce = ", A - B) # {0, 8, 6}
print ("Symetrical Difference = ", A ^ B) # {0, 1, 3, 5, 6, 8} # i guess union - intersection

# Disjoin set --> A = {1, 3, 5} B = {2, 4, 6} hence two sets are disjoin set because intersection of these two set is null

num1 = {1, 3, 5}
num2 = {2, 4, 6}

if num1.isdisjoint(num2) == True:
    print("Yes! this two sets are disjoin set")
else:
    print("No it is not")



