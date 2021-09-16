# Keyword-only arguments
def greet(*, name = "Guest", msg="Hello"):
    print(msg, name)


#greet("Abc")
greet(msg="Hello", name="Andy")  # keyword parameters
greet(name="Scott")
