print("str_funs  ver. 1.0")

def has_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def has_lower(st):
    for c in st:
        if c.islower():
            return True

    return False


