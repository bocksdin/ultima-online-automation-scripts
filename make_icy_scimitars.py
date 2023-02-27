####### CHANGE THESE
good_dropoff = 0x43C95D69
trash_barrel = 0x42E271B3
extra_tools_container = 0x4616BA7B
ash_container = 0x44297976
resource_container = 0x43A71A8B
resource_ItemID = 0x1BF2
resource_Color = 0x08ab

tool_ItemID = 0x13E3
tool_Color = 0x0972
item_to_craft_ItemID = 0x2D33

####### ADD MORE SLAYERS YOU WOULD LIKE TO FILTER OUT
bad_slayers = ['spider slayer', 'terathan slayer', 
               'ophidian slayer', 'poison elemental slayer', 
               'water elemental slayer', 'lizardman slayer', 
               'orc slayer', 'air elemental slayer', 
               'gargoyle slayer', 'earth elemental slayer', 
               'snow elemental slayer', 'fire elemental slayer', 
               'scorpion slayer', 'troll slayer', 
               'ogre slayer', 'snake slayer']


class Attribute:
    name = None
    value = None
    
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

####### ADD MORE COMBINATIONS OF STATS
####### COMMA SEPARATED AND GROUPED BY [] SQUARE BRACKETS        
good_stats = [
    [Attribute('slayer'), Attribute('mana leech'), Attribute('swing speed')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('mana leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('swing speed')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('lightning')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('harm', 15.1)],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('fireball')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('magic arrow')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('lightning')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('harm', 15.1)],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('fireball')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('magic arrow')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('life leech'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('life leech'), Attribute('mana leech'), Attribute('area')],
    [Attribute('mana leech'), Attribute('swing speed'), Attribute('area')],
    [Attribute('stamina leech'), Attribute('swing speed'), Attribute('area')],
    [Attribute('area'), Attribute('mana leech'), Attribute('lightning')],
    [Attribute('area'), Attribute('mana leech'), Attribute('harm', 15.1)],
    [Attribute('area'), Attribute('mana leech'), Attribute('fireball')],
    [Attribute('area'), Attribute('mana leech'), Attribute('magic arrow')],
    [Attribute('area'), Attribute('stamina leech'), Attribute('lightning')],
    [Attribute('area'), Attribute('stamina leech'), Attribute('harm', 15.1)],
    [Attribute('area'), Attribute('stamina leech'), Attribute('fireball')],
    [Attribute('area'), Attribute('stamina leech'), Attribute('magic arrow')],
    [Attribute('swing speed'), Attribute('mana leech'), Attribute('lightning')],
    [Attribute('swing speed'), Attribute('mana leech'), Attribute('harm', 15.1)],
    [Attribute('swing speed'), Attribute('mana leech'), Attribute('fireball')],
    [Attribute('swing speed'), Attribute('mana leech'), Attribute('magic arrow')],
    [Attribute('swing speed'), Attribute('stamina leech'), Attribute('lightning')],
    [Attribute('swing speed'), Attribute('stamina leech'), Attribute('harm', 15.1)],
    [Attribute('swing speed'), Attribute('stamina leech'), Attribute('fireball')],
    [Attribute('swing speed'), Attribute('stamina leech'), Attribute('magic arrow')],
    [Attribute('stamina leech'), Attribute('mana leech'), Attribute('lightning')],
    [Attribute('stamina leech'), Attribute('mana leech'), Attribute('harm', 15.1)],
    [Attribute('stamina leech'), Attribute('mana leech'), Attribute('fireball')],
    [Attribute('stamina leech'), Attribute('mana leech'), Attribute('magic arrow')],
    [Attribute('stamina leech'), Attribute('life leech'), Attribute('lightning')],
    [Attribute('stamina leech'), Attribute('life leech'), Attribute('harm', 15.1)],
    [Attribute('stamina leech'), Attribute('life leech'), Attribute('fireball')],
    [Attribute('stamina leech'), Attribute('life leech'), Attribute('magic arrow')],
    [Attribute('mana leech'), Attribute('life leech'), Attribute('lightning')],
    [Attribute('mana leech'), Attribute('life leech'), Attribute('harm, 15.1')],
    [Attribute('mana leech'), Attribute('life leech'), Attribute('fireball')],
    [Attribute('mana leech'), Attribute('life leech'), Attribute('magic arrow')],
]


####### DO NOT CHANGE ANYTHING BELOW HERE
def grab_new_tool():
    tool = Items.FindByID(tool_ItemID,tool_Color,Player.Backpack.Serial,0,0)
    while Items.FindByID(tool_ItemID,tool_Color,Player.Backpack.Serial,0,0) is None:
        tool = Items.FindByID(tool_ItemID,tool_Color,extra_tools_container,0,0)
        Items.Move(tool,Player.Backpack.Serial,1)
        Misc.Pause(525)
        
    return tool

def check_item(item, tool):
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
            Player.HeadMessage(33,'DESTROYING')
            if Target.HasTarget():
                Target.TargetExecute(Player.Serial)
            if not Gumps.HasGump():
                Items.UseItem(tool)
            Gumps.WaitForGump(949095101, 5000)
            Gumps.SendAction(949095101, 14)
            Target.WaitForTarget(5000)
            Target.TargetExecute(item.Serial)
            Misc.Pause(1000)

Misc.Pause(5000)
tool = grab_new_tool()
while tool is not None and Items.FindBySerial(tool.Serial) is not None:
    Player.HeadMessage(33,'HAS TOOL')
    if not Player.CheckLayer('RightHand'):
        Player.HeadMessage(33,'GRABBING ASH')
        ash = Items.FindByID(0x13E4,0x0482,Player.Backpack.Serial,0,0)
        if ash is not None:
            Player.EquipItem(ash)
            Misc.Pause(1000)
        else:
            ash = Items.FindByID(0x13E4,0x0482,ash_container,0,0)
            if ash is not None:
                Player.EquipItem(ash)
                Misc.Pause(1000)
            else:
                break
        
    dark_sapphire = Items.FindByID(0x3192,0x0000,Player.Backpack.Serial,0,0)
    if dark_sapphire is None or dark_sapphire.Amount < 1:
        Player.HeadMessage(33,'GRABBING GEMS')
        Items.Move(Items.FindByID(0x3192,0x0000,resource_container,0,0),Player.Backpack.Serial,100)
        Misc.Pause(1000)

    resource = Items.FindByID(resource_ItemID,resource_Color,Player.Backpack.Serial,0,0)
    if resource is None or resource.Amount < 15:
        Player.HeadMessage(33,'GRABBING INGOTS')
        Items.Move(Items.FindByID(resource_ItemID,resource_Color,resource_container,0,0),Player.Backpack.Serial,500)
        Misc.Pause(525)
    
    #### CRAFT ITEM
    Player.HeadMessage(33,'CRAFTING')
    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 36)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 387)
    Misc.Pause(2000)
    
    item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
    while item is not None and Items.FindBySerial(tool.Serial) is not None:
        check_item(item, tool)
        Misc.Pause(500)
        item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
        
    tool = grab_new_tool()
    Misc.Pause(100)