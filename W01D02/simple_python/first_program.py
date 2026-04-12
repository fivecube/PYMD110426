# x = True
# count = 0
# while x:
#     count = count + 1
#     print('Hi', count)
#     if count == 817078:
#         break

counter = 0

while counter < 18:
    counter += 1  # counter = counter + 1
    print('I am not allowed to drink alcohol because I am ', counter, ' Years old')


print('The while loop is over!')
print('I am ', counter, ' years old!')


def calculate_percentage(list_of_marks):
    number_of_subjects = len(list_of_marks)
    total_marks = sum(list_of_marks)
    percentage = total_marks/number_of_subjects
    return percentage


result = calculate_percentage([44, 56, 78])

print(result)
