myList = [1, 1, 2, 2, 3, 3, 2, 2, 4, 5 , 5]
# out --> [1, 2, 3, 4, 5]

L = list()

for i in myList:
    if i not in L:
        L.append(i)
print(L)


# Using set
mySet = set(myList)

print(mySet)

