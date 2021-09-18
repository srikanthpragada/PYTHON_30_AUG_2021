# Pass an immutable object by reference
def increment(v):
    print(id(v))
    v += 1
    print(id(v))
    print(v)


a = 100
print(id(a))
increment(a)
print(a)

