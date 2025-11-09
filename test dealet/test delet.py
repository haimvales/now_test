class Student:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name 
    
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def start(self):
        return f"{self.brand} {self.model} engine started!"
    
class Cars(Vehicle):
    def __init__(self, brand, model,doors):
        super().__init__(brand, model)
        self.doors = doors
    def start(self):
        return f"{super().start()} {self.doors} doors"

        
car = Cars("toyota",2025,4)
print(car.start())

