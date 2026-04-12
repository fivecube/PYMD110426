# continue:- SKIPPING THE REST OF THE LINES

age = 5

while age < 18:
    age += 1  # counter = counter + 1
    print('You are not allowed to use phone because you are ', age, ' Years old')
    if age <= 10:
        continue
    marks = int(input('Give me your annual %'))
    if marks > 95:
        break


print('The while loop is over!')
print('You are ', age, ' years old! and you are allowed to use phone!')
