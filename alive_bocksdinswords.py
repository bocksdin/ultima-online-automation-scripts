from System.Collections.Generic import List
from System import Byte
#######################################################################################
#Purpose: Auto Targets mobs, casts Buffs, honors mobs, uses bag of sending,           #
#         handles bloodoath via eating apples/remove curse                            #
#                                                                                     #  
#Author: Bocksdin reachable on Discord - Bocksdin#1136                                #  
#Date: August 30, 2022                                                                #
#Tested on: Demise                                                                    #
#Template: Sampire                                                                    #
#######################################################################################

#      S E T T I N G S          S E T T I N G S         S E T T I N G S               #

#######################################################################################
#-------------------------------------------------------------------------------------#

def mobs_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs

use_honor = 1
use_eoo = 0

Misc.Pause(2000)
def chiv_spells(enemy):
    chiv_skill = Player.GetSkillValue('Chivalry')
    if Player.Hits >= Player.HitsMax * 0.9:
        if not Player.BuffsExist('Divine Fury') and Player.Mana >= 10:
            Spells.CastChivalry('Divine Fury')
            Misc.Pause(1000)
        if not Player.BuffsExist('Consecrate Weapon')  and Player.Mana >= 10:
            Spells.CastChivalry('Consecrate Weapon')
            Misc.Pause(1000)
        if use_eoo == 1 and not Player.BuffsExist('Enemy Of One') and enemy.Notoriety != 5 and Player.Mana >= 20:
            Spells.CastChivalry('Enemy Of One')
            Misc.Pause(1000)
        
def heal():
    if Player.Poisoned:
        Spells.CastChivalry('Cleanse by Fire')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)
    if Player.Hits <= Player.HitsMax * 0.5 and not Player.Poisoned:
        Spells.CastChivalry('Close Wounds')
        Target.WaitForTarget(2000)
        Target.TargetExecute(Player.Serial)

def weapon_skills():
    if nearby_enemies_len > 2 and not Player.HasSecondarySpecial and Player.Mana >= 8.0:
            Player.WeaponSecondarySA()
            Misc.Pause(700)
    elif not Player.HasPrimarySpecial and Player.Mana >= 18.0:
            Player.WeaponPrimarySA()
            Misc.Pause(700)


def fighting(enemy): 
    Player.Attack(enemy)
    #heal()
    chiv_spells(enemy)
    #weapon_skills()
    
def get_nearest(victims):
    return Mobiles.Select(victims, 'Nearest')

while not Player.IsGhost and Player.Visible:
    Misc.Pause(100)
    victims = mobs_list(10)
    
    if len(victims) > 0:
        honored_nearest = False
        nearest = get_nearest(victims)
        
        if use_honor == 1 and (not honored_nearest or Mobiles.FindBySerial(nearest.Serial) is None):
            Player.InvokeVirtue('Honor')
            Target.WaitForTarget(400)
            Target.TargetExecute(nearest)
            Misc.Pause(100)
            honored_nearest = True
        elif Mobiles.FindBySerial(nearest.Serial) is None:
            honored_nearest = False
            
        while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=10:    
            nearby_enemies_len = len(mobs_list(1))
            fighting(nearest)
            Misc.Pause(100)
            victims = mobs_list(10)
            if len(victims) > 0:
                nearest = get_nearest(victims)
