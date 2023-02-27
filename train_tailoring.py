skill_level = Player.GetRealSkillValue('Tailoring')
skill_cap = Player.GetSkillCap('Tailoring')
trash_barrel = 0x4040A43F

def discard(item_id):
    while Items.FindByID(item_id,-1,Player.Backpack.Serial,0,0):
        if item_id == 0x175D:
            Items.Move(Items.FindByID(item_id,-1,Player.Backpack.Serial,0,0), trash_barrel, -1)
            Misc.Pause(700)
        else:
            Items.UseItem(0x42A42464)
            Target.WaitForTarget(10000)
            Target.TargetExecute(Items.FindByID(item_id,-1,Player.Backpack.Serial,0,0))
            Misc.Pause(1000)

while skill_level < skill_cap:
    skill_level = Player.GetRealSkillValue('Tailoring')
    
    # CREATE MORE TINKER TOOLS
    tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
    while len(tinker_tools) < 2:
        Items.UseItemByID(0x1EB8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23)
        Misc.Pause(1000)
        tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
        
    # CREATE MORE SEWING KITS
    sewing_kits = Items.FindAllByID(0x0F9D,-1,Player.Backpack.Serial,0,0)
    while len(sewing_kits) < 2:
        Items.UseItemByID(0x1EB8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 44)
        Misc.Pause(1000)
        sewing_kits = Items.FindAllByID(0x0F9D,-1,Player.Backpack.Serial,0,0)
       
    leather = Items.FindByID(0x1081,-1,Player.Backpack.Serial,0,0)
    if leather.Amount < 100:
        leather_in_bank = Items.FindByID(0x1081,-1,Player.Bank.Serial,0,0)
        if leather_in_bank is not None:
            Items.Move(leather_in_bank.Serial, Player.Backpack, 400)
            Misc.Pause(1000)

    current_tools = Items.FindByID(0x0F9D,-1,Player.Backpack.Serial,0,0)
    Items.UseItem(current_tools)
    Gumps.WaitForGump(949095101, 10000)
    
    # Create Fur Boots
    if skill_level < 54.0:
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 9)
        Misc.Pause(2000)
        discard(0x2307)
    # Create Robes
    elif skill_level < 65.0:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 58)
        Misc.Pause(2000)
        discard(0x1F03)
    # Create Kasa
    elif skill_level < 72.0:
        Gumps.SendAction(949095101, 1)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 100)
        Misc.Pause(2000)
        discard(0x2798)
    # Create Ninja Tabi
    elif skill_level < 78.0:
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 16)
        Misc.Pause(2000)
        discard(0x2797)
    # Create Oil Cloths
    elif skill_level < 99.6:
        Gumps.SendAction(949095101, 22)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 72)
        Misc.Pause(2000)
        discard(0x175D)
    # Create Elven Shirt
    elif skill_level < 105.0:
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 135)
        Misc.Pause(2000)
        discard(0x3175)
    # Create Studded Tunic
    elif skill_level < 117.5:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 30)
        Misc.Pause(2000)
        discard(0x13DB)
    # Create Studded Do
    else:
        Gumps.SendAction(949095101, 43)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 44)
        Misc.Pause(2000)
        discard(0x27C7)
        