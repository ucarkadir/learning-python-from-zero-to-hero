class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

tk = Person('kadir','ucarkadir@outlook.com')
print(tk._email)