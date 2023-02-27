def magery():
    return Player.GetRealSkillValue('Magery')
    
while magery() < 100.0:
    while Player.Hits <= Player.HitsMax * 0.9:
        Spells.Cast('Heal')
        Target.WaitForTarget(1000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(1000)
        
    if magery() < 45.0:
        Spells.Cast('Fireball')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(2000)
    elif magery() < 55.0:
        Spells.Cast('Lightning')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(2000)
    elif magery() < 65.0:
        Spells.Cast('Paralyze')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(1000)
    elif magery() < 75.0:
        Spells.Cast('Reveal')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(1000)
    elif magery() < 90.0:
        Spells.Cast('Flamestrike')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
        Misc.Pause(2000)