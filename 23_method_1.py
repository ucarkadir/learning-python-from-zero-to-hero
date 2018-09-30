class Vehicle:
    def __init__(self, number_of_wheels, type_of_tant, seating_capacitiy, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tant = type_of_tant
        self.seating_capacitiy = seating_capacitiy
        self.maximum_velocity = maximum_velocity

    def number_of_whees(self):
        return self.number_of_wheels
    
    def set_number_of_wheels(self, number):
        self.number_of_wheels = number
