myDict = {"name": "Ankit", "gender": "male", "age": 21, "position": "backend developer"}

key_len_greater_4 = {key: value for key, value in myDict.items() if len(key) > 4}

print(key_len_greater_4)   # {'gender': 'male', 'position': 'backend developer'}

#  if we want to print list items as key and their sqares as their values

numList = list(range(1, 21))

sqTable = {item: item ** 2 for item in numList}

print(sqTable)

