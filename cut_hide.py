while 1==1:
    if Items.FindByID(0x1079,-1,Player.Backpack.Serial,0,0) is not None:
        Items.UseItemByID(0x0F9F,-1)
        Target.WaitForTarget(1000)
        Target.TargetExecute(Items.FindByID(0x1079,-1,Player.Backpack.Serial,0,0))
        Misc.Pause(1000)
        
    if Player.Weight > 400 and Items.FindByID(0x1079,-1,Player.Backpack.Serial,0,0) is None:
        Items.UseItemByID(0x0E76,-1)
        Target.WaitForTarget(1000)
        Target.TargetExecute(Items.FindByID(0x1081,-1,Player.Backpack.Serial,0,0))
        Misc.Pause(1000)
        
    Misc.Pause(500)