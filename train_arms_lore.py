while Player.Dex > 103.0:
    Player.UseSkill("Arms Lore")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(0x4014F038)
    Misc.Pause(100)