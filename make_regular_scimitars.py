####### CHANGE THESE
good_dropoff = 0x43C95D69
trash_barrel = 0x42E271B3
extra_tools_container = 0x4616BA7B
ash_container = 0x44297976
resource_container = 0x43A71A8B
resource_ItemID = 0x1BF2
resource_Color = 0x0966

tool_ItemID = 0x13E3
tool_Color = 0x0972
item_to_craft_ItemID = 0x2D33

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
    [Attribute('slayer'), Attribute('mana leech'), Attribute('swing speed')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('lower attack')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('lower defense')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('lower attack')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('lower defense')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('mana leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('swing speed')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('life leech'), Attribute('stamina leech'), Attribute('area')],
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
    Player.HeadMessage(33,'CHECKING ITEM')
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
                Player.HeadMessage(33,'SAVING')
                Items.Move(item, good_dropoff, 1)
                Misc.Pause(1000)
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
                
    resource = Items.FindByID(resource_ItemID,resource_Color,Player.Backpack.Serial,0,0)
    if resource is None or resource.Amount < 15:
        Player.HeadMessage(33,'GRABBING RESOURCES')
        Items.Move(Items.FindByID(resource_ItemID,resource_Color,resource_container,0,0),Player.Backpack.Serial,500)
        Misc.Pause(525)
    
        
    Player.HeadMessage(33,'CRAFTING')
    #### CRAFT ITEM
    Items.UseItem(tool)
    Gumps.WaitForGump(949095101, 5000)
    Gumps.SendAction(949095101, 36)
    Gumps.WaitForGump(949095101, 5000)
    Gumps.SendAction(949095101, 128)
    Misc.Pause(2000)
    
    item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
    while item is not None and Items.FindBySerial(tool.Serial) is not None:
        check_item(item, tool)
        Misc.Pause(500)
        item = Items.FindByID(item_to_craft_ItemID,-1,Player.Backpack.Serial,0,0)
        
    tool = grab_new_tool()
    Misc.Pause(100)
