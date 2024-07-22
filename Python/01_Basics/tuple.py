# We can't modify a tuple once it is crreated


numbers = (1, 2, -6)

print(numbers)

myTup = tuple(('Ankit', 'Tiasa', 'Diya', 'Rupsha', 'Arpan'))

print(myTup)

# Tuple characteristics = i. Tuple is Ordered
                        # ii. Immutable
                        # iii. Allow duplicates
                        
# Accessing within Tuple

print(myTup[1: ])
print(myTup[1])

# myTup[1] = 'Banhee'  # TUPLE can't be mo  dified after initialization


for name in myTup:
    print(name) 
    
# check a element present in tuple or not

if 'soumen' in myTup: #No not presesnt
    print('Yes exists in tuple')
else:
    print('No not presesnt')
    

# delete tuple
del myTup

# print(myTup)
    
# String ************************
# split()

wrd = 'Python is a great language. Everyone should learn this asap!'

myList = wrd.split()

print(myList)

replace_txt = wrd.replace('Python', 'Javascript')

print(replace_txt)
