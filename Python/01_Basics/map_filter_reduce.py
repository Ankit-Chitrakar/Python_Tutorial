myList = [1, 2, 3, 4, 5]

print(list(map(lambda num: num * 2, myList))) # [2, 4, 6, 8, 10]


students = [
    {
        "name": "Ankit Chirakar",
        "father's name": "Bimal Chitrakar",
        "Address": "Sonarpur, Kolkata",
    },
    {
        'name': 'Tiasa Chirakar',
        "father's name": "Bhaskar Ash",
        "Address": "Boubazar, Kolkata",
    },
    {
        "name": "Arpan Ghosh",
        "father's name": "Soumen Mondal",
        "Address": "Belgharia, Kolkata",
    },
]

# print(map(lambda student: student['name'], students))  # returns a map object # <map object at 0x0000019C40399C60>

print(list(map(lambda student: student['name'], students)))  # this will print all names from the students json



# Fliter

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda num: num % 2 == 0, myList))) # returns a list with only even values # [2, 4, 6, 8, 10]

fruits = ['Apple', 'Orange', 'Guava', 'Watermelon', 'Papaya', 'Mango', 'Pinaple']

print(list(filter(lambda fruit: 'e' in fruit, fruits)))  # returbns a list which fruit contains a letter 'e' 
# ['Apple', 'Orange', 'Watermelon', 'Pinaple']



# Reduce

myCart = [
    {
        "courseName": "Full-stack web course",
        "price": 2999
    },
    {
        "courseName": "Node-js with Express js",
        "price": 1999
    },
    {
        "courseName": "Mobile Dev course",
        "price": 3999
    },
    {
        "courseName": "DSA course",
        "price": 4999
    },
    {
        "courseName": "Data Science course",
        "price": 12999
    },
]

#  all the items are add to cart 
# give me the total price to pay

from functools import reduce

total_price_in_cart = reduce(lambda acc, curr: acc+ curr['price'], myCart, 0)

print(total_price_in_cart)