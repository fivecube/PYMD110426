def calculate_happiness(list_of_emotions):
    return 100


# students = [("A", 90), ("B", 67), ("C", 78), ("D", 92)]
#
# for x in students:
#     print(x[1])

students = [("A", "Singh", 90), ("B", "Khanna", 67), ("C", "Chouhan", 78), ("D", "Patil", 92)]

for x in students:
    print(x[2])

sorted_result = sorted(students, key=lambda x: x[2], reverse=True)

print(f"sorted result = {sorted_result}")
