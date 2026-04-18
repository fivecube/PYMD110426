# Variable visibility


x = 10


# global namespace/frame

def func():
    global x
    x = 2000
    print("inside func x", x)  # global x

    # local namespace/frame

    def next_func():
        x = 999
        print('inside next_func x', x)

    next_func()


print("before calling func x", x)

func()

print("after calling func x", x)  # global x


