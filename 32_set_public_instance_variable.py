class Person:
    def __init__(self, first_name):
        self.first_name = first_name

tk = Person('Tk')
print(tk.first_name)

tk.first_name = 'Kaio'
print(tk.first_name)