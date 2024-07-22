# Syntax --> {key: Value}

capital = {
    'India': 'New Delhi',
    'West Bengal': 'Kolkata',
    'Germany': 'Berlin',
    'West Bengal': 'Kolkata',
}

print(capital)

# Keys are unique 

# Accessing Dict item
print(capital['West Bengal'])  # Kolkata

capital_of_westBengal = capital.get('West Bengal')
print(capital_of_westBengal)

print("By Get method",capital.get('West Bengal'))

# Add Item in Dictionary 
capital['Bangladesh'] = 'Dhaka'

print(capital)

#Remove/ delete dictionary item

# del capital['Germany']

# print(capital)

popped_Item = capital.pop('Bangladesh')

print(f"Popped item = {popped_Item} and dict = {capital}")

# if we popped a item which does not in the dictionary then its guve an error
# del capital['France']  # Gives an error

# popped = capital.pop('France')  # Give an error

# print(popped)

# Clear method clear all the dict item in one run
# capital.clear()



# popitem() dont take any parameter just delete the last in first out item

print("************************")
# deleted_item = capital.popitem()
# (delete_key, delete_value) = capital.popitem()

# print(deleted_item)
# print(delete_key, delete_value)

print(capital)  #{}

# Update Dictionary item 

capital['West Bengal'] = 'Sonarpur'

print(capital)

# update() method is used to add a new item, change a existing item

# Add external dict
another_capital = {
    'Pakistan': 'Lahore',
    'France': 'Paris',
    'UAE': 'Dubai'
}

capital.update(another_capital)

print(capital)

# Change existing item or update
capital_change = {
    'India': 'New Delhi',
    'West Bengal': 'Kolkata',
    'USA': 'New York'
}

capital.update(capital_change)

print(capital)

capital.update({'Japan': 'Tokyo'})


# Keys() and values() and items()

capital_keys = capital.keys()

capital_values = capital.values()

capital_items = capital.items()

print(f"Keys = {capital_keys}")  # Keys = dict_keys(['India', 'West Bengal', 'Germany', 'Pakistan', 'France', 'UAE', 'USA'])  --> As a List
print(f"Values = {capital_values}")  # Values = dict_values(['New Delhi', 'Kolkata', 'Berlin', 'Lahore', 'Paris', 'Dubai', 'New York'])  --> As a List
print(f"Items = {capital_items}")   # Items = dict_items([('India', 'New Delhi'), ('West Bengal', 'Kolkata'), ('Germany', 'Berlin'), ('Pakistan', 'Lahore'), ('France', 'Paris'), ('UAE', 'Dubai'), ('USA', 'New York')])
print(type(capital_items))  # Dict Items --> 


# Traversal of Keys(), Values() and items()
for country in capital_keys:
    print(country)
    
for capital in capital_values:
    print(capital)
    
for (key, value) in capital_items:
    print(key, ": ",value)
    

# fromKeys() take 2 parameters as keys and values
vowelKey = {'a', 'e', 'i', 'o', 'u'}
vowelVal = 'vowel'

vowels = dict.fromkeys(vowelKey, vowelVal)  # Does not in orderd form

print(vowels)



# Update() when any tuple is passed

myDict = {
    'x': 100,
    'y': 90
}

myDict.update([('z', 80)])

print(myDict)


# Copy()  --> Shalow copy

myDesc = {
    'name': 'Ankit Chitrakar',
    'age': 21,
    'role': 'Software Developer Intern'
}

print(myDesc)

copyDesc = myDesc.copy()

copyDesc.update({'hobby': 'cricket'})

print(copyDesc)
print(myDesc)

# Use = operator

duplicateDesc = myDesc;

duplicateDesc['intern'] = '6 months'

print(duplicateDesc)
print(myDesc)
