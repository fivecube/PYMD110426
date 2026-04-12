# break:-

# ask for marks in while loop, if the marks are below 33, we will break the loop.

counter = 0

while counter < 18:
    counter += 1  # counter = counter + 1
    print('You are not allowed to use phone because you are ', counter, ' Years old')
    marks = int(input('Give me your annual %'))
    if marks > 95:
        break


print('The while loop is over!')
print('You are ', counter, ' years old! and you are allowed to use phone!')
