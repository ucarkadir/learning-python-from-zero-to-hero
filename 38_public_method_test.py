class Person:
    def __init__ (self, first_name, age):
        self.first_name = first_name
        self._age = age
    
    def show_age(self):
        return self._age
    
tk = Person('Tk',25)
print(tk.show_age()) # => 25