# Parameters and return values
# Lambda functions
# Scope and namespaces


def calculate_happiness_2(param1, param2=90, param3=100):
    return param1 + param2 + param3


result = calculate_happiness_2(4, 5, 7)

print(result)

# default parameters(argument)

result2 = calculate_happiness_2(10)

print(result2)


def calculate_happiness_3(param1, param2=90, param3=100):
    return param1 + param2, param1 + param3


return1, return2 = calculate_happiness_3(10)
# tuple unpacking. So the function returned a tuple with 2 values and since
# we created 2 variables in front of the call of the function. It understood that it can
# unpack these 2 tuple values into these 2 variables.

print(f"return1={return1}, return2={return2}")
# String formatting. If you use f infront of a string, it becomes a formatted string.
# It has the power to directly add the variable values inside it by curly brackets {}


combined_result = calculate_happiness_3(10)

print("combined_result", type(combined_result))
print(combined_result)
print(combined_result[0])
print(combined_result[1])

# Lambda functions

# 1 line functions
# nameless functions
# lambda input: output

students = [("A", 90), ("B", 67), ("C", 78), ("D", 92)]

# D, A, C, B
# SORT BASED ON EVERY ITEM'S 1ST INDEX OR(2ND POSITION)
sorted_result1 = sorted(students)

print(f"sorted result 1 = {sorted_result1}")

sorted_result2 = sorted(students, key=lambda x: x[1], reverse=True)

print(f"sorted result 2 = {sorted_result2}")


def give_me_correct_key(x):
    # This function was used only for the following sorted call, It's useless now as we don't need it.
    return x[1]


sorted_result3 = sorted(students, key=give_me_correct_key, reverse=True)

print(f"sorted result 3 = {sorted_result3}")
