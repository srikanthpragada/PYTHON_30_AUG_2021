def f1():
    print("Function f1")


def next_even(n):
    if n % 2 == 0:
        n += 2
    else:
        n += 1

    return n


def next_even2(n):
    if n % 2 == 0:
        return n + 2
    else:
        return n + 1


def next_even3(n):
    return n + 2 if n % 2 == 0 else n + 1


v = f1()
print(v)

print( next_even(10), next_even(21))

