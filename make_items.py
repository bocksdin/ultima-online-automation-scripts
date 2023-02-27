####### CHANGE THESE
good_dropoff = 0
trash_barrel = 0
extra_tools_container = 0
resource_container = 0
resource_ItemID = 0
resource_Color = 0

tool_ItemID = 0x1028
tool_Color = 0x04a8
item_to_craft_ItemID = 0

use_ash = True

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
def grab_new_tool():
    tool = Items.FindByID(tool_ItemID,tool_Color,Player.Backpack.Serial,0,0)
    if tool is None:
        tool = Items.FindByID(tool_ItemID,tool_Color,extra_tools_container,0,0)
        Items.Move(tool,Player.Backpack.Serial,1)
        Misc.Pause(525)
        
    return tool

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
                Misc.Pause(525)
                saved = True
                break
                
        if saved == False:
            Items.Move(item, trash_barrel, 1)
            Misc.Pause(525)

def equip_ash():
    if not Player.CheckLayer('RightHand'):
        ash = Items.FindByID(0x13E4,0x0482,Player.Backpack.Serial,0,0)
        if ash is not None:
            Player.EquipItem(ash)
            Misc.Pause(1000)
        else:
            ash = Items.FindByID(0x13E4,0x0482,extra_tools_container,0,0)
            if ash is not None:
                Player.EquipItem(ash)
                Misc.Pause(1000)
            else:
                break

tool = grab_new_tool()
    
while tool is not None:
    if use_ash:
      equip_ash()

    resource = Items.FindByID(resource_ItemID,resource_Color,Player.Backpack.Serial,0,0)
    if resource is None or resource.Amount < 15:
        Items.Move(Items.FindByID(resource_ItemID,resource_Color,resource_container,0,0),Player.Backpack.Serial,250)
        Misc.Pause(525)
    
    #### CRAFT ITEM
    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 22)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 9)
    Misc.Pause(2000)
    item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
    while item is not None:
        check_item(item)
        item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
        
    tool = grab_new_tool()
    Misc.Pause(100)
