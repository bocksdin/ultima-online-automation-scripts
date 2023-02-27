runebooks = [0x43FFD4FA,0x43FF8AD4,0x4402664C,0x44026F10]
for book in runebooks:
    for i in range(16):
        Items.UseItem(book)
        Gumps.WaitForGump(1431013363, 1000)
        Gumps.SendAction(1431013363, 3)
        Misc.Pause(1000)