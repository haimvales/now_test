
from soldier import Soldier
from strikeOption import StrikeOption
# from unit import Unit
#מחלקת יחידה מקבל סוג יחידה ולוחם ורשימת לוחמים 
class Unit:
    """
    מחלקת יחידה מקבל סוג יחידה ומפקד ורשימת לוחמים 
    """
    def __init__(self,unit_name:str,commander:Soldier,soldiers:list[Soldier],strike:StrikeOption):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike = strike




    def briefing(self):
        """
        פונקציה שמדפיסה יחידה ודו"ח המפקד
        """
        print(self.unit_name,self.commander)

