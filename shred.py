mining_dropoff = 0x43A71A8B
fire_beetle = 0x001CCDFD
ore_books = [0x40D5A164, 0x40D584B3, 0x43FF770F, 0x40D5FAE2]
home_runebook = 0x43FFBD48
runes = [7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97]
ore_graphics = [0x19b9, 0x19b8, 0x19ba, 0x19b7]
ore_colors = [0x0000, 2419, 2406, 2413, 2418, 2213, 2425, 2207, 2219]
items_to_dropoff = [0x1bf2, 0x3192, 0x3193, 0x3194, 0x3195, 0x3197, 0x3198]

Misc.Pause(2000)
for book in ore_books:
  for rune in runes:
    Misc.Pause(250)
    Journal.Clear()
    Misc.Pause(250)
    Mobiles.UseMobile(fire_beetle)
    Misc.Pause(1000)
    if Player.Direction != 'North':
        Player.Walk('North')
        Misc.Pause(1000)
    Items.UseItem(book)
    Gumps.WaitForGump(0x554b87f3, 5000)
    Gumps.SendAction(0x554b87f3, rune)
    Player.HeadMessage(33, 'Rune {} {}'.format(book, rune))
    Misc.Pause(2000)
    Mobiles.UseMobile(Player.Serial)
    Misc.Pause(1000)
    while Journal.SearchByType('no metal here', 'System') is not True and Journal.SearchByType("can't mine that", 'System') is not True:
      if Journal.SearchByType("can't dig while riding or flying", 'System') is True:
        Mobiles.UseMobile(Player.Serial)
        Journal.Clear()
      if Journal.SearchByType('Script Error: UseItem: Invalid Serial', 'System') is True:
        Items.UseItem(Player.Backpack.Serial)
        Misc.Pause(1000)
        Journal.Clear()
      Misc.Pause(300)
      pickaxe = Items.FindByID(0xe86, -1, Player.Backpack.Serial, 0, 0)
      if pickaxe is not None:
        Items.UseItem(pickaxe.Serial)
        Target.WaitForTarget(1000)
        Target.TargetExecuteRelative(Player.Serial, 1)
      else:
        tinker_tools = Items.FindAllByID(0x1eb8, -1, Player.Backpack.Serial, 0, 0)
        if len(tinker_tools) < 2:
          Items.UseItem(tinker_tools[0].Serial)
          Gumps.WaitForGump(0x38920abd, 5000)
          Gumps.SendAction(0x38920abd, 8)
          Gumps.WaitForGump(0x38920abd, 5000)
          Gumps.SendAction(0x38920abd, 23)
          Misc.Pause(2000)

        Items.UseItem(tinker_tools[0].Serial)
        Gumps.WaitForGump(0x38920abd, 5000)
        Gumps.SendAction(0x38920abd, 8)
        Gumps.WaitForGump(0x38920abd, 5000)
        Gumps.SendAction(0x38920abd, 114)
        Misc.Pause(2000)

      if Player.Weight >= Player.MaxWeight:
        for graphic in ore_graphics:
          for color in ore_colors:
            ore_pile = Items.FindByID(graphic, color, Player.Backpack.Serial, 0, 0)
            if ore_pile is not None:
              Items.UseItem(ore_pile.Serial)
              Target.WaitForTarget(1000)
              Target.TargetExecute(fire_beetle)
        Journal.Clear()
      
      ingots = Items.FindAllByID(0x1bf2, -1, Player.Backpack.Serial, 0, 0)
      if sum([i.Amount for i in ingots]) > 1000:
        Misc.Pause(500)
        Mobiles.UseMobile(fire_beetle)
        Misc.Pause(1000)
        Items.UseItem(home_runebook)
        Gumps.WaitForGump(0x554b87f3, 5000)
        Gumps.SendAction(0x554b87f3, 7)
        Misc.Pause(2000)
        
        for item in items_to_dropoff:
          items = Items.FindAllByID(item, -1, Player.Backpack.Serial, 0, 0)
          for i in items:
            Items.Move(i.Serial, mining_dropoff, 0)
            Misc.Pause(1000)
        
        Items.UseItem(mining_dropoff)
        Misc.Pause(1000)
        iron_ingots = Items.FindByID(0x1bf2, 0x0000, mining_dropoff, 0, 0)
        if iron_ingots is not None:
          Items.Move(iron_ingots.Serial, Player.Backpack.Serial, 100)
          Misc.Pause(1000)

        Items.UseItem(book)
        Gumps.WaitForGump(0x554b87f3, 5000)
        Gumps.SendAction(0x554b87f3, rune)
        Misc.Pause(2000)
        Mobiles.UseMobile(Player.Serial)
        Misc.Pause(1000)


