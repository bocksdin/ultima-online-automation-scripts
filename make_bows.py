####### CHANGE THESE
good_dropoff = 0
trash_barrel = 0
extra_kits_container = 0
wood_container = 0

kit_ItemID = 0x1022
kit_Color = 0x0000
yumi_ItemID = 0
magical_shortbow_ItemID = 

####### ADD MORE SLAYERS YOU WOULD LIKE TO FILTER OUT
bad_slayers = ['spider slayer', 'terathan slayer', 
               'ophidian slayer', 'poison elemental slayer', 
               'blood elemental slayer', 'water elemental slayer', 
               'lizardman slayer', 'orc slayer', 
               'air elemental slayer', 'gargoyle slayer', 
               'earth elemental slayer', 'snow elemental slayer', 
               'fire elemental slayer', 'scorpion slayer', 
               'troll slayer', 'ogre slayer', 'snake slayer']


class Attribute:
    name = None
    value = None
    
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

####### ADD MORE COMBINATIONS OF STATS
####### COMMA SEPARATED AND GROUPED BY [] SQUARE BRACKETS        
good_stats = [
    [Attribute('slayer'), Attribute('mana leech')],
    [Attribute('slayer'), Attribute('stamina leech')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('life leech')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('swing speed')],
]


####### DO NOT CHANGE ANYTHING BELOW HERE
def grab_new_kit():
    kit = Items.FindByID(kit_ItemID,kit_Color,Player.Backpack.Serial,0,0)
    if kit is None:
        kit = Items.FindByID(kit_ItemID,kit_Color,extra_kits_container,0,0)
        Items.Move(kit,Player.Backpack.Serial,1)
        Misc.Pause(1000)

def check_item(item):
    if item is not None:
        saved = False
        item_attributes = Items.GetPropStringList(item)
        for combo in good_stats:
            score = 0
            for attribute in combo:
                for attr in item_attributes:
                    if attr.find(attribute.name) > -1 and attr not in bad_slayers:
                        if attribute.value is None:
                            score += 1
                            break
                        elif Items.GetPropValue(item,attr) >= attribute.value:
                            score += 1
                            break
                            
            if score >= len(combo):
                Items.Move(item, good_dropoff, 1)
                Misc.Pause(1000)
                saved = True
                break
                
        if saved == False:
            Items.Move(item, trash_barrel, 1)
            Misc.Pause(1000)

grab_new_kit()
    
while kit is not None:
    boards = Items.FindByID(boards_ItemID,boards_Color,Player.Backpack.Serial,0,0)
    if boards is None or boards.Amount < 15:
        Items.Move(Items.FindByID(boards_ItemID,boards_Color,boards_container,0,0),Player.Backpack.Serial,500)
        Misc.Pause(1000)
    
    #### CRAFT YUMI
    Items.UseItem(kit)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 15)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 37)
    Misc.Pause(2000)
    yumi = Items.FindByID(yumi_ItemID,-1,Player.Backpack.Serial,0,0)
    check_item(yumi)
        
    #### CRAFT MAGICAL SHORTBOW
    Items.UseItem(kit)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 15)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 51)
    Misc.Pause(2000)
    magical_shortbow = Items.FindByID(magical_shortbow_ItemID,-1,Player.Backpack.Serial,0,0)
    check_item(magical_shortbow)
        
    grab_new_kit()
    Misc.Pause(100)
