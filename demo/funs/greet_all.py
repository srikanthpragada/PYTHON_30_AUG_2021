def greet(*names, msg="Hi"):
    for n in names:
        print(msg, n)


greet("Van Rossum", "Mark", "Andy")
greet("Larry", "Elon", msg="Hello")
greet("Scott")
