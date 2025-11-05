
from weapon import Weapon
from soldier import Soldier
from unit import Unit
from strikeOption import StrikeOption, Tank
from agent import Agent,Mission



w = Weapon("zuzu",20)
s = Soldier("momo","a",w)
s_list = [s]
# s.report()
tank = Tank("tank1",200)
u = Unit("kodkod",s,s_list,tank)
# u.briefing()

w2 =    Weapon("yoyo",30)
s2 = Soldier("yuyu","b",w2)
s_list2 = [s2]
# s2.report()
tank2 = Tank("tank2",300)
u2 = Unit("kodkod",s2,s_list2,tank2)
# u2.briefing()

for i in [tank,tank2]:
    i.strike()

a = Agent("2468",3)
m = Mission("abcdef","sydg",a)
m.briefing()





