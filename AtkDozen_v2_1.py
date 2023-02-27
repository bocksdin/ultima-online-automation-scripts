from System.Collections.Generic import List
from System import Byte 
from datetime import datetime, timedelta
import re
#######################################################################################
#-------------------------------------------------------------------------------------#
#Settings/Options for script-change or dont change whatever suits your needs
#-------------------------------------------------------------------------------------#
#######################################################################################
def mobs_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.IsHuman = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
#################################################################################################
move = True #Set to True if you want your char to pathfind to targets
return_to_start = False #Set to 1 if you would like to return to xyz coord you pressed play at
use_enemyofone = 0 #Set to 1 for Enemy of One - Otherwise 0 
use_divinefury = 1 #Set 1 for Divine Fury - Otherwise 0
use_consecratewep = 1 #Set 1 for Consecrate Weapon - Otherwise 0
use_counterattack = 1 #Set 1 for Counter Attack - Otherwise 0
use_curseweapon = 1 #Set 1 for Curse Weapon - Otherwise 0
use_cleansebyfire = 0 #Set 1 for Cleanse by Fire - Otherwise 0
use_closewounds = 0 #Set 1 for Close Wounds - Otherwise 0
#----------------------------------------------------------------------------------
ls_or_ability = 2 # ls == 1 #Set 1 for Lightning Strike, 
#Set 2 for Primary Ability, Set 3 for Secondary Ability
#----------------------------------------------------------------------------------
use_honor = 1 #Set 1 for Honor - Otherwise 0
use_momentummstrike = 1 #Set 1 for Momentum Strike - Otherwise 0
appt = datetime.now() #This is the enchanted apple timer

bag_of_sending = Items.FindByName('a bag of sending',-1,Player.Backpack.Serial,0,0)
#-------------------------------------------------------------------------------------#
castingDelayTweak = 25 #this is for casting speed, increase little by little          #
#to account for any possible latency if you find its casting too fast                 #
#-------------------------------------------------------------------------------------#
#######################################################################################
startX = Player.Position.X  #Starting Coordinates for Return to Start Function        #
startY = Player.Position.Y                                                            #
startZ = Player.Position.Z                                                            #
startPos = Player.Position  #Setting the coords to variable                           #
#######################################################################################    
def MoveToEnnemy(n): #Move to Enemy/Target Function
    if move:
        Player.PathFindTo(n.Position.X, n.Position.Y, n.Position.Z)
        Misc.Pause(550)
##############################################################################
def returnToStart(): #Return to Starting Coords Function/Timer
    if return_to_start:
        if (Player.Position.X != startPos.X) and (Player.Position.Y != startPos.Y ):
            Misc.Pause (5000)
            Misc.SendMessage(' [Returning] ', 1271)
            Player.PathFindTo(startPos.X, startPos.Y, startPos.Z )
            Misc.Pause(1000)
###################################################################################################### 
def bloodoath(): #The handling of Blood Oath function
    global appt
    apple = Items.FindByID(0x2FD8,-1,Player.Backpack.Serial) #this is incase you dont have any apples
    if Items.FindByID(0x2FD8,-1,Player.Backpack.Serial) == None:
            Player.HeadMessage(2041, '[Out of Apples!]')
            Spells.CastChivalry('Remove Curse')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(450)
    if apple: #this eats an apple if you have any
        if appt <= datetime.now(): 
            Player.HeadMessage(1271, '[Eating Apple and setting timer!]')
            Items.UseItem(apple)
            appt = datetime.now() + timedelta(seconds = 120)
            Misc.Pause(450)
        else: #this is incase apples are on cooldown
            Player.HeadMessage(2092, '[Apples on cooldown!]')
            Spells.CastChivalry('Remove Curse')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(450)
    Misc.Pause(550)
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
######################################################################################################### 
#           STAND-BY THREAD (meaning NO mobs in range) this is where things like curing poison          #                #
#########################################################################################################
def standbythread():
    if Player.Poisoned and use_cleansebyfire == 1 and Player.Hits <= Player.HitsMax * .80 and Player.Mana >= 10:
            Spells.Cast('Cleanse By Fire')
            Target.WaitForTarget(fcDelay(2))
            Target.TargetExecute(Player.Serial)
            Misc.Pause(fcrDelay())
            Misc.Pause(350)
    elif not (Timer.Check('ConfTimer')) and Player.Hits <= Player.HitsMax * .80 and Player.Mana >= 10:
            Spells.CastBushido('Confidence')
            Target.WaitForTarget(fcDelay(2))
            Misc.Pause(fcrDelay())
            Timer.Create('ConfTimer', 5000)
    elif Player.Hits <= Player.HitsMax * .60 and use_closewounds == 1 and Player.Mana >= 10 and not Player.Poisoned:
            Spells.CastChivalry('Close Wounds')
            Target.WaitForTarget(fcDelay(2))
            Target.TargetExecute(Player.Serial)
            Misc.Pause(fcrDelay())
Misc.Pause(50)
###################################################################################################    
def fighting(enemy): #the attack thread/targeting thread
        
    Player.Attack(nearest)  
    if nearest.Notoriety != 5 and use_enemyofone == 1 and Player.Mana >= 20:
        Spells.CastChivalry('Enemy of One')
        Target.WaitForTarget(fcDelay(1))
        Misc.Pause(fcrDelay())
    elif not Player.BuffsExist('Counter Attack') and use_counterattack == 1 and Player.Mana >= 5:
        Spells.CastBushido('Counter Attack')
        Target.WaitForTarget(fcDelay(1))
        Misc.Pause(fcrDelay())       
    elif Player.Stam <= Player.StamMax * .85 and use_divinefury == 1 and Player.Mana >= 10:
        Spells.CastChivalry('Divine Fury')
        Target.WaitForTarget(fcDelay(2))
        Misc.Pause(fcrDelay())
    elif not Player.BuffsExist('Consecrate Weapon') and use_consecratewep == 1 and Player.Mana >= 10:
        Spells.CastChivalry('Consecrate Weapon')
        Target.WaitForTarget(fcDelay(2))
        Misc.Pause(fcrDelay())
    elif Player.Hits <= Player.HitsMax * .90 and (Timer.Check('ConfTimer')) == False and Player.Mana >= 10:
        Spells.CastBushido('Confidence')
        Timer.Create('ConfTimer', 5000)
        Target.WaitForTarget(fcDelay(1))
        Misc.Pause(fcrDelay())
    elif not Player.BuffsExist('Curse Weapon') and use_curseweapon == 1 and Player.Mana >= 7:
        Spells.Cast('Curse Weapon')
        Target.WaitForTarget(fcDelay(1))
        Misc.Pause(fcrDelay())  
    if nearby_enemies_len >= 1: #if 1 mob
        if ls_or_ability == 1:
            if not Player.SpellIsEnabled('Lightning Strike') and not Player.HasSpecial and Player.Mana >= 10:
                Spells.CastBushido('Lightning Strike')
                Misc.Pause(fcrDelay())
        elif ls_or_ability == 2:
            if not Player.HasPrimarySpecial and Player.Mana >= 10:
                Player.WeaponPrimarySA()
        elif ls_or_ability == 3:
            if not Player.HasSecondarySpecial and Player.Mana >= 10:
                Player.WeaponSecondarySA()
        Misc.Pause(150)            
while not Player.IsGhost and Player.Visible:

    victims = mobs_list(10)

    if len(victims) > 0:
        nearest = Mobiles.Select(victims, 'Nearest')
        #Player.HeadMessage(1265, 'Target is: {}'.format(nearest.Name))
        if use_honor == 1:
            Journal.Clear()
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(750, True)
            Target.TargetExecute(nearest)
            Journal.WaitJournal('Honorable',2)
            MoveToEnnemy(nearest)
        while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=10:#:
            nearby_enemies_len = len(mobs_list(1))
            #Misc.SendMessage (nearby_enemies_len)
            #Misc.SendMessage('FIGHTING WITH : {}'.format (nearest.Name),1171)
            fighting(nearest)
            MoveToEnnemy(nearest)
            Misc.Pause(100)
            
    else:
        standbythread()
        returnToStart()
        #Misc.SendMessage('no enemy')
        Misc.Pause(10)
        
    if Player.Weight > 500 and bag_of_sending != None:
        Items.UseItem(bag_of_sending.Serial)
        Target.WaitForTarget(5000)
        Target.TargetExecute(Items.FindByID(0x0EED,-1,Player.Backpack.Serial,0,0))
Misc.Pause(50)