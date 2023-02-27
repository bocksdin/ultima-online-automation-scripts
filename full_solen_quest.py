from System.Collections.Generic import List
from System import Byte

ants_dropoff = 0x4099d101
ants_runebook = 0x4401C924
ants_home = 0x43FF743A

ant_runes = [7, 13, 19, 25, 31, 37, 43, 49, 55]
items_to_store = [0x0EED, 0x26B8, 0xf26, 0xf25, 0xf16, 0xf10, 0xf19, 0xf21, 0xf2d, 0xf13, 0x26B7]
weapon_type = 0x2D33

def mobs_list(range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
    
def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem

Misc.Pause(2000)
while 1==1:
    for rune in ant_runes:
        Misc.Pause(250)
        Journal.Clear()
        Misc.Pause(250)
        Items.UseItem(ants_runebook)
        Gumps.WaitForGump(1431013363,10000)
        Gumps.SendAction(1431013363,rune)
        Misc.SendMessage("Rune {0}".format(rune),33)
        Misc.Pause(2000)
        
        victims = mobs_list(10)
        while len(victims) > 0:
            nearest = Mobiles.Select(victims, 'Nearest')
            Player.Attack(nearest)
            
            if len(mobs_list(1)) > 1 and Player.Mana >= 10:
                Player.WeaponPrimarySA()
            
            victims = mobs_list(10)
            Misc.Pause(500)
            
        weapon = Player.GetItemOnLayer('RightHand')
        if weapon is None or Items.GetPropValue(weapon,'durability') <= 0.0:
            extra_weapon = Items.FindByID(weapon_type,-1,Player.Backpack.Serial,0,0)
            if extra_weapon is not None and (Items.GetPropValue(extra_weapon,'durability') > 0.0 or Player.CheckLayer('RightHand') == False):
                Player.UnEquipItemByLayer('RightHand',5000)
                Misc.Pause(1000)
                Player.EquipItem(extra_weapon)
        Misc.Pause(5000)
        
        if Player.Weight >= Player.MaxWeight * 0.5:
            Items.UseItem(ants_home)
            Gumps.WaitForGump(1431013363,10000)
            Gumps.SendAction(1431013363,7)
            Misc.Pause(5000)
            
            for item in items_to_store:
                item_to_store = FindItem(item, Player.Backpack, 0x0000)
                if item_to_store != None:
                    Items.Move(item_to_store, ants_dropoff, -1)
                    Misc.Pause(700)