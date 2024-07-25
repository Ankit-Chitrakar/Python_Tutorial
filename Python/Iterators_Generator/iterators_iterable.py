# Iterator->
# An Iterator is an object that alows you to travers through a sequence of data without having to store
# the entire data in the memory

myList = [i for i in range(0, 1000)]

# for i in myList:
    # print(i*2)

import sys

print(sys.getsizeof(myList))  # this will storev entire list in memory and then traverse

# now only takes range
x = range(0, 1000)

print(sys.getsizeof(x)) # this will not store entire memory this will store one object at a time load this doing operations and delete this from memeory and then load next 

# That's why we should use Iterator for memory optimization in python

# Iterable 
# in the iterable we can persorm iteration using iterator

# Iterable generates it's iterator by iter(iterable_name)

myList = [1, 2, 3]

iterator_myList = iter(myList)

type(iterator_myList) # type as iterator object 

# Identify iterator/iterable

# Iterable --> 

li = [1, 2, 3, 4, 5]

dir(li) # if dir(any object) gives a magic method named __iter__ then this is a iterable object

print(dir(li)) # here __iter__ is presesnt

# Iterator -->

iterator_li = iter(li)
print(dir(iterator_li)) # if any dir(iterable object) gives two magic methods named __iter__ and __next__ then it is a iterator


# Implementaton of for loop
num = [1, 2, 3]

iterator_num = iter(num)

print(next(iterator_num))
print(next(iterator_num))
print(next(iterator_num))
# print(next(iterator_num))  # this will give StopIteration error

# Make it won for loop

def make_my_for_loop(itearble):
    iterator = iter(itearble)

    while True:
        try:
            print(next(iterator), end=" ")
        except StopIteration:
            break

myList = [1, 2, 3, 4, 5]
mySet = {1, 2, 3}
myDict = {0:1,1:2,2:3}
myTup = (1, 2, 3)

make_my_for_loop(myList)
make_my_for_loop(mySet)
make_my_for_loop(myDict)
make_my_for_loop(myTup)