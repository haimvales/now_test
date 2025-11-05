
from abc import ABC,abstractmethod


class StrikeOption(ABC):
    def __init__(self,name:str,ammo:int):
        self.name = name
        self.ammo = ammo

    @abstractmethod
    def strike(self):
        pass
        
    

class Tank(StrikeOption):
    def strike(self):
        print("this is from tank")

class Drone(StrikeOption):
    def strike(self):
        print("this is from drone")



    



