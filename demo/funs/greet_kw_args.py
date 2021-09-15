def greet(name, msg):
    print(msg, name)


greet("Van Rossum", "Hi")  # Positional parameters
greet(msg="Hello", name="Andy")  # keyword parameters
greet("Richards", msg="Hello")   # Mixed
