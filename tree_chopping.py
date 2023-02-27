##### SET THESE YOURSELF #####
lumber_dropoff = 0x44b2d80a
beetle = 0xf8112
tree_books = []
home_lumber = 

##### DON'T CHANGE THESE #####
runes = [7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97]
wood_colors = [0x07da,0x04a8,0x04a9,0x04a7,0x047f,0x04aa,0x0000]
board_graphic = 0x1BD7
graphics_to_dropoff = [0x318F,0x3190,0x3199,0x2F5F]


def recall(book, rune):
    # This function will send your lumberjack to the next rune location
    Items.UseItem(book)
    Gumps.WaitForGump(0x554b87f3,1000)
    Gumps.SendAction(0x554b87f3,rune)
    Player.HeadMessage(33,"Book: {}, Rune: {}".format(book, rune))
    Misc.Pause(2000)

def equip_axe():
    # This function equips an axe if needed
    if not Player.CheckLayer('LeftHand'):
        axe = Items.FindByID(0x0F47,-1,Player.Backpack.Serial,0,0)
        if axe is not None:
            Player.EquipItem(axe)
            Misc.Pause(1000)
            
def cut_logs():
    # This function will cut logs into boards
    logs = Items.FindByID(0x1bdd,-1,Player.Backpack.Serial,0,0)
    if logs is not None:
        Items.UseItem(Player.GetItemOnLayer('LeftHand'))
        Target.WaitForTarget(1000)
        Target.TargetExecute(logs)
        Misc.Pause(300)
        
def chop_wood():
    # This function will chop the tree for wood
    # Tree should be 1 tile Northwest of your character
    tile = Statics.GetStaticsTileInfo(Player.Position.X - 1, Player.Position.Y - 1, 1)
    for i in tile:
        if Statics.GetTileFlag(i.StaticID,'Impassable') == True and Statics.GetTileFlag(i.StaticID,'Foliage') == False:
            axe = Player.GetItemOnLayer('LeftHand')
            if axe is not None:
                Items.UseItem(axe)
                Target.WaitForTarget(1000)
                Target.TargetExecute(Player.Position.X - 1, Player.Position.Y - 1 ,Player.Position.Z ,i.StaticID)
                Target.TargetExecute(Player.Position.X - 1, Player.Position.Y - 1 ,Player.Position.Z + 1 ,i.StaticID)
                Target.TargetExecute(Player.Position.X - 1, Player.Position.Y - 1 ,Player.Position.Z - 1 ,i.StaticID)
                Misc.Pause(2000)
                
def perform_dropoff(book, rune):
    if Player.Weight >= Player.MaxWeight * 0.9:
        Items.UseItem(home_lumber)
        Gumps.WaitForGump(0x554b87f3,1000)
        Gumps.SendAction(0x554b87f3,7)
        Misc.Pause(2000)
        for color in wood_colors:
            boards = Items.FindByID(board_graphic,color,Player.Backpack.Serial,0,0)
            if boards is not None:
                Items.Move(boards.Serial,lumber_dropoff,0)
                Misc.Pause(1000)
        for graphic in graphics_to_dropoff:
            item = Items.FindByID(graphic,-1,Player.Backpack.Serial,0,0)
            if item is not None:
                Items.Move(item.Serial,lumber_dropoff,0)
                Misc.Pause(1000)
                
        recall(book, rune)

for book in tree_books:
    for rune in runes:
        Journal.Clear()
        Misc.Pause(500)
        recall(book, rune)
        equip_axe()
        
        while not Journal.SearchByType('enough wood here','System'):
            Misc.Pause(300)
            cut_logs()
            chop_wood()
            perform_dropoff(book, rune)
                        

        

                    
