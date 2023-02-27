from System.Collections.Generic import List
from System import Byte
#######################################################################################
#Purpose: Auto Targets mobs, casts Buffs, heals, honors mobs, uses bag of sending,    #
#         dispels revenants, handles bloodoath via eating apples/remove curse,        #
#         auto insures loot.                                                          #  
#Author: Dozen reachable on Discord - Dani Mocanu#2660 - Dozen#1351                   #  
#Date: August 30, 2022                                                                #
#Tested on: Demise                                                                    #
#Template: Sampire (will be adding in the ability to use pets/tamer template)         #
#######################################################################################

#      S E T T I N G S          S E T T I N G S         S E T T I N G S               #

#######################################################################################
#-------------------------------------------------------------------------------------#
#Settings/Options for script-change or dont change whatever suits your needs          #
#-------------------------------------------------------------------------------------#
castingDelayTweak = 100 #this is for casting speed, increase little by little          #
#to account for any possible latency if you find its casting too fast                 #
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
 
 
use_eoo = 0
use_df = 1
use_cw = 1
use_cursew = 0
use_ca = 1
use_honor = 1
 
weapon_type = 0x2D33

Misc.Pause(2000)
has_bushido = Player.GetSkillValue('Bushido') > 0.0
bags_of_sending = Items.FindAllByID(0x0E76,-1,Player.Backpack.Serial,0,0)
current_bag_of_sending = 0

######################################################################################################    
def fcDelay(spellLevel):
    fc = int((((3 + spellLevel) / 4) * 1000) - ((Player.FasterCasting * .25) * 1000))
    if fc < 250:
        fc = 250
    return fc    
def fcrDelay():
    fcr = int(((6 - Player.FasterCastRecovery) / 4) * 1000)
    if fcr < 0:
        fcr = 0
    return fcr
def castingDelay(spellLevel):
    fc = fcDelay(spellLevel)
    fcr = fcrDelay()
    castingDelay = fc + fcr + castingDelayTweak
    #Misc.SendMessage('{} + {} + {} = {}'.format(fc, fcr, castingDelayTweak, castingDelay), 89)
    return castingDelay  
    

##################################################################################### 
def bloodoath():
    global appt
    apple = Items.FindByID(0x2FD8,-1,Player.Backpack.Serial) #this is incase you dont have any apples
    if Items.FindByID(0x2FD8,-1,Player.Backpack.Serial) == None:
            Player.HeadMessage(2041, 'Out of Apples!')
            Spells.CastChivalry('Remove Curse')
            Target.WaitForTarget(fcDelay(2))
            Target.TargetExecute(Player.Serial)
            Misc.Pause(fcrDelay())
            Misc.Pause(400)
    if apple: #this eats an apple if you have any
        if appt <= datetime.now(): 
            Player.HeadMessage(1271, 'Eating Apple and setting timer!')
            Items.UseItem(apple)
            appt = datetime.now() + timedelta(seconds = 120)
            Misc.Pause(400)
        else: #this is incase apples are on cooldown
            Player.HeadMessage(2092, 'Apples on cooldown!')
            Spells.CastChivalry('Remove Curse')
            Target.WaitForTarget(fcDelay(2))
            Target.TargetExecute(Player.Serial)
            Misc.Pause(fcrDelay())
    Misc.Pause(550)


def fighting(enemy): 
 
    Player.Attack(nearest)
    
    if not Player.BuffsExist('Curse Weapon') and use_cursew == 1 and Player.Mana >= 7:
        Spells.CastNecro('Curse Weapon')
        Misc.Pause(500)
    if not Player.BuffsExist('Divine Fury') and use_df == 1 and Player.Mana >= 8:
        Spells.CastChivalry('Divine Fury')
        Misc.Pause(500)
    if not Player.BuffsExist('Consecrate Weapon') and use_cw == 1  and Player.Mana >= 8:
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
    if enemy.Notoriety != 5 and use_eoo == 1 and Player.Mana >= 15:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
    if has_bushido == True:
        if not Player.BuffsExist('Counter Attack') and use_ca == 1 and Player.Mana >= 10:
            Spells.Cast('Counter Attack')
        elif (Timer.Check('ConfidenceTimer')) and Player.Hits <= Player.HitsMax * .90 and Player.Mana >= 10:
            Spells.Cast('Confidence')
            Misc.Pause(500)
            Timer.Create('ConfidenceTimer', 4000)
        
    if Player.Mana >= 10:
        if nearby_enemies_len > 2:
            if not Player.HasPrimarySpecial:
                Player.WeaponPrimarySA()
                Misc.Pause(500)
        elif has_bushido == True:
            if nearby_enemies_len > 1:
                if not Player.SpellIsEnabled('Momentum Strike'):
                    Spells.CastBushido('Momentum Strike')
                    Misc.Pause(500)
            else:
                if not Player.SpellIsEnabled('Lightning Strike'):
                    Spells.CastBushido('Lightning Strike')
                    Misc.Pause(500)
            

while not Player.IsGhost and Player.Visible:
    weapon = Player.GetItemOnLayer('RightHand')
    if weapon is None or Items.GetPropValue(weapon,'durability') <= 0.0:
        extra_weapon = Items.FindByID(weapon_type,-1,Player.Backpack.Serial,0,0)
        if extra_weapon is not None and (Items.GetPropValue(extra_weapon,'durability') > 0.0 or Player.CheckLayer('RightHand') == False):
            Player.UnEquipItemByLayer('RightHand',5000)
            Misc.Pause(1000)
            Player.EquipItem(extra_weapon)
    
    victims = mobs_list(8)
    
    if len(victims) > 0:
        honored_nearest = False
        nearest = Mobiles.Select(victims, 'Nearest')
        
        if use_honor == 1 and honored_nearest == False:
            Player.InvokeVirtue('Honor')
            Target.WaitForTarget(400)
            Target.TargetExecute(nearest)
            honored_nearest = True
 
        while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=8:
            nearby_enemies_len = len(mobs_list(1))
            fighting(nearest)
            Misc.Pause(100)
            
    else:
        Misc.Pause(100)

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
