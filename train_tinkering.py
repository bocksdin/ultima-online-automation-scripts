skill_level = Player.GetRealSkillValue('Tinkering')
skill_cap = Player.GetSkillCap('Tinkering')
gump = 949095101
trash_barrel = 0x41A799CD

def discard(item_id):
    while Items.FindByID(item_id,-1,Player.Backpack.Serial,0,0):
        Items.Move(Items.FindByID(item_id,-1,Player.Backpack.Serial,0,0), trash_barrel, -1)
        Misc.Pause(700)


while skill_level < skill_cap:
    skill_level = Player.GetRealSkillValue('Tinkering')
    
    # CREATE MORE TINKER TOOLS
    tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
    while len(tinker_tools) < 2:
        Items.UseItemByID(0x1EB8)
        Gumps.WaitForGump(gump, 10000)
        Gumps.SendAction(gump, 8)
        Gumps.WaitForGump(gump, 10000)
        Gumps.SendAction(gump, 23)
        Misc.Pause(1000)
        tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)

    current_tools = Items.FindByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
    Items.UseItem(current_tools)
    Gumps.WaitForGump(gump, 10000)
    
    # Create Scissors
    if skill_level < 45.0:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 2)
        Misc.Pause(1500)
        discard(0x0F9F)
    # Create Tongs
    elif skill_level < 60.0:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 86)
        Misc.Pause(1500)
        discard(0x0FBB)
    # Create Lockpicks
    elif skill_level < 75.0:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 121)
        Misc.Pause(1500)
        discard(0x14FC)
    # Create Bracelets
    elif skill_level < 85.0:
        Gumps.SendAction(949095101, 36)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 9)
        Misc.Pause(1500)
        discard(0x1086)
    # Create Spyglasses
    elif skill_level < 90.0:
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 37)
        Misc.Pause(1500)
        discard(0x14F5)
        discard(0x0E9B)
    # Create Rings
    else:
        Gumps.SendAction(949095101, 36)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 2)
        Misc.Pause(1500)
        discard(0x108A)
        discard(0x1011)