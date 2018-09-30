class Car:
    def __init__ (self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

class ElectricCar(Car):
    def __init__ (self, number_of_wheels, seating_capacity, maximum_velocity):
       Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

my_electric_car = ElectricCar(4,5,250)

print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250

'''
Copy a folder including all subfolders. 
#XCOPY C:\utils\* D:\Backcup\utils /s /i 
"It is easier to copy than to think, hence fashion"  ~Wallace Steens 

I like it.
'''