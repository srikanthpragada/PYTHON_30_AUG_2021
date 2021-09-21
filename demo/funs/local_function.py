g = 100  # Global variable


def outer():
    global g
    g = 0
    a = 10  # Enclosing variable

    # Local function
    def inner():
        b = 20  # Local variable
        nonlocal a
        a = 1000
        print("Inner", a, b)

    inner()
    print("Outer", a)

    return inner


outer()
