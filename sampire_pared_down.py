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
 
 
use_chivalry = 0
use_eoo = 1
use_df = 0
use_cw = 1

use_cursew = 0
use_ca = 1

use_honor = 0
change_weapons = 0
use_potions = 1
 
weapon_type = 0x2D33
is_katana = 0

Misc.Pause(2000)
has_bushido = Player.GetSkillValue('Bushido') > 0.0
bags_of_sending = Items.FindAllByID(0x0E76,-1,Player.Backpack.Serial,0,0)
current_bag_of_sending = 0

def curse_weapon():
    if not Player.BuffsExist('Curse Weapon'):
        Spells.CastNecro('Curse Weapon')
        Misc.Pause(1000)

def chiv_spells(enemy):
    if not Player.BuffsExist('Divine Fury') and use_df == 1 and Player.Mana >= 8:
        Spells.CastChivalry('Divine Fury')
        Misc.Pause(1000)
    if not Player.BuffsExist('Consecrate Weapon') and use_cw == 1  and Player.Mana >= 8:
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(1000)
    if not Player.BuffsExist('Enemy Of One') and enemy.Notoriety != 5 and use_eoo == 1 and Player.Mana >= 15:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(1000)

def bushido_skills():
    if has_bushido == True:
        if not Player.BuffsExist('Counter Attack') and use_ca == 1:
            Spells.Cast('Counter Attack')
            Misc.Pause(300)
        elif (Timer.Check('ConfidenceTimer')) and Player.Hits <= Player.HitsMax * .90:
            Spells.Cast('Confidence')
            Misc.Pause(300)
            Timer.Create('ConfidenceTimer', 4000)

def weapon_skills():    
    if is_katana == 1:
        if Player.Mana >= 30:
            if not Player.HasSecondarySpecial:
                Player.WeaponSecondarySA()
                Misc.Pause(300)
        elif Player.Mana >= 30:
            if not Player.HasPrimarySpecial:
                Player.WeaponPrimarySA()
                Misc.Pause(300)
        elif Player.Mana >= 5:
            if not Player.SpellIsEnabled('Lightning Strike'):
                Spells.CastBushido('Lightning Strike')
                Misc.Pause(300)
    else:
        if nearby_enemies_len > 2:
            if not Player.HasPrimarySpecial:
                Player.WeaponPrimarySA()
                Misc.Pause(700)
        elif has_bushido == True:
            if nearby_enemies_len > 1:
                if not Player.SpellIsEnabled('Momentum Strike'):
                    Spells.CastBushido('Momentum Strike')
                    Misc.Pause(700)
            else:
                if not Player.SpellIsEnabled('Lightning Strike'):
                    Spells.CastBushido('Lightning Strike')
                    Misc.Pause(700)
    

def remove_curse():
    if Player.BuffsExist('Curse'):
        apple = Items.FindByID(0x2FD8,-1,Player.Backpack.Serial,0,0)
        if apple is not None and not Timer.Check('AppleTimer'):
            Items.UseItem(apple)
            Misc.Pause(300)
            Timer.Create('AppleTimer', 1000*60*2)
    
def potions():
    if Player.Stam < 130.0:
        refresh_potions = Items.FindByID(0x0F0B,-1,Player.Backpack.Serial,0,0)
        if refresh_potions is not None:
            Items.UseItem(refresh_potions)
            Misc.Pause(300)
            
    remove_curse()
    
    if Player.Str <= 130.0:
        strength_potions = Items.FindByID(0x0F09,-1,Player.Backpack.Serial,0,0)
        if strength_potions is not None:
            Items.UseItem(strength_potions)
            Misc.Pause(300)
      
    if Player.Dex <= 130.0:
        agility_potions = Items.FindByID(0x0F08,-1,Player.Backpack.Serial,0,0)
        if agility_potions is not None:
            Items.UseItem(agility_potions)
            Misc.Pause(300)


def fighting(enemy): 
    Player.Attack(enemy)
    if use_potions == 1:
        potions()
    bushido_skills()
    if use_cursew == 1:
        curse_weapon()
    if use_chivalry == 1:
        chiv_spells(enemy)
    weapon_skills()
    
def get_nearest(victims):
    return Mobiles.Select(victims, 'Nearest')

while not Player.IsGhost and Player.Visible:
    Misc.Pause(100)
    if change_weapons == 1:
        weapon = Player.GetItemOnLayer('RightHand')
        if weapon is None or Items.GetPropValue(weapon,'durability') <= 0.0:
            extra_weapon = Items.FindByID(weapon_type,-1,Player.Backpack.Serial,0,0)
            if extra_weapon is not None and (Items.GetPropValue(extra_weapon,'durability') > 0.0 or Player.CheckLayer('RightHand') == False):
                Player.UnEquipItemByLayer('RightHand',5000)
                Misc.Pause(1000)
                Player.EquipItem(extra_weapon)
    
    victims = mobs_list(10)
    
    if len(victims) > 0:
        honored_nearest = False
        nearest = get_nearest(victims)
 
        while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=10:
        
            if use_honor == 1 and honored_nearest == False:
                Player.InvokeVirtue('Honor')
                Target.WaitForTarget(400)
                Target.TargetExecute(nearest)
                honored_nearest = True
                Misc.Pause(1000)
                
            nearby_enemies_len = len(mobs_list(1))
            fighting(nearest)
            Misc.Pause(100)
            victims = mobs_list(10)
            if len(victims) > 0:
                new_nearest = get_nearest(victims)
                if new_nearest.Serial != nearest.Serial:
                    honored_nearest = False
                    nearest = new_nearest

        if current_bag_of_sending < len(bags_of_sending):
            bag_of_sending = bags_of_sending[current_bag_of_sending]
            if Player.Weight > Player.MaxWeight * 0.95 and bag_of_sending != None:
                Player.HeadMessage(33,"SENDING")
                Items.UseItem(bag_of_sending.Serial)
                Target.WaitForTarget(5000)
                Target.TargetExecute(Items.FindByID(0x0EED,-1,Player.Backpack.Serial,0,0))
                Misc.Pause(500)
                if Items.GetPropValue(bag_of_sending, 'charges') == 0:
                    current_bag_of_sending += 1
