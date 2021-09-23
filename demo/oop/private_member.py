class Person:
    def __init__(self, name, email):
        self.name = name
        # Private member
        self.__email = email

    def get_email(self):
        return self.__email


p1 = Person("Andy", "andy@gmail.com")
print(p1.get_email())
print(p1.__dict__)
print(p1._Person__email)   # Can do, but should not do it
