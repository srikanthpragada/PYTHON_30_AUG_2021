def numbers():
    for n in range(10):
        yield n

g = numbers()
print(type(g))
print(next(g))
print(next(g))

# for n in g:
#     print(n)
