
class Agent:
    def __init__(self,codename:str,clearance_level:int):
        self.codename = codename
        self.clearance_level = clearance_level


class Mission:
    def __init__(self,mission_name:str,target:str,assigned_agent:Agent):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
    def __repr__(self):
        return f"mission_name = {self.mission_name} target = {self.target} codename = {self.assigned_agent.codename}"
    def  briefing(self):
          print(self)