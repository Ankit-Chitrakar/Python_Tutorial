# There are 3 types of datatype in pythin

# 1. Basic Datatypes --> (Integer, Float, Complex, Boolean, None, String)
# 2. Container Types --> (List, Tuples, Set, Dictionary)
# 3. User Defined Types --> (Class)

#1. Basic Datatypes -->
#  i. Integer

a = 10
print(10) # 10

# ii. Float 
a = 10.005
print(a) # 10.005 


# iii. Complex
a = 10 + 5j
print(a) # (10+5j)

# iv. Boolean
a = True
print(a) # True   


# v. None
a = None
print(a) # None   


# vi. String
a = "Ankit Chitrakar"
b = 'Ankit Chitrakar'
c = """Ankit Chitrakar"""

print(a, b, c, sep='\n') # Ankit Chitrakar
                        # Ankit Chitrakar
                        # Ankit Chitrakar


# __________________________________________________________

# 2. Container Types

# i. List (Syntax = [] ==> Like array in others language)
a = [10, 20, 30]
print(a)  # [10, 20, 30]


# ii. Tuple (Syntax = () ==> Same as List but modification is not allowed)
a = (10, 20, 30)
print(a) # (10, 20, 30)

# a[0] = 20   # 'tuple' object does not support item assignment
# print(a)

# iii. Set (Syntax = {} ==> Conatining only unique values and not maintaing any order)
a = {10, 20, 20, 10, 30, 40}
print(a) # {40, 10, 20, 30}


# iv. Dictionary (Syntax = {key: value} ==> key is unique for accessing fast)
a = {"name": "Ankit Chitrakar", "age": 21, "gender": "male", "position": "Intern software developer"}
print(a) # {'name': 'Ankit Chitrakar', 'age': 21, 'gender': 'male', 'position': 'Intern software developer'}




