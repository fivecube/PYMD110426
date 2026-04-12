from first_program import calculate_percentage


list_of_fruits = ['kiwi', 'water melon', 'apple', 'banana', 'orange', 'grapes', 'mango', 'blueberry']

vitamin_c_fruits = ['orange', 'grapes', 'blueberry', 'kiwi']

vitamin_k_fruits = ['banana', 'blueberry']

iron_fruits = ['apple', 'water melon']

for fruit in list_of_fruits:
    print('The fruit', fruit, 'contains:-')
    if fruit in vitamin_c_fruits:
        print('Vitamin C')
    if fruit in vitamin_k_fruits:
        print('Vitamin K')
    if fruit in iron_fruits:
        print('IRON')

result = calculate_percentage([44, 56, 78])

print(result)
