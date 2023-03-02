from datetime import datetime
import time
from py_stealth import *

mining_dropoff = 0x43A71A8B
forge = 0x42A42FFD

ore_books = []
home_runebook = []
ore_graphics = [0x19b9, 0x19b8, 0x19ba, 0x19b7]
ore_colors = [0x0000, 2419, 2406, 2413, 2418, 2213, 2425, 2207, 2219]
items_to_dropoff = [0x1bf2, 0x3192, 0x3193, 0x3194, 0x3195, 0x3197, 0x3198]
runes = list(range(7, 103, 6))

def get_runebooks():
  # FIND RUNEBOOKS IN BACKPACK
  if FindType(0x22C5, Backpack()):
    for found in GetFindedList():
      name = GetTooltip(found).rsplit('|', 1)[1]
      if 'Ore' in name:
        ore_books.append(found)
      elif 'Home' in name:
        home_runebook.append(found)

def sacred_journey(book, rune):
  UseObject(book)
  Wait(500)
  NumGumpButton(0, rune)
  Wait(2000)

def unload(book, rune):
  # IF WEIGHT IS OVER 90% UTILIZED
  while Weight() >= MaxWeight() * 0.9:
    CancelTarget()
    Wait(300)
    while IsGump():
      CloseSimpleGump(0)
      Wait(300)

    # SACRED JOURNEY HOME
    sacred_journey(home_runebook[0], 7)

    # SMELT ALL DIFFERENT ORES IF MORE THAN 2 IN PILE
    for graphic in ore_graphics:
      for color in ore_colors:
        ore_pile = FindTypeEx(graphic, color, Backpack())
        if GetQuantity(ore_pile) > 1:
          UseObject(ore_pile)
          WaitTargetObject(forge)
          Wait(1000)
        Wait(100)
      Wait(100)

    # MOVE ALL INGOTS AND GEMS INTO THE DROPOFF CHEST
    for item in items_to_dropoff:
      for _ in range(5):
        if FindType(item):
          MoveItem(FindItem(), -1, mining_dropoff, 0xFFFF, 0xFFFF, 0)
          Wait(1000)

    # SACRED JOURNEY BACK TO MINING LOCATION
    sacred_journey(book, rune)

def craft_tools(book, rune):
  # IF LESS THAN 10 IRON INGOTS IN BACKPACK, GO GET SOME FROM HOME
  if GetQuantity(FindTypeEx(0x1bf2, 0x0000, Backpack(), False)) < 10:
    Wait(500)
    # SACRED JOURNEY HOME
    sacred_journey(home_runebook[0], 7)

    UseObject(mining_dropoff)
    Wait(1000)
    if FindTypeEx(0x1bf2, 0x0000, mining_dropoff, False):
      MoveItem(FindItem(), 50, Backpack(), 0xFFFF, 0xFFFF, 0)
      Wait(1000)

    # SACRED JOURNEY BACK TO PREVIOUS MINING LOCATION
    sacred_journey(book, rune)

  # IF LESS THAN 2 TINKER TOOLS, CRAFT MORE
  if Count(0x1eb8) < 2:
    UseObject(FindItem())
    Wait(500)
    NumGumpButton(0, 8)
    Wait(500)
    NumGumpButton(0, 23)
    Wait(2000)

  # CRAFT A NEW PICKAXE
  UseObject(FindType(0x1eb8, Backpack()))
  Wait(500)
  NumGumpButton(0, 8)
  Wait(500)
  NumGumpButton(0, 114)
  Wait(2000)

def mine(book, rune):
  if Weight() <= MaxWeight() * 0.9:
    # IF YOU HAVE A PICKAXE, MINE, ELSE CRAFT MORE
    if FindType(0xE86, Backpack()) > 0:
      UseObject(FindItem())
      WaitForTarget(5000)
      TargetToXYZ(GetX(Self()), GetY(Self()) - 1, 0)
      Wait(1000)
    else:
      craft_tools(book, rune)

def main():
  for book in ore_books:
    for rune in runes:
      ClearJournal()
      Wait(300)

      # OPEN BACKPACK TO PREVENT SCRIPT ISSUE
      UseObject(Backpack())
      Wait(1000)
      
      # MAKE SURE YOU'RE FACING NORTH
      if GetDirection(Self()) != 0:
        Step(0)
        Wait(300)
      
      # CLOSE OPEN GUMP TO PREVENT SCRIPT ISSUE
      while IsGump():
        CloseSimpleGump(0)
        Wait(300)
      
      # SACRED JOURNEY TO MINING LOCATION
      sacred_journey(book, rune)

      # MINE WHILE METAL TO MINE
      while InJournal('no metal here') == -1 and InJournal("can't mine that") == -1 and InJournal("can't mine there") == -1:
        Wait(300)

        unload(book, rune)
        mine(book, rune)

Wait(2000)
get_runebooks()
while True:
  main()