# Pass an immutable object by reference
def increment(v):
    print(id(v))
    v += 1
    print(id(v))
    print(v)


def prepend(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
increment(a)
print(a)

l = [1, 2, 3]
prepend(l, 10)
print(l)
