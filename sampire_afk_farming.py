from System.Collections.Generic import List
from System import Byte

#      S E T T I N G S          S E T T I N G S         S E T T I N G S               #

#######################################################################################
#-------------------------------------------------------------------------------------#
#Settings/Options for script-change or dont change whatever suits your needs          #
#-------------------------------------------------------------------------------------#
castingDelayTweak = 25 #this is for casting speed, increase little by little          #
#to account for any possible latency if you find its casting too fast                 #
#-------------------------------------------------------------------------------------#
 
 
use_eoo = 1
use_df = 1
use_cw = 1
use_cursew = 1
use_ca = 1
use_honor = 1

use_chivalry = 1
 
weapon_type = 0x2D33
items_to_send = [0x0F16,0x0F10,0x0F15,0x0F25,0x0F26,0x0F13,0x0F21,0x0F19,0x0F2D]

Misc.Pause(2000)
has_bushido = Player.GetSkillValue('Bushido') > 0.0
bags_of_sending = Items.FindAllByID(0x0E76,-1,Player.Backpack.Serial,0,0)
current_bag_of_sending = 0
Player.HeadMessage(33,"{} {}".format(len(bags_of_sending), current_bag_of_sending))
    
def mobs_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs


def fighting(enemy): 
 
    Player.Attack(nearest)
    
    if use_chivalry == 1:
        if not Player.BuffsExist('Divine Fury') and use_df == 1 and Player.Mana >= 8:
            Spells.CastChivalry('Divine Fury')
            Misc.Pause(1000)
        if not Player.BuffsExist('Consecrate Weapon') and use_cw == 1  and Player.Mana >= 8:
            Spells.CastChivalry('Consecrate Weapon')
            Misc.Pause(1000)
    if not Player.BuffsExist('Enemy Of One') and enemy.Notoriety != 5 and use_eoo == 1 and Player.Mana >= 15:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(1000)
    if has_bushido == True:
        if not Player.BuffsExist('Counter Attack') and use_ca == 1 and Player.Mana >= 10:
            Spells.Cast('Counter Attack')
            Misc.Pause(500)
        elif (Timer.Check('ConfidenceTimer')) and Player.Hits <= Player.HitsMax * .90 and Player.Mana >= 10:
            Spells.Cast('Confidence')
            Misc.Pause(1000)
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
        
        if current_bag_of_sending < len(bags_of_sending):
            bag_of_sending = bags_of_sending[current_bag_of_sending]
            if Player.Weight > Player.MaxWeight * 0.95 and bag_of_sending != None:
                Player.HeadMessage(33,"SENDING")
                Items.UseItem(bag_of_sending.Serial)
                Target.WaitForTarget(1000)
                Target.TargetExecute(Items.FindByID(0x0EED,-1,Player.Backpack.Serial,0,0))
                Misc.Pause(500)
                    
            for item in Items.FindAllByID(items_to_send,-1,Player.Backpack.Serial,0,0):
                if item.Amount >= 200:
                    Player.HeadMessage(33,"SENDING GEM")
                    Items.UseItem(bag_of_sending.Serial)
                    Target.WaitForTarget(1000)
                    Target.TargetExecute(item)
                    Misc.Pause(500)
                    
            if Items.GetPropValue(bag_of_sending, 'charges') == 0:
                current_bag_of_sending += 1
            
    else:
        Misc.Pause(100)
                
