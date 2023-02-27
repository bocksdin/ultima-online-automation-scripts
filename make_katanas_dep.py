good_dropoff = 0x43C95D69
trash_barrel = 0x42E271B3
extra_hammers = 0x44297976

ingots_container = 0x43A71A8B

hammer_ItemID = 0x13E3
hammer_Color = 0x0972
ingots_ItemID = 0x1BF2
ingots_Color = 0x096d

bad_slayers = ['spider slayer', 'terathan slayer', 'ophidian slayer', 'poison elemental slayer', 'water elemental slayer', 'lizardman slayer', 'orc slayer', 'air elemental slayer', 'gargoyle slayer', 'earth elemental slayer', 'snow elemental slayer', 'fire elemental slayer', 'scorpion slayer', 'troll slayer', 'ogre slayer', 'snake slayer']


class Attribute:
    name = None
    value = None
    
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        
good_stats = [
    [Attribute('slayer'), Attribute('mana leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('lower attack')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('lower defense')],
    [Attribute('slayer'), Attribute('mana leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('area')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('lower attack')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('lower defense')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('life leech')],
    [Attribute('slayer'), Attribute('stamina leech'), Attribute('mana leech')],
    [Attribute('mana leech'), Attribute('slayer'), Attribute('hit lightning')],
    [Attribute('mana leech'), Attribute('slayer'), Attribute('hit harm')],
    [Attribute('mana leech'), Attribute('slayer'), Attribute('hit fireball')],
    [Attribute('mana leech'), Attribute('slayer'), Attribute('hit magic arrow')],
    [Attribute('stamina leech'), Attribute('slayer'), Attribute('hit lightning')],
    [Attribute('stamina leech'), Attribute('slayer'), Attribute('hit harm')],
    [Attribute('stamina leech'), Attribute('slayer'), Attribute('hit fireball')],
    [Attribute('stamina leech'), Attribute('slayer'), Attribute('hit magic arrow')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('life leech')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('hit lightning')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('hit harm')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('hit fireball')],
    [Attribute('mana leech'), Attribute('stamina leech'), Attribute('hit magic arrow')],
    [Attribute('mana leech', 40.0), Attribute('stamina leech', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit lightning', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit harm', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit fireball', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit magic arrow', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('life leech', 40.0), Attribute('hit lower attack', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('stamina leech', 40.0), Attribute('hit lower defense', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit lightning', 40.0), Attribute('hit lower defense', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit harm', 40.0), Attribute('hit lower defense', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit fireball', 40.0), Attribute('hit lower defense', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('hit magic arrow', 40.0), Attribute('hit lower defense', 40.0)],
    [Attribute('mana leech', 40.0), Attribute('life leech', 40.0), Attribute('hit lower defense', 40.0)],
]

hammer = Items.FindByID(hammer_ItemID,hammer_Color,Player.Backpack.Serial,0,0)
if hammer is None:
    hammer = Items.FindByID(hammer_ItemID,hammer_Color,extra_hammers,0,0)
    Items.Move(hammer,Player.Backpack.Serial,1)
    Misc.Pause(525)
    
while hammer is not None:
    ingots = Items.FindByID(ingots_ItemID,ingots_Color,Player.Backpack.Serial,0,0)
    if ingots is None or ingots.Amount < 15:
        Items.Move(Items.FindByID(ingots_ItemID,ingots_Color,ingots_container,0,0),Player.Backpack.Serial,500)
        Misc.Pause(525)
    
    Items.UseItem(hammer)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 36)
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 37)
    Misc.Pause(2000)
    
    katana = Items.FindByID(0x13FF,-1,Player.Backpack.Serial,0,0)
    while katana is not None:
        saved = False
        item_attributes = Items.GetPropStringList(katana)
        for combo in good_stats:
            score = 0
            for attribute in combo:
                for attr in item_attributes:
                    if attr.find(attribute.name) > -1 and attr not in bad_slayers:
                        if attribute.value is None:
                            score += 1
                            break
                        elif Items.GetPropValue(katana,attr) >= attribute.value:
                            score += 1
                            break
                            
            if score >= len(combo):
                Items.Move(katana, good_dropoff, 1)
                Misc.Pause(525)
                saved = True
                break
                
        if saved == False:
            Items.Move(katana, trash_barrel, 1)
            Misc.Pause(525)
            
        katana = Items.FindByID(0x13FF,-1,Player.Backpack.Serial,0,0)
        
        
    hammer = Items.FindByID(hammer_ItemID,hammer_Color,Player.Backpack.Serial,0,0)
    if hammer is None:
        hammer = Items.FindByID(hammer_ItemID,hammer_Color,extra_hammers,0,0)
        Items.Move(hammer,Player.Backpack.Serial,1)
        Misc.Pause(525)
    
    Misc.Pause(100)