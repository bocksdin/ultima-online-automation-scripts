while 1==1:
    Spells.Cast('Corpse Skin')
    Target.WaitForTarget(2000)
    Target.TargetExecute(Player.Serial)
    Misc.Pause(2000)