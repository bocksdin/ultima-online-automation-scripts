ants_dropoff = 0x4099d101
ants_runebook = 0x43FFE2D3
ants_home = 0x43FF743A

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
            
if len(Items.FindAllByID(0x1F9D,0x0000,Player.Backpack.Serial, 0, False)) < 8:
    Items.UseItem(ants_home)
    Gumps.WaitForGump(1431013363,10000)
    Gumps.SendAction(1431013363,7)
    Misc.Pause(5000)
    Items.UseItem(ants_dropoff)
    Misc.Pause(1000)
    Items.UseItem(0x466884f7)
    Misc.Pause(1000)
    water_bag = Items.FindBySerial(0x466884f7)
    for i in range(8):
        pitcher_of_water = FindItem(0x1F9D,water_bag,0x0000)
        if pitcher_of_water != None:
            Items.Move(pitcher_of_water, Player.Backpack, -1)
            Misc.Pause(700)
        
#Items.UseItem(0x43FFE2D3)
#Gumps.WaitForGump(1431013363, 10000)
#Gumps.SendAction(1431013363, 7)