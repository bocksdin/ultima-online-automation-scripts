while Player.Dex < 120.0:
    Player.HeadMessage(33, '{}'.format(Player.Dex))
    Spells.CastChivalry('Noble Sacrifice')
    Misc.Pause(2000)