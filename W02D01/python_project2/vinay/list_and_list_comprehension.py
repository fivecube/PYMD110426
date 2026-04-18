# list

# collection of items which are ordered
# mutable collection:- edit items inside the list
# indexing
# slicing

list_of_fruits = ['apple', 'mango', 'banana', 'orange']

print(list_of_fruits[0])

print(list_of_fruits[-1])

print(list_of_fruits[-2])

# List Index out of Range Error:- This happens when you try to access an index which is not there

print(list_of_fruits[-4])

for i in range(-1, -len(list_of_fruits) - 1, -1):
    print(i)

