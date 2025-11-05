
# from weapon import Weapon
#מחלקת לוחם מקבלת שם דרגה ומופע של נשק
# import weapon
class Soldier:
    def __init__(self,name:str,rank:str,weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    
    def __repr__(self):
        return f"neme_Soldier= {self.name}, rank_Soldier= {self.rank}, {self.weapon}"
    
    def  report(self):
        print(self)
        




