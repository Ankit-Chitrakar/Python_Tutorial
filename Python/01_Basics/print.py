# How can we print anything using python

print("India", "Pakistan", "Nepal", "Bangladesh") # India Pakistan Nepal Bangladesh

# If we want to print not with ' ' but a '-' or '/' thing then we can do it by sep='-'

print("India", "Pakistan", "Nepal", "Bangladesh", sep='-') # India-Pakistan-Nepal-Bangladesh

# By default print() has a '\n' by end 

print('hello')
print('world')

# hello
# world

# if we want to prevent this default behaviour then we use end operator

print("hello", end=' ')
print("world")

# hello world