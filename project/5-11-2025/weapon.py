
# from soldier import Soldier

# import soldier
#מחלקת נשק מקבלת שם וכמות יריות וכל פעם מוסיפה עוד כלי נשק
class Weapon:
    total_weapons = 0
    def __init__(self,name:str,ammo:int):
        self.name= name
        self.ammo = ammo
        Weapon.total_weapons += 1
    def __repr__(self):
        return f"neme_Weapon= {self.name}, ammo_Weapon= {self.ammo}"
    

        