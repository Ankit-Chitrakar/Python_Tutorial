# generator is a special type of function who usually temprarily done the work and remmembered it's state and variable's value untill the next(generatr_object) has called

def generator_demo():

    yield "First Statement"
    yield "Second Statement"
    yield "Third Statement"
    yield "Fourth Statement"

    # in generator return is not used there use yield 

gen = generator_demo()

type(gen) # it gives a generator object 

# print(next(gen)) # firts statement
# print(next(gen)) # Second statement
# print(next(gen)) # Third statement
# print(next(gen)) # Fourth statement
# print(next(gen)) # Stop Error

# memorise previous state of work
# Eg->

print(next(gen)) # firts statement

for i in gen:
    print(i)   # it will start from second statemnet not from tghe first one bcz it's memorize it's previous state of line ehich is done in line 23


# Given numbers sqare print

def sqare_print(num):
    for i in range(1, num+1):
        yield i ** 2

nums_li = sqare_print(10)
print(next(nums_li)) #1
print(next(nums_li)) #4
print(next(nums_li), end="") #9
print("________________________") 
for num in nums_li: 
    print(num)   # here it is started from 16 to 100 not 1 to 100

# custom range function using generators

def my_range(start, end):
    for num in range(start, end):
        yield num

gen = my_range(15, 30)
# for i in gen:
    # print(i)  # print 15 to 30


# Generator exp 
myGenerator = (i ** 2 for i in range(1, 11))   # one line expression not writing any def and yeild
print(type(myGenerator))  # generator object

for i in myGenerator:
    print(i)

"""
Use of Generator
Memory Efficiency: Unlike list comprehensions that generate the entire list in memory, a generator expression produces items one by one using an iterator, which is much more memory efficient.
# Decorator

# func takes parameter a func and modifying this func within that and return modifying func


Performance: Since items are produced on demand, generator expressions can be faster for large datasets because they don't require the entire dataset to be loaded into memory at once.

Conciseness: A generator expression in one line makes the code more concise and often easier to read, especially for simple operations.

Lazy Evaluation: Generators perform lazy evaluation, which means they generate values only when needed. This can be useful in scenarios where you might not need all the values or when working with potentially infinite sequences.
"""


# Decorator

# func takes parameter a func and modifying this func within that and return modifying func

def my_decorator(func):
    def wrapper():
        print("*********************")
        func()
        print("""""""""""""""""""""""")
    return wrapper

def hello():
    print("Hello")

a = my_decorator(hello)
a()