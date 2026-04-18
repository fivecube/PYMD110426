# Variable visibility


x = 10


# global namespace/frame

def func():
    x = 5
    print("first x", x)  # local x

    # local namespace/frame

    def next_func():
        x = 20
        print('third x', x)

    next_func()


func()

print("second x", x)  # global x
