Misc.Pause(5000)
Items.UseItem(Items.FindByID(0x0FBF,-1,Player.Backpack.Serial,0,0))
while Player.GetSkillValue('Inscription') < 100.0:
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 21)
    Misc.Pause(2000)
    if Journal.Search('You have worn out your tool!'):
        Player.HeadMessage(33,'USING NEW TOOL')
        Journal.Clear()
        Items.UseItem(Items.FindByID(0x0FBF,-1,Player.Backpack.Serial,0,0))