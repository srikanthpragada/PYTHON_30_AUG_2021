def total_length(*values):
    total = 0
    for n in values:
        total += len(n)

    return total


print( total_length("Abc","Xy","Pqrs"))


