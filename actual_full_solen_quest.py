from System.Collections.Generic import List
from System import Byte

wait_time = 100
ants_dropoff = 0x4099d101
ants_runebook = 0x43FFE2D3
ants_home = 0x43FF743A
trash_bin = 0x4301BD1E

ant_runes = [7, 13, 19, 25, 31, 37, 43, 49, 55]
items_to_store = [0x0EED, 0x26B8, 0xf26, 0xf25, 0xf16, 0xf10, 0xf19, 0xf21, 0xf2d, 0xf13, 0x26B7]

def zoogi_fungus_amount():
    return 0 if Items.FindByID(0x26B7,0x0000,0x41547BC3,0) == None else Items.FindByID(0x26B7,0x0000,0x41547BC3,0).Amount

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

def run_to_queen():
    Items.UseItem(0x40000435)
    Misc.Pause(1000)


    while Player.Position.Y < 1858: # 5921, 1797 -> 5921, 1858
        Player.Run('South')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1878: # 5921, 1858 -> 5901, 1878
        Player.Run('Left')
        Misc.Pause(wait_time)
        
    Items.UseItem(0x40000459)
    Misc.Pause(1000)

    while Player.Position.Y > 1853: # 5874, 1870 -> 5892, 1853
        Player.Run('Right')
        Misc.Pause(wait_time)
        
    while Player.Position.Y > 1819: # 5892, 1853 -> 5858, 1819
        Player.Run('Up')
        Misc.Pause(wait_time)

    while Player.Position.X > 5844: # 5858, 1819 -> 5844, 1819
        Player.Run('West')
        Misc.Pause(wait_time)
        
    while Player.Position.Y > 1797: # 5844, 1819 -> 5822, 1797
        Player.Run('Up')
        Misc.Pause(wait_time)
        
    while Player.Position.X > 5794: # 5822, 1797 -> 5794, 1797
        Player.Run('West')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1813: # 5794, 1797 -> 5794, 1813
        Player.Run('South')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1855: # 5794, 1813 -> 5828, 1855
        Player.Run('Down')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1864: # 5828, 1855 -> 5819, 1864
        Player.Run('Left')
        Misc.Pause(wait_time)
        
    while Player.Position.X > 5801: # 5819, 1864 -> 5801, 1864
        Player.Run('West')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1897: # 5801, 1864 -> 5833, 1897
        Player.Run('Down')
        Misc.Pause(wait_time)
        
    while Player.Position.X < 5846: # 5833, 1897 -> 5846, 1897
        Player.Run('East')
        Misc.Pause(wait_time)
        
    while Player.Position.Y > 1873: # 5846, 1897 -> 5846, 1873
        Player.Run('North')
        Misc.Pause(wait_time)
        
    while Player.Position.X < 5851: # 5846, 1873 -> 5851, 1873
        Player.Run('East')
        Misc.Pause(wait_time)
        
    while Player.Position.Y > 1851: # 5851, 1873 -> 5851, 1851
        Player.Run('North')
        Misc.Pause(wait_time)
        
    Items.UseItem(0x4000046D)
    Misc.Pause(1000)

    while Player.Position.Y < 1902: # 5774, 1870 -> 5807, 1902
        Player.Run('Down')
        Misc.Pause(wait_time)

    while Player.Position.Y < 1914: # 5807, 1902 -> 5807, 1914
        Player.Run('South')
        Misc.Pause(wait_time)
        
    while Player.Position.Y < 1920: # 5807, 1914 -> 5801, 1920
        Player.Run('Left')
        Misc.Pause(wait_time)
        
    while Player.Position.Y > 1897: # 5801, 1920 -> 5778, 1897
        Player.Run('Up')
        Misc.Pause(wait_time)
        
def dump_water():
    while Player.Position.Y < 1922: # 5778, 1897 -> 5803, 1922
        Player.Run('Down')
        Misc.Pause(wait_time)
        
    while Player.Position.X > 5800: # 5803, 1922 -> 5800, 1925
        Player.Run('Left')
        Misc.Pause(wait_time)
        
    for i in range(8):
        pitcher_of_water = FindItem(0x1F9D,Player.Backpack,0x0000)
        if pitcher_of_water is not None:
            Items.UseItem(pitcher_of_water)
            Target.WaitForTarget(10000)
            Target.TargetExecute(0x40016111)
            Misc.Pause(500)
            
    while Player.Position.X < 5803: # 5800, 1925 -> 5803, 1922
        Player.Run('Right')
        Misc.Pause(wait_time)

    while Player.Position.Y > 1897: # 5803, 1922 -> 5778, 1897
        Player.Run('Up')
        Misc.Pause(wait_time)

######### DROP THE QUEST IF YOU ALREADY HAVE IT ############
#Items.UseItem(ants_home)
#Gumps.WaitForGump(1431013363,10000)
#Gumps.SendAction(1431013363,19)
#Misc.Pause(2000)
#   
#run_to_queen()

######### ACCEPT QUEST START ###########
Misc.WaitForContext(0x00029CDC, 10000)
Misc.ContextReply(0x00029CDC, 0)
Gumps.WaitForGump(2460962336, 10000)
Gumps.SendAction(2460962336, 1)
Gumps.WaitForGump(2685952746, 10000)
Gumps.SendAction(2685952746, 1)

#while zoogi_fungus_amount() < 200:
#    for rune in ant_runes:
#        Misc.Pause(250)
#        Journal.Clear()
#        Misc.Pause(250)
#        Items.UseItem(ants_runebook)
#        Gumps.WaitForGump(1431013363,10000)
#        Gumps.SendAction(1431013363,rune)
#        Misc.SendMessage("Rune {0}".format(rune),33)
#        Misc.Pause(2000)
#        
#        victims = mobs_list(10)
#        while len(victims) > 0:
#            nearest = Mobiles.Select(victims, 'Nearest')
#            Player.Attack(nearest)
#            
#            if len(mobs_list(1)) > 1 and Player.Mana >= 10:
#                Player.WeaponPrimarySA()
#            
#            victims = mobs_list(10)
#            Misc.Pause(500)
#            
#        Misc.Pause(5000)
#        
########## ACCEPT WATER QUEST ###########
#Misc.WaitForContext(0x00029CDC, 10000)
#Misc.ContextReply(0x00029CDC, 0)
#Gumps.WaitForGump(2685952746, 10000)
#Gumps.SendAction(2685952746, 1)
#
#if len(Items.FindAllByID(0x1F9D,0x0000,Player.Backpack.Serial, 0, False)) < 8:
#    Items.UseItem(ants_home)
#    Gumps.WaitForGump(1431013363,10000)
#    Gumps.SendAction(1431013363,7)
#    Misc.Pause(2000)
#    Items.UseItem(ants_dropoff)
#    Misc.Pause(1000)
#    Items.UseItem(0x466884f7)
#    Misc.Pause(1000)
#    water_bag = Items.FindBySerial(0x466884f7)
#    
#    for i in range(64):
#        pitcher_of_water = FindItem(0x1F9D,water_bag,0x0000)
#        if pitcher_of_water != None:
#            Items.Move(pitcher_of_water, Player.Backpack, -1)
#            Misc.Pause(700)
#            
#    empty_pitcher = FindItem(0x0FF6, Player.Backpack, 0x0000)
#    while empty_pitcher != None:
#        Items.Move(empty_pitcher, trash_bin, -1)
#        Misc.Pause(700)
#        empty_pitcher = FindItem(0x0FF6, Player.Backpack, 0x0000)
#        
#    for item in items_to_store:
#        item_to_store = FindItem(item, Player.Backpack, 0x0000)
#        if item_to_store != None:
#            Items.Move(item_to_store, ants_dropoff, -1)
#            Misc.Pause(700)
#        
#    Items.UseItem(ants_home)
#    Gumps.WaitForGump(1431013363,10000)
#    Gumps.SendAction(1431013363,19)
#    Misc.Pause(2000)
#    run_to_queen()
#    dump_water()
#    
#    ######### HAND IN WATER QUEST #########
#    Misc.WaitForContext(0x00029CDC, 10000)
#    Misc.ContextReply(0x00029CDC, 0)
#    Gumps.WaitForGump(2685952746, 10000)
#    Gumps.SendAction(2685952746, 1)
#    Misc.Pause(500)
#
#    ######### PROCESS ZOOGI FUNGUS ########
#    zoogi_fungus = FindItem(0x26B7, Player.Backpack, 0x0000)
#    Misc.WaitForContext(0x00029CDC, 10000)
#    Misc.ContextReply(0x00029CDC, 1)
#    Target.WaitForTarget(10000, False)
#    Target.TargetExecute(zoogi_fungus.Serial)
#    Misc.Pause(500)
            



