while Player.Dex > 130.0:
    Items.UseItemByID(0x0DE1,-1)
    Misc.Pause(500)

    backpack_kindling = Items.FindByID(0x0DE1,-1,Player.Backpack.Serial,0,0)
    bank_kindling = Items.FindByID(0x0DE1,-1,Player.Bank.Serial,0,0)
    if bank_kindling is not None and (backpack_kindling is None or backpack_kindling.Amount < 1):
        Items.Move(bank_kindling,Player.Backpack,20)
        Misc.Pause(1000)
    