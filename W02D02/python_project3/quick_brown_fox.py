string1 = 'cdefghijkamnobpqrstuvwxyz'

something_missing = False

for i in range(ord('a'), ord('z') + 1):
    alpha = chr(i)
    alpha_found = False
    for char in string1:
        if alpha == char:
            alpha_found = True
            break
    if not alpha_found:
        something_missing = True
        break
print('Any Alphabet missing:- ', something_missing)
