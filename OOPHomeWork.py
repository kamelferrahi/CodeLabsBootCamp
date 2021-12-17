class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Vehicule:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicule):
    def __init__(self,length,width):
        super().__init__(self,length,width)
