from datetime import datetime
import time
from py_stealth import *
pickaxe = 0xE86


def main():
    if FindType(pickaxe, Backpack()) > 0 and Weight() <= MaxWeight() - 50:
      UseObject(FindItem())
      WaitForTarget(5000)
      print("[ FIND ITEM: {} ]".format(FindItem()))
      TargetToXYZ(GetX(Self()), GetY(Self()) - 1, 0)
          # if TargetPresent() is True:
          #   print("[ TARGET PRESENT ]")
          #   print("[ {}, {}, {} ]".format(GetX(Self()), GetY(Self())-1, GetZ(Self())))
      Wait(1000)


while True:
     main()