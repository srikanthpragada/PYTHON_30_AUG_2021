# Positional-only arguments
def greet(name="Guest", msg="Hello", /):
    print(msg, name)


greet("Abc", "Hello")
# greet(msg="Hello", name="Andy")
