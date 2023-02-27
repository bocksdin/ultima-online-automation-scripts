from System.Collections.Generic import List
from System import Byte

def mobs_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
    
victims = mobs_list(10)

while len(victims) > 0:
    nearest = Mobiles.Select(victims, 'Nearest')
    Player.Attack(nearest)
    
    victims = mobs_list(10)
    Misc.Pause(1000)
    
Misc.SendMessage("Fighting Complete")