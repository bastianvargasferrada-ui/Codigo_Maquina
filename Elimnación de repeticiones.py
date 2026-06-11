my_list2 = [1, 2, 4, 4, 2]
my_list = []

for number in my_list2:
    if number not in my_list:
        my_list.append(number)



print("La lista con elementos únicos:")
print(my_list)


