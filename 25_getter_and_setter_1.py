class Vehicle:
    def __init__(self, number_of_wheels, type_of_tant, seating_capacitiy, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tant = type_of_tant
        self.seating_capacitiy = seating_capacitiy
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self.number_of_wheels
    
    @number_of_wheels.setter
    def set_number_of_wheels(self, number):
        self.number_of_wheels = number

tesla_model_s = Vehicle(4,'electric', 5, 250)
print(tesla_model_s.number_of_wheels) # 4 
tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
print(tesla_model_s.number_of_wheels) # 2


# this is my code
if tesla_model_s.number_of_wheels == 2:
    print("This is not posible %s" %(tesla_model_s.number_of_wheels))
