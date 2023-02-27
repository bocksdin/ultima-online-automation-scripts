container_Serial = 0x44530811 # Serial of container to search
target_container_Serial = Player.Backpack.Serial # Serial of container to place desired items
item_ItemID = 0x2D33 # ItemID of item for which to search, such as Scimitar (0x2D33)

class Attribute:
    name = None
    value = None
    
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

# Specify attributes you're looking for
# If value doesn't matter, like with a slayer, leave it out
desired_attributes = [
    #Attribute('slayer'),
    Attribute('mana leech', 40.0),
    Attribute('stamina leech', 40.0),
    #Attribute('life leech'),
    #Attribute('swing speed')
]

items = Items.FindAllByID(item_ItemID,-1,container_Serial,0,0)
for item in items:
    score = 0
    item_attributes = Items.GetPropStringList(item)
    for attribute in desired_attributes:
        for attr in item_attributes:
            if attr.find(attribute.name) > -1:
                if attribute.value is None:
                    score += 1
                    break
                elif Items.GetPropValue(item,attr) >= attribute.value:
                    score += 1
                    break
            
    if score == len(desired_attributes):
        Items.Move(item, target_container_Serial, 1)
        Misc.Pause(1000)
        
    Misc.Pause(100)