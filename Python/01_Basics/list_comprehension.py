myList = [1, 2, 3, 4, 5]

l1 = [num * 2 for num in myList]  # gave the output of [2, 4, 6, 8, 10]
print(l1)

l2 = [num ** 2 for num in range(0, 11)]
print(l2) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Print only sqare of even number from range of 0 to 20

sq_even_list = [num ** 2 for num in range(0, 21) if num % 2 == 0]
print(sq_even_list)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

fruits = ['Apple', 'Orange', 'Guava', 'Watermelon', 'Papaya', 'Mango', 'Pinaple']

fruit_contains_n = [fruit for fruit in fruits if 'n' in fruit]
print(fruit_contains_n) # ['Orange', 'Watermelon', 'Mango', 'Pinaple']

