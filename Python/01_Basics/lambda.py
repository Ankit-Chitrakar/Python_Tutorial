# dont have name 
# single line function

# sqare of a number
x = lambda x: x ** 2
print(x(9))

# Sum of two numbers

sum = lambda x, y: x + y
print(sum(4, 5))

# Lambda function is used to create higher order function
# Higher order fyunction --> that takes function as a parameter inside an function

# Lets suppose we want to print odd sum, even sum and prime sum 

# then what we do 

# normal method

def checkPrime(number):
    flag = 0
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
            

def sum_operation(number_list):
    even_sum = 0
    odd_sum = 0
    prime_sum = 0

    for number in number_list:
        # check the number is even or odd
        if number % 2 == 0:
            even_sum += number
        elif number % 2 != 0:
            odd_sum += number
        if checkPrime(number):
            print(number)
            prime_sum += number
    return (even_sum, odd_sum, prime_sum)

myList = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(sum_operation(myList))

# Using Lambda Function

def sum_operation_lambda(function, number_list):
    result = 0
    for num in number_list:
        if function(num):
            result += num
    return result

even = lambda number: number % 2 == 0
odd = lambda number: number % 2 != 0

print(sum_operation_lambda(even, myList))
print(sum_operation_lambda(odd, myList))


# Lambda function is also used in Map, Filter, Reduce function in py