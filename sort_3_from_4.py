three_mod_container_Serial = # Serial of target container for 3 mod items
four_mod_container_Serial = # Serial of target container for 4+ mod items
unsorted_container_Serial = # Serial of starting, cluttered container
item_to_sort_ItemID = # ItemID of item type to sort (like 0x2EDD for radiant scimitars)
sorting_weapons = False # If sorting weapons, set to True, else set to False


###### SHOULDNT NEED TO CHANGE ANYTHING BELOW THIS LINE ######
class Attribute:
    name = None
    value = None
    
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

weapon_attributes = [
  Attribute('hit '),
  Attribute('spell channeling'),
  Attribute('faster'),
  Attribute('swing speed'),
  Attribute('luck'),
  Attribute('chance increase'),
  Attribute('slayer'),
  Attribute('use best'),
  Attribute('resist'),
]

armor_attributes = [
  Attribute('night sight'),
  Attribute('reflect'),
  Attribute('increase'),
  Attribute('regeneration'),
  Attribute('luck'),
  Attribute('resist', 12.0),
  Attribute('cost'),
  Attribute('self repair'),
]

attributes = weapon_attributes if sorting_weapons == True else armor_attributes
items = Items.FindAllByID(item_to_sort_ItemID, -1, unsorted_container_Serial, 0, 0)
Player.HeadMessage(33, '{}'.format(len(items)))
for item in items:
  if item is not None:
    item_attributes = Items.GetPropStringList(item)
    score = 0
    for attr in item_attributes:
        for attribute in attributes:
          if attr.find(attribute.name) > -1:
            if attribute.value is None:
                score += 1
            elif Items.GetPropValue(item,attr) >= attribute.value:
                score += 1
        
        if score > 3:
          break

    if score > 3:
      Items.Move(item.Serial, four_mod_container_Serial, 1)
      Misc.Pause(525)
    else:
      Items.Move(item.Serial, three_mod_container_Serial, 1)
      Misc.Pause(525)
