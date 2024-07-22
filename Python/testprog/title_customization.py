# "hello how are you"
# out-> Hello How Are You

str = "hello how are you. We are a very good foody men "

# Process 1
result = ""

str_list = str.split()

for i in str_list:
    i = i.capitalize()
    result += i + " "  


# print(result)  # Hello How Are You. We Are A Very Good Foody Men

# Process 2

str_list = str.split()
L = list()

for i in str_list:
    i = i.capitalize()
    L.append(i)
print(" ".join(L))  # Hello How Are You. We Are A Very Good Foody Men

