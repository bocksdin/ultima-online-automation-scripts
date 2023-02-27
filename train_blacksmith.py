skill_level = Player.GetRealSkillValue('Blacksmith')
skill_cap = Player.GetSkillCap('Blacksmith')
hammer_gump = 949095101


while skill_level < skill_cap:
    skill_level = Player.GetRealSkillValue('Blacksmith')
    current_hammer = Items.FindByID(0x13E3,-1,Player.Backpack.Serial,0,0)
    Items.UseItem(current_hammer)
    Gumps.WaitForGump(hammer_gump, 10000)
        
    
    #CREATE MORE TINKER TOOLS
    tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
    while len(tinker_tools) < 2:
        Items.UseItemByID(0x1EB8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23)
        Misc.Pause(1000)
        tinker_tools = Items.FindAllByID(0x1EB8,-1,Player.Backpack.Serial,0,0)
        
    #CREATE MORE HAMMERS
    smith_hammers = Items.FindAllByID(0x13E3,-1,Player.Backpack.Serial,0,0)
    while len(smith_hammers) < 2:
        Items.UseItemByID(0x13E3)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 93)
        Misc.Pause(1000)
        smith_hammers = Items.FindAllByID(0x13E3,-1,Player.Backpack.Serial,0,0)
    
    # Create Cutlass
    if skill_level < 55.0:
        Gumps.SendAction(hammer_gump, 36)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 23)
        Misc.Pause(1500)
        
        cutlass = Items.FindByID(0x1441,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and cutlass is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(cutlass.Serial)
            Misc.Pause(500)
    # Create Katana
    elif skill_level < 59.5:
        Gumps.SendAction(hammer_gump, 36)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 37)
        Misc.Pause(1500)
        
        katana = Items.FindByID(0x13FF,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and katana is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(katana.Serial)
            Misc.Pause(500)
    # Create Scimitar
    elif skill_level < 70.5:
        Gumps.SendAction(hammer_gump, 36)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 58)
        Misc.Pause(1500)
        
        scimitar = Items.FindByID(0x13B6,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and scimitar is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(scimitar.Serial)
            Misc.Pause(500)
    # Create Platemail Gorget
    elif skill_level < 106.4:
        Gumps.SendAction(hammer_gump, 15)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 16)
        Misc.Pause(1500)
        
        gorget = Items.FindByID(0x1413,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and gorget is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(gorget.Serial)
            Misc.Pause(500)
    # Create Platemail Gloves
    elif skill_level < 108.9:
        Gumps.SendAction(hammer_gump, 15)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 9)
        Misc.Pause(2000)
        
        gloves = Items.FindByID(0x1414,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and gloves is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(gloves.Serial)
            Misc.Pause(500)
    # Create Platemail Arms
    elif skill_level < 116.3:
        Gumps.SendAction(hammer_gump, 15)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 2)
        Misc.Pause(2000)
        
        arms = Items.FindByID(0x1410,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and arms is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(arms.Serial)
            Misc.Pause(500)
    # Create Platemail Legs
    elif skill_level < 118.8:
        Gumps.SendAction(hammer_gump, 15)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 23)
        Misc.Pause(2000)
        
        legs = Items.FindByID(0x1411,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and legs is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(legs.Serial)
            Misc.Pause(500)
    # Create Platemail Tunics
    else:
        Gumps.SendAction(hammer_gump, 15)
        Gumps.WaitForGump(hammer_gump, 10000)
        Gumps.SendAction(hammer_gump, 30)
        Misc.Pause(2000)
        
        tunic = Items.FindByID(0x1415,-1,Player.Backpack.Serial,0,0)
        if Items.FindBySerial(current_hammer.Serial) is not None and tunic is not None:
            Gumps.WaitForGump(hammer_gump, 10000)
            Gumps.SendAction(hammer_gump, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(tunic.Serial)
            Misc.Pause(500)