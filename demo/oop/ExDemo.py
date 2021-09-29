
st = "Abc"
try:
    n = int(st)
    print(n * n)
except KeyError as ex:
    print("Error -->", ex)

print("The End")


