############################################################################################
#Author:  Dozen                                                                            #
#Discord: Dozen#0001                                                                       #
#Date: October 15, 2022                                                                    #
#Tested on:  UOGamers Demise                                                               #
#UOStealth Version:  9.4.0                                                                 #
#Python Version:   3.10.4                                                                  #
#Purpose: Collects Bods via logging in/out and cycling through each                        #
#         profile setup that you tell it, it will grab 1 Smith and 1 Tailor bod & sort     #
#         them into the appropriate book - it will do this every 60 minutes automatically  #
#         once the script is running, you will not have to do anything.                    #                                                               #
############################################################################################
#     ** NEED TO HAVE PYTHON 3.10 INSTALLED AS WELL AS DATETIME/REQUESTS MODULES **        #
############################################################################################
#  1. Profiles in Stealth need to be named in Stealth the same as what you name them here  #
#     in the section below this: I named mine Bod1-1 meaning Account 1 Character 1 etc     #
#     for organization sake/housekeeping                                                   #
#  2. Characters collecting bods need to be logged out above Luna bank                     #
#     in the corner by the inn                                                             #
#  3. If putting BODS in a book, they should be named Tailor and Blacksmith                #
#     if you dont have BOD books, it will just collect and leave them in your pack)        #
############################################################################################

from py_stealth import *
from stealth import *
from datetime import datetime, timedelta

############################################################################################
#Rememeber these need to be named the same HERE as you name them to login using stealth
############################################################################################
Profiles = ['Bod1-1', 'Bod1-2', 'Bod1-3', 'Bod1-4', 'Bod1-5', 'Bod1-6', 'Bod1-7', 'Bod2-1',
'Bod2-2', 'Bod2-3', 'Bod2-4', 'Bod2-5', 'Bod2-6', 'Bod2-7']


############################################################################################
Tailor = 0x0009B52A  # Serial of Luna tailor/weaver  (NOT THE GUILDMASTERS)
Blacksmith = 0x0009B4F7  # Serial of Luna Blacksmith (NOT THE GUILDMASTERS)
WAIT_TIME = 500

def ConnectChar(profile):
    print("Connecting with profile {}".format(profile))
    while not Connected():
        Connect()
        Wait(10000)
    print("{} connected".format(profile))


def DisconnectChar():
    print("Disconnecting...")
    while Connected():
        Disconnect()
        Wait(10000)
    print("Disconnected")


def GetBod(npc):
    RequestContextMenu(npc)
    Wait(600)
    SetContextMenuHook(npc, 1)
    Wait(1000)
    WaitGump('1')
    Wait(2000)


def SortBods():
    res = FindTypeEx(8793, 0, Backpack(), False)
    FoundBooks = GetFindedList()
    res = FindTypeEx(8792, 1155, Backpack(), False)  # Tailor
    if res != 0:
        FoundTailorBods = GetFindedList()
    else:
        FoundTailorBods = []
    res = FindTypeEx(8792, 1102, Backpack(), False)  # Blacksmith
    if res != 0:
        FoundBlacksmithBods = GetFindedList()
    else:
        FoundBlacksmithBods = []
    for book in FoundBooks:
        tooltip = GetTooltip(book)
        print(tooltip)
        if 'Tailor' in tooltip:
            for tbod in FoundTailorBods:
                MoveItem(tbod, 0, book, 0, 0, 0)
                Wait(1000)
        else:
            for bbod in FoundBlacksmithBods:
                MoveItem(bbod, 0, book, 0, 0, 0)
                Wait(1000)


# Main body
if __name__ == '__main__':
    print()
    WAIT_TIME = datetime.now()
    # Print while wait the time
    while True:
        if WAIT_TIME > datetime.now():
            print('Waiting for BOD cycle..')
        else:
            print('Starting Script')
            for Char in Profiles:
                changed = ChangeProfile(Char)
                if changed != 0:
                    print("Error while changing to profile {}. Result {}".format(Char, changed))
                ConnectChar(Char)
                GetBod(Tailor)
                GetBod(Blacksmith)
                ClickOnObject(Backpack())
                SortBods()
                DisconnectChar()
                #print("check1")
            WAIT_TIME = datetime.now() + timedelta(minutes = 60)
            #print("afterwait")
        Wait(1000)
