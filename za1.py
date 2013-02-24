import zombie_classes
import random
from sys import exit
global prompt
prompt = "//:>"
#:In the future make tool to be able to extract elements from a list two
#:or more at a time from a list or within elements of the list
#:humvee fight or airport fight.
#:Marina fight and then boat
#:head to islands
#:build combat engine
#:Refinements left to implement, weight issue.
#:amount of individual weapons available
#:Missing story if you have a weapon but no ammo and no knife



def open():
    print r'''
#:#############################################################################################
#:#############################################################################################
#:#############################################################################################
#:###########################                     #############################################
#:###########################    Zombie Adventure #############################################
#:###########################                     #############################################
#:#############################################################################################
#:#############################################################################################
#:#############################################################################################
'''

    print "...\t\t\t...\t..." * 3
    print "...\t\t\t...\t..." * 3
    print "...\t\t\t...\t..." * 3
    print "It's finally happened, the wish everyone has had since the beginning\n\
of hatchets and cheap ammo, the Mutha fuckin zombie Apocalypse."
    print "...\t\t\t...\t..." * 3
    print "...\t\t\t...\t..." * 3
    print "...\t\t\t...\t..." * 3

open()


def opening():
    global player
    p_avatar = zombie_classes.Avatar()

    print"To Pick your Avatar, type in their number \n\
for 15 extra health and stamina points type R for random pick\n\n"
    a = p_avatar.Anna ()
    v = p_avatar.Victor()
    g = p_avatar.Gabriel()
    print '1: Anna:    ' + p_avatar.Anna.Anna_stats
    print '2: Victor:  ' + p_avatar.Victor.Victor_stats
    print '3: Gabriel: ' + p_avatar.Gabriel.Gabriel_stats


    avatar_pick = raw_input(prompt)

    if avatar_pick == '1':
        player = a
    elif avatar_pick == '2':
        player = v
    elif avatar_pick == '3':
        player = g
    elif avatar_pick == "r" or avatar_pick =="R":
        ply = random.choice('avg')
        if ply == 'a':
            player = a
            a.Health_Points += 15
            a.Stamina_Points +=15

        if ply == 'v':
            player = v
            v.Health_Points +=15
            v.Stamina_Points +=15

        if ply == 'g':
            player = g
            g.Health_Points +=15
            g.Stamina_Points +=15

    else:
        print "Please make a valid choice"
        return opening()

    print "\n\nyour avatar is:" , player.Name + "\n\n"
    return player

opening()


def opening_cont():

    print "Lucky for you, you have survived the first wave of panic and death it is"
    print "said that the dead are probably the lucky ones, its probably true but you"
    print "are surprised that you aren't gripped by panic but rather a cool demeanor"
    print "you think for a minute  and you make an assesment on your situation, this is"
    print "mostly because you are in your friends mansion and the chaos is down below in"
    print "torrance and Redondo beach. You are a top the Palos Verdez peninzula, everything"
    print "south of you is burning and from the news reports, it dawns on you that you will"
    print "not be safe for much longer; you remeber that your friend is a gun afficionado,"
    print "and you think to yourself fuck yeah, time to blow some heads then you realize"
    print "that this is not a video game and once you're bitten you're fucked further more your"
    print "asthma prevents you from carrying more then a few things on you at any one time."

opening_cont()


def destiny():
    global player
    riffle = zombie_classes.The_GunRoom.Riffle_rack
    guns = zombie_classes.The_GunRoom.guns
    knives = zombie_classes.The_GunRoom.Knife_rack
    Ammo = zombie_classes.The_GunRoom.Ammo_rack

    print "\n\nDo you choose to stay in the mansion or to make it to the marina"
    print "////////////    press 1 to stay in the mansion    //////////////"
    print "////////////    press 2 to head to the marina     //////////////"
    mansion_or_marina = raw_input(prompt)

    if mansion_or_marina == '1':
        star = zombie_classes.remain_in_mansion()
        return
    elif mansion_or_marina == '2':
        print "You choose to make a run for the marina"
    else:
        print "Invalid choice"
        return destiny()

    print "You go into your friends weapons room and see an assortment of weapons"
    print "there is a rack with knives of various sizes the wall next to it has rifles of various calibers,"
    print "next to it is a locker with ammo for all the weapons"
    print "finally you see a rack with handguns. You know you can't take more then four weapons at a time.\n"
    print (r"//////////////////////////////////************************* *\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    def Weapon_Layout(x):

        print "Riffle rack:\n"
        for i in riffle:
            print i
        print "\n"

        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print "Hand Gun Rack:\n"
        for g in guns:
            print g
        print "\n"

        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print "Knife Rack:\n"
        for i in knives:
            print i

    if mansion_or_marina == '2':
        Weapon_Layout(2)

    else:
        print "\n\nplease make a valid choice"
        return destiny()

    def weapons_pick():

        def weapons_bag():

            if len(player.weapon) > 4:

                print "You have too many weapons in your bag"
                print "To see the weapons in your bag type 'w"
                print "To see the Ammo in your bag type 'a'"
                w_remove = raw_input(prompt)
                if w_remove == 'w' or w_remove == 'W':
                    for w in player.weapon:
                        print w
                    print "\nTo remove a weapon, type in its number"
                    print "for example to remove the first weapon type in '1'"
                    w_remove = raw_input(prompt)
                    if w_remove == '1':
                        player.weapon.pop(0)
                    elif w_remove == '2':
                        player.weapon.pop(1)
                    elif w_remove == '3':
                        player.weapon.pop(2)
                    elif w_remove == '4':
                        player.weapon.pop(3)
                    elif w_remove == '5':
                        player.weapon.pop(4)
                    else:
                        print "please make a valid choice"
                        return weapons_pick()
                    for w in player.weapon:
                        print w
                    return weapons_pick()

                elif w_remove == 'a' or w_remove == 'A':
                    for a in player.amount_of_ammo:
                        print a
                    print "To remove ammo, type in its number"
                    print "for example to remove the first item type in '1'"
                    a_remove = raw_input(prompt)
                    if a_remove == '1':
                        player.amount_of_ammo.pop(0)
                    elif a_remove == '2':
                        player.amout_of_ammo.pop(1)
                    elif a_remove == '3':
                        player.amout_of_ammo.pop(2)
                    elif a_remove == '4':
                        player.amout_of_ammo.pop(3)
                    elif a_remove == '5':
                        player.amout_of_ammo.pop(4)
                    elif a_remove == '6':
                        player.amout_of_ammo.pop(5)
                    elif a_remove == '7':
                        player.amout_of_ammo.pop(6)
                    elif a_remove == '8':
                        player.amout_of_ammo.pop(7)
                    elif a_remove == '9':
                        player.amout_of_ammo.pop(8)
                    elif a_remove == '10':
                        player.amout_of_ammo.pop(9)
                    elif a_remove == '11':
                        player.amout_of_ammo.pop(10)
                    elif a_remove == '12':
                        player.amout_of_ammo.pop(11)

                else:
                    print "please make a valid choice"
                    return weapons_pick()
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print "These are your weapons:\n"
            for a in player.weapon:
                print a
            print "\n"
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print "This is your ammo:\n"
            for a in player.amount_of_ammo:
                print a
            print "\n\n"
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            return weapons_pick()
        def ammo_count():
            global player

            for a in player.amount_of_ammo:
                if player.amount_of_ammo.count('Ammo 1: H&K Machinegun  ' 'Cal 5.56 M' 'Ammo Weight:12.0 lbs  Amount:200') > 4 :
                    print "you have too much of %r ammo" % player.amount_of_ammo[0]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 2: Rem 308         ' 'Cal 308   ' 'Ammo Weight: 5.0 lbs  Amount:30') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[1]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 3: H&K HK416       ' 'Cal:5.56  ' 'Ammo Weight: 1.5 lbs  Amount:30') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[2]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 4: H&K HK417       ' 'Cal:7.62  ' 'Ammo Weight: 7.0 lbs  Amount:30') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[3]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 5: .44             Cal:.44   Ammo Weight: 4.5 lbs  Amount:25') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[4]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 6: .45 ACP         Cal:.45   Ammo Weight: 4.5 lbs  Amount:25') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[5]
                    return weapons_pick()
                elif player.amount_of_ammo.count( 'Ammo 7: .357            Cal:.357  Ammo Weight: 4.0 lbs  Amount:25') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[6]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 8: .50             Cal:.50   Ammo Weight: 6.0 lbs  Amount:25') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[7]
                    return weapons_pick()
                elif player.amount_of_ammo.count('Ammo 9: 9mm            Cal:9mm   Ammo Weight: 3.5 lbs  Amount:30') > 4:
                    print "you have too much of %r ammo" % player.amount_of_ammo[8]
                    return weapons_pick()


        print "\n\n"
        print "To pick from the riffle rack type 'R' "
        print "To pick from the gun rack type 'G' "
        print "To pick from the knive rack type 'K' "
        print "To get ammo from the ammo locker type 'A' "
        print "To check what is in your weapons bag type 'B'"
        print "Now pick your weapons, sissy:"
        print "when done in weapons room press 'D'"
        weap_pick = raw_input(prompt)
        print "\n"
        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print (r"//////////////////////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

        if weap_pick == 'k' or weap_pick== 'K':
            if len(player.weapon) > 4:
                print "you have too many weapons"
                print "look in your bag and remove some weapons"
                return weapons_pick()

            print "Knife Rack"
            print "\n"
            for k in knives:
                print k

            print "To add weapon type in its number"
            w_pick = raw_input(prompt)
            if w_pick == '1':
                player.weapon.append(knives[0])
            elif w_pick =='2':
                player.weapon.append(knives[1])
            elif w_pick == '3':
                player.weapon.append(knives[2])
            elif w_pick == '4':
                player.weapon.append(knives[3])
            elif w_pick == '5':
                player.weapon.append(knives[4])
            else:
                print "invalid choice"
                return weapons_pick()

            for w in player.weapon:
                print w
            return weapons_pick()

        elif weap_pick == 'a' or weap_pick == 'A':
            if len(player.weapon) > 4:
                print "you have too many weapons"
                print "look in your bag and remove some weapons"
                return weapons_pick()

            for a in Ammo:
                print a
            print "To add ammo type in its number"
            w_pick = raw_input(prompt)
            if w_pick   == '1':
                player.amount_of_ammo.append(Ammo[0])
            elif w_pick == '2':
                player.amount_of_ammo.append(Ammo[1])
            elif w_pick == '3':
                player.amount_of_ammo.append(Ammo[2])
            elif w_pick == '4':
                player.amount_of_ammo.append(Ammo[3])
            elif w_pick == '5':
                player.amount_of_ammo.append(Ammo[4])
            elif w_pick == '6':
                player.amount_of_ammo.append(Ammo[5])
            elif w_pick == '7':
                player.amount_of_ammo.append(Ammo[6])
            elif w_pick == '8':
                player.amount_of_ammo.append(Ammo[7])
            elif w_pick == '9':
                player.amount_of_ammo.append(Ammo[8])
            else:
                print "invalid choice"
                return weapons_pick()
            player.amount_of_ammo.sort()
            ammo_count()
            for a in player.amount_of_ammo:
                print a
            return weapons_pick()

        elif weap_pick == 'r' or weap_pick == 'R':
            if len(player.weapon) > 4:
                print "you have too many weapons"
                print "look in your bag and remove some weapons"
                return weapons_pick()

            print "Riffle Rack\n"
            for r in riffle:
                print r

            print "To add weapon type in its number"
            w_pick = raw_input(prompt)
            if w_pick == '1':
                player.weapon.append(riffle[0])
            elif w_pick =='2':
                player.weapon.append(riffle[1])
            elif w_pick == '3':
                player.weapon.append(riffle[2])
            elif w_pick == '4':
                player.weapon.append(riffle[3])
            elif w_pick == '5':
                player.weapon.append(riffle[4])
            else:
                print "invalid choice"
                return weapons_pick()
            for w in player.weapon:
                print w
            return weapons_pick()
        elif weap_pick == 'g' or weap_pick == 'G':
            if len(player.weapon) > 4:
                print "you have too many weapons"
                print "look in your bag and remove some weapons"
                return weapons_pick()

            print "Gun Rack\n"
            for g in guns:
                print g
            print "To add weapon type in its number"
            w_pick = raw_input(prompt)
            if w_pick == '1':
                player.weapon.append(guns[0])
            elif w_pick =='2':
                player.weapon.append(guns[1])
            elif w_pick == '3':
                player.weapon.append(guns[2])
            elif w_pick == '4':
                player.weapon.append(guns[3])
            elif w_pick == '5':
                player.weapon.append(guns[4])
            else:
                print "invalid choice"
                return weapons_pick()

            for w in player.weapon:
                print w
            return weapons_pick()
        elif weap_pick == 'b' or weap_pick == 'B':
            weapons_bag()
        elif weap_pick == 'd' or weap_pick == 'D':
            ammo_count()
            if player.weapon and not player.amount_of_ammo:
                print "you do not have any ammo"
            print "\nyou are done in weapons room\n"

        else:
            print "invalid choice"
            return weapons_pick()

    weapons_pick()
    
destiny()


def fleet_or_foot():
    global player

    vehicle = player.vehicle
    truck = zombie_classes.Garage.truck
    motorcycle = zombie_classes.Garage.Motorcycle
    car = zombie_classes.Garage.Car

    print "\nYou have picked your weapons and now you are ready to get out of there"
    print "you see the house next to you starting to burn and hear screams that are too close for comfort"
    print "now you have to decide how you are going to make it to the marina by foot or on a vehicle"
    print "\nto go by foot press '1' to leave on a vehicle press '2'"
    wheel_or_feet = raw_input(prompt)

    if wheel_or_feet == '1':
        foot = zombie_classes.foot_fault()
        exit()
    elif wheel_or_feet == '2':
        print "You've chosen to take a vehicle to get to the marina, so you head to"
        print "the garage, in there you see various vehicles\n\n"

        print "Trucks:"
        for v in truck:
            print v
        print "\n"
        print "Motorcycles:"
        for m in motorcycle:
            print m
        print "\n"
        print "Sport Cars:"
        for c in car:
            print c
        print "\n\n"
        print "to choose a vehicle type in its number"
        v_choice = raw_input(prompt)


        if v_choice == '1':
            player.vehicle.append(truck[0])
        elif v_choice == '2':
            player.vehicle.append(truck[1])
        elif v_choice == '3':
            player.vehicle.append(motorcycle[0])
        elif v_choice == '4':
            player.vehicle.append(motorcycle[1])
        elif v_choice == '5':
            player.vehicle.append(car[0])
        elif v_choice == '6':
            player.vehicle.append(car[1])
        else:
            print "Invalid choice"
            return fleet_or_foot()

        print "You chose",player.vehicle[0]
        if len(player.weapon) == 0:
            nw_death = zombie_classes.no_weapons_death()
            exit ()
    else:
        print "please make valid choice"
        return fleet_or_foot()

fleet_or_foot()


#:all vehicles converge on airport, must make stories for other vehicles that made it through

def peninsula_flee():
    global player
    vehicle = player.vehicle
    truck = zombie_classes.Garage.truck
    motorcycle = zombie_classes.Garage.Motorcycle
    car = zombie_classes.Garage.Car


    if player.Name == 'Anna' or player.Name == 'Victor':
        if player.vehicle [0] == motorcycle[0] or player.vehicle[0] == motorcycle[1]:
            m_death = zombie_classes.motor_death()
            return open()
        else:
            v_ditch = zombie_classes.vehicle_ditch()
    elif player.Name == 'Gabriel' and player.vehicle == motorcycle[1]:
        gab_death = zombie_classes.gabriel_m_death()
    elif player.Name == 'Gabriel' and player.prime_vehicle == player.vehicle[0]:
        g_hop = zombie_classes.gabriel_hop()
    elif player.prime_vehicle[0] == player.vehicle[0]:
        zombie_classes.flee()
        return the_airport()
    else:
        v_ditch = zombie_classes.vehicle_ditch()

peninsula_flee()


def l_mod(partial):
    #:Which desicions are forced and which are not ?
    #:Probably need to make it a class to access methods and attributes
    #:!Display weapons and ammo that I have
    #:!Let me pick a weapon
    #:!!!!()Must check the type of weapon picked first; firearm or knife
    #:!Count amount of ammo I have
    #:!Check that ammo and weapon caliber match but not tell me
    #:!Check that ammo and weapon caliber match
    #:!Amount of ammo I have
    #:~!if I have only one firearm and no ammo or wrong ammo then die anytime facing z's
    #:~!if I have only a knife display that use that and return or start fighting
    #:~!if I have only one firearm and ammo for that and use that til ammo runs out
    #:~!If wep picked == no/wrong ammo and all weps == wrong/no ammo
    #:    but I have one knife --> default to knife
    #:!If I only have multiple knives then allow to switch weapons
    #:!If I only have multiple firearms
    #:!if wep picked == no ammo and have k's and weps but no ammo match
    #:    then show viable knives and allow to switch
    #:!If wep picked == no ammo and other weps == viable ammo
    #:     and no knives warn and show viable weps and allow to switch
    #:if wep picked == no ammo and I have mutiple  available caliber and knives?
    #:!Load weapon initially


    global player
    global weapon
    global caliber
    global prompt
    global knives
    global viable_firearm
    global viable_firearms
    global active_weapon
    global mag_count
    weapon  = 0
    active_weapon = []


    #:Shows weapons and type of ammo available
    def weapons_display(out_of_ammo):

        #:This displays the knives in inventory only
        if out_of_ammo == 1:
            print "your only viable weapons are these"
            #.This would work faster and better player.weapon[:] = [x for x if 'Knife' not in x ]"
            for x in player.weapon[:]:
                if 'Knife' not in x:
                    player.weapon.remove(x)
            for x in player.weapon:
                print x
            return

        #:This displays all available weapons
        print "Your weapons:"
        for w in player.weapon:
            print w

        #:Displays ammo from caliver[] Dictionary instead
        if partial == 3:
            if caliber:
                cat = 0
                for k,v in caliber.iteritems():
                    if v > 0 :
                        cat = 1
                        break
                if cat == 1:    
                    print "\n\nYour Ammo:"
                if cat == 0:
                    print "\n\nYou have no ammo for any of your weapons"
                for k,v in caliber.iteritems():
                    if v > 0 :
                        print k, 'Amount:', v
                print "\n"
        if player.amount_of_ammo and partial == 0:
            print "\n\nYour ammo"
            for a in player.amount_of_ammo:
                print a
            print "\n"

    weapons_display(0)

    #:weapon_pick has been passed inside the func   tion up top
    #:appends to active weapon the weapon you chose
    def weapon_pick():

            print "\nto pick a weapon type in its number, for example for the first weapon press '1'"
            weapon_pick = raw_input(prompt)
            if weapon_pick == '1' and len(player.weapon) >= 1:
                active_weapon.append(player.weapon[0])
            elif weapon_pick == '2' and len(player.weapon) >= 2:
                active_weapon.append(player.weapon[1])
            elif weapon_pick == '3' and len(player.weapon) >= 3:
                active_weapon.append(player.weapon[2])
            elif weapon_pick == '4' and len(player.weapon) >= 4:
                active_weapon.append(player.weapon[3])
            elif weapon_pick == '5' and len(player.weapon) >= 5:
                active_weapon.append(player.weapon[4])
            else :
                print "please make a valid choice\n\n"
                return l_mod(0)

            print "\n"
            return active_weapon
            print "\n"
    weapon_pick()


    #:makes a list from the knives in player.weapon in case of multiple knives
    def knife_attack():
        global knives
        knives = []

        for x in player.weapon:
            if 'Knife' in x:
                knives.append(x)
        return knives
    knife_attack()


    #:Below adds all the ammo per caliber, if available 'saves' sum total
    def ammo_load():
        global caliber
        caliber = {
         'Cal:5.56 M ' : 0,
         'Cal:308    ' : 0,
         'Cal:5.56   ' : 0,
         'Cal:7.62   ' : 0,
         'Cal:.44    ' : 0,
         'Cal:.45 ACP' : 0,
         'Cal:.357   ' : 0,
         'Cal:.50    ' : 0,
         'Cal: 9mm   ' : 0,}
        if player.amount_of_ammo:
            for a in player.amount_of_ammo:
                if   'Ammo 1:' in a:
                    caliber['Cal:5.56 M '] +=200
                elif 'Ammo 2:' in a:
                    caliber['Cal:308    '] +=30
                elif 'Ammo 3:' in a:
                    caliber['Cal:5.56   '] +=30
                elif 'Ammo 4:' in a:
                    caliber['Cal:7.62   '] +=30
                elif 'Ammo 5:' in a:
                    caliber['Cal:.44    '] +=25
                elif 'Ammo 6:' in a:
                    caliber['Cal:.45 ACP'] +=25
                elif 'Ammo 7:' in a:
                    caliber['Cal:.357   '] +=25
                elif 'Ammo 8:' in a:
                    caliber['Cal:.50    '] +=25
                elif 'Ammo 9:' in a:
                    caliber['Cal: 9mm   '] +=30

        return caliber
    #:####bypass this with 'partial' variable this fixes the double ammo counting
    if partial == 0 :
        ammo_load()

    #:Below appends to wammo_type the caliber of the weapons in your bag
    wammo_type = []
    if player.weapon:
        for x in player.weapon:
            if 'Riffle' in x :
                wammo_type.append(x[54:65])
            if 'Gun' in x:
                wammo_type.append(x[36:47])
    #:Below appends to ammo_type the caliber of the ammo in your bag
    ammo_cal = []
    #b_cal = []
    if caliber:
        for k,v in caliber.iteritems():
            if v > 0 :
                ammo_cal.append(k)
    '''
    if player.amount_of_ammo:
        for a in player.amount_of_ammo:
            if 'Cal' in a:
                b_cal.append(a[24:35])
     for x in b_cal:
        print "this is player amount ...%r" % x
     for x in ammo_cal:
        print "this is dic Cal ammo cal %r" % x
    '''

    #:Function makes caliber set_list of weapon that has available ammo
    wep_n_cal = []
    def w_and_a_check(wep_n_cal,wammo_type,ammo_cal):
        wep_set = set(wammo_type)
        cal_set = set(ammo_cal)
        wep_n_cal = wep_set & cal_set
        return wep_n_cal

    #:Calls function that checks and returns caliber of weapon and ammo available
    weapons_and_caliber = w_and_a_check(wep_n_cal,wammo_type,ammo_cal)

    #:checks that weapon picked has ammo returns viable_firearm
    def ammo_availability():
        global viable_firearm
        #:availability is the weapon that was picked
        #:Check what availability is for ...?
        availability = []
        if active_weapon:
            for x in active_weapon:
                if 'Riffle' in x :
                    availability.append(x[54:65])
                if 'Gun' in x:
                    availability.append(x[36:47])
        active_set = set(availability)
        ammo_x_set = set(weapons_and_caliber)
        viable_firearm = active_set & ammo_x_set
        return viable_firearm

    #:Calls ammo_availability and returns viable_firearm
    ammo_availability()

    #:Function that returns viable firearms
    def vi_firearms(weapons_and_caliber):
        #:I need a function that takes all the firearms in inventory
        #:and replaces it with a list of weapons that have ammo,
        #:i.e. viable firearms
        global viable_firearms
        viable_firearms = []
        for w in weapons_and_caliber:
            for p in player.weapon:
                if w in p:
                    viable_firearms.append(p)

        return viable_firearms

    #:Calls vi_firerms function and returns viable_firearms / plural
    vi_firearms(weapons_and_caliber)


    '''
    if knives:
        print "we have liftoff and knives"
        elif not knives:
        print "we were left behind with no knives"
        if viable_firearm:
        print "we have bang bang"
        elif not viable_firearm:
        print "no blood no bang bang"
        if viable_firearms:
        print "we have multiple firearms"
        elif not viable_firearms:
        print "we don't have a whole bunch"
        if weapons_and_caliber:
        print "we have weapons and calibers"
        elif not weapons_and_caliber:
        print "we don't have cals or weps"
    '''
    #:~if only one firearm, no knife and wrong or no ammo then I die
    if len(player.weapon) == 1:
        for x in player.weapon:
            if not weapons_and_caliber and not knives:
                print "you have the wrong ammo or no ammo for your firearm and no knife"
                print "the zombies grab ya, they bite ya and you die"
                print "yuuummmyyy"
                exit()


    #:if several firearms,wrong or no ammo and no knife then I die
    if len(player.weapon) > 1:
        for x in player.weapon:
            if not knives and not weapons_and_caliber :
                print "you have the wrong ammo or no ammo for your firearm and no knife"
                print "the zombies grab ya, they bite ya and you die"
                print "yuuummmyyy"
                exit()


    #:~If I only have a knife
    if len(player.weapon) == 1:
        for x in player.weapon:
            if 'Knife' in x:
                print "Your only weapon is a knife"
                print "your weapon is"
                print active_weapon[0]
                print "\n"
                return


    #:~If only have one firearm and proper ammo then return and fight
    if len(player.weapon) == 1:
        for x in player.weapon:
            if 'Gun' in x or 'Riffle' in x:
                if weapons_and_caliber:
                    print "You have only one firearm"
                    print "Your weapons is"
                    print active_weapon[0]

    #:If I have viable weapons and knifes
    if knives and viable_firearms:
        if active_weapon:
            print "your weapon is: "
            print active_weapon[0]
            print "\n"


    #:~If wep picked == no/wrong ammo and all weps == wrong/no ammo
    #:    but I have one knife --> default to knife
    for x in active_weapon:
        if not viable_firearm and not weapons_and_caliber and ('Gun' in x or 'Riffle' in x):
                if len(knives) == 1 and len(player.weapon) > 1:
                    active_weapon = []
                    print "you have no ammo or the wrong ammo for all of your firearms"
                    print "your weapon is now"
                    print knives[0]
                    print "\n"
                    active_weapon.append(knives[0])


    #:if I only have multiple knives then allow me to change weapon if desired
    if len(knives) > 1 and not wammo_type:
        print "your weapon is"
        print active_weapon[0]
        print "to switch weapon press '1' to use weapon press '2'"
        switch_or_use = raw_input(prompt)
    #:this checks the desicion to switch or to use weapon
        if switch_or_use == '1':
            return l_mod(0)
        elif switch_or_use == '2':
            return


    #:If only firearms and no knives
    for x in active_weapon:
        if not knives and not viable_firearm and viable_firearms:
            active_weapon = []
            print "\n\nthe firearm you chose has no or the wrong bullets"
            print "these are your viable firearms\n"
            for x in viable_firearms:
                print x
            print "\n"
            print "To pick a weapon type in its number for example for the first weapon"
            print "type in '1' for the second weapon type in '2'"
            weapons_pick = raw_input(prompt)
            if weapons_pick == '1':
                active_weapon.append(viable_firearms[0])
            elif weapons_pick == '2':
                active_weapon.append(viable_firearms[1])
            elif weapons_pick == '3':
                active_weapon.append(viable_firearms[2])
            else:
                print "Please make a valid choice"
                return l_mod(0)
            print "your weapon is"
            print active_weapon[0]
            print "\n"
            return
        if not knives and viable_firearm and viable_firearms:
            print "your weapon is"
            print active_weapon[0]
            print "\n"

    #: ########################################################
    '''
    if knives:
        print "we have liftoff and knives"
        elif not knives:
        print "we were left behind with no knives"
        if viable_firearm:
        print "we have viable firearm"
        elif not viable_firearm:
        print "not a viable firearm"
        if viable_firearms:
        print "we have multiple viable firearms"
        elif not viable_firearms:
        print "we don't have a whole bunch"
        if weapons_and_caliber:
        print "we have weapons and calibers"
        elif not weapons_and_caliber:
        print "we don't have cals or weps"
    '''
    #: ########################################################
    #:if wep picked == no ammo and have 'k's' and weps but no ammo
    #:    match then show viable knives and allow to switch
    #:This checks that we have multiple knives
    for x in active_weapon:
        if not weapons_and_caliber and knives and ('Gun' in x  or 'Riffle' in x):
            print "you have no ammo that matches any of your firearms"
            active_weapon = []
            weapons_display(1)
            weapon_pick()
            #:At this point knives have been displayed and picked now return to fight
            print "your weapon is"
            print active_weapon[0]
            print "\n"
            return


    #:if wep picked == no ammo, and other weps == viable ammo and no knives
    #:    show viable weps and allow to switch
    #:The following checks that you picked a firearm and that there are other viable weapons
    for x in active_weapon:
        if not knives and not viable_firearm and viable_firearms and ('Gun'in x or 'Riffle' in x):
            active_weapon = []
            print "The firearm you picked has no ammo--"
            print "These are your viable firearms\n\n"

            #:this calls viable_firearms function trough weapons_display
            for x in viable_firearms:
                print x

            print "To pick a weapon type in its number for example for the first weapon"
            print "type in '1' for the second weapon type in '2'"
            weapons_pick = raw_input(prompt)
            if weapons_pick == 1:
                active_weapon.append(viable_firearms[0])
            elif weapons_pick == 2:
                avtive_weapon.append(vialbe_firearms[1])
            elif weapons_pick == 3:
                avtive_weapon.append(vialbe_firearms[2])
            elif weapons_pick == 4:
                avtive_weapon.append(vialbe_firearms[3])

            print "your weapon is"
            print active_weapon[0]
            print "\n"
            return


    #:If firearm picked == no ammo and have viable firearms and knives
    #:    show viable firearms and knives and allow to change into those
    #:Check that the weapon picked has no ammo
    #:check that we have viable weapons and multiple knives
    for x in active_weapon:
        if knives and viable_firearms and not viable_firearm and ('Gun' in x or 'Riffle' in x) :
            #:This clears the original list of weapons and updates it with the viable ones
            player.weapon = []
            for x in viable_firearms:
                player.weapon.append(x)
            for x in knives:
                player.weapon.append(x)

            active_weapon = []
            print "the firearm you picked has no ammo**"
            print "these are your viable weapons\n\n"
            weapons_display(0)
            print "To pick a weapon type in its number for example for the first weapon"
            print "type in '1' for the second weapon type in '2'"
            weapons_pick = raw_input(prompt)
            if weapons_pick == '1':
                active_weapon.append(player.weapon[0])
            elif weapons_pick == '2':
                active_weapon.append(player.weapon[1])
            elif weapons_pick == '3':
                active_weapon.append(player.weapon[2])
            elif weapons_pick == '4':
                active_weapon.append(player.weapon[3])
            else:
                print "Please make a valid choice"
                return weapons_mod
            print "your weapon is"
            print active_weapon[0]
            print "\n"


    #:Changes weapons_and_ammo from a set to a list
    weapons_and_ammo = list(viable_firearm)
    #:Function returns index of caliber in list
    def ammo_index(cal):
        for x in player.amount_of_ammo:
            if  cal in x:
                cal_index = player.amount_of_ammo.index(x)
        return cal_index
    if weapons_and_ammo:
        mag_count = 0
    #:Weapons_loader Caliber[] Subtractor clears player.amount of ammo box when appropriate
    #:at the moment only a few boxes of ammo are poped off
    def weapons_loader(ammo_index):
        global mag_count
        if '5.56 M' in weapons_and_ammo[0]:
            caliber['Cal:5.56 M '] -= 200
            #:ammo_index = player.amount_of_ammo.index('Cal:5.56 M')
            cal = ('Cal:5.56 M')
            ammo_index = ammo_index('Cal:5.56 M')
            player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 200
        elif '308' in weapons_and_ammo[0]:
            caliber['Cal:308    '] -= 4
            #:ammo_index = player.amount_of_ammo.index('Cal:308')
            cal = ('Cal:308')
            ammo_index = ammo_index('Cal:308')
            #:Belox comes in box of 25
            #!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 4
        elif '5.56' in weapons_and_ammo[0]:
            caliber['Cal:5.56   '] -= 30
            #:ammo_index = player.amount_of_ammo.index('Cal:5.56')
            cal = ('Cal:5.56')
            ammo_index = ammo_index('Cal:5.56')
            player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 30
        elif '7.62' in weapons_and_ammo[0]:
            caliber['Cal:7.62   '] -= 20
            #:ammo_index = player.amount_of_ammo.index('Cal:7.62')
            cal = ('Cal:7.62')
            ammo_index = ammo_index('Cal:7.62')
            #:Below comes in box of 30
            #!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 20
        elif '.44' in weapons_and_ammo[0]:
            caliber['Cal:.44    '] -= 6
            #:ammo_index = player.amount_of_ammo.index('Cal:.44')
            cal = ('Cal:.44')
            ammo_index = ammo_index('Cal:.44')
            #:Belox comes in box of 25
            #!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 6
        elif '.45 ACP' in weapons_and_ammo[0]:
            caliber['Cal:.45 ACP'] -= 9
            #:ammo_index = player.amount_of_ammo.index('Cal:.45 ACP')
            cal = ('Cal:.45 ACP')
            ammo_index = ammo_index('Cal:.45 ACP')
            #:Belox comes in box of 25
            #:!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 9
        elif '.357' in weapons_and_ammo[0]:
            caliber['Cal:.357   '] -= 13
            #:ammo_index = player.amount_of_ammo.index('Cal:.357')
            cal = ('Cal:.357')
            ammo_index = ammo_index('Cal:.357')
            #:Belox comes in box of 25
            #!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 13
        elif '.50' in weapons_and_ammo[0]:
            caliber['Cal:.50    '] -= 7
            #:ammo_index = player.amount_of_ammo.index('Cal:.50 ')
            cal = ('Cal:.50 ')
            ammo_index = ammo_index('Cal:.50')
            #:Belox comes in box of 25
            #!!!player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 7
        elif '9mm' in weapons_and_ammo[0]:
            caliber['Cal: 9mm   '] -= 30
            #:ammo_index = player.amount_of_ammo.index('Cal: 9mm')
            cal = ('Cal: 9mm')
            ammo_index = ammo_index('Cal: 9mm')
            player.amount_of_ammo.pop(ammo_index)
            mag_count = mag_count + 30
        return player.amount_of_ammo
    for x in active_weapon:
        if 'Knife' not in x:
            weapons_loader(ammo_index)

def zombie_engine():
    global player
    global weapon
    global caliber
    global prompt
    global knives
    global zombie_count
    global viable_firearm
    global viable_firearms
    global p_amount_of_ammo
    global mag_count
    global active_weapon
    global weapons_and_ammo
    global stamina
    global weapons_switch
    global partial
    weapons_switch = 0
    #:####!GLOBALS!#####
    '''
     #:global check naming it global here did not work
     #:However naming it conventionally here and using or calling it global inside the
     #:Function did work
     #:Name_Space Works DiFerently inside a function when using global's
     #:It lOokS liKe you hAvE tO use global twice when working with a function inside a function
     global color
     color = 'red'
     print "the color pre func is %s" % color
     def f_color():
        global color
        print "the color inside func is %s" % color
        print "now i'm setting color to 'blue'"
        color  = 'blue'
        print "the color is now %s" % color
     f_color()
     p rint "after f_color() color is %s" % color
    '''
    #.!Check for the type of weapon being used and determine weather its a players
    #   prime, semi or non prime weapon
    #:!Zombies are Easy Medium or Hard depending on 'active_weapon
    #.!Ammo Counter
    #:!Counting down the amount of zombies
    #:!Counting down the amount of stamina
    #:!Make stamina ammo does not go negative if they go to zero you die on zero or on
    #:!    whatever zombie takes you to zero and lower
    #:!Remeber that the machinegun fires off more rounds then regular firearms

    print #:########################################################################################
	
    #.check which type of weapon you are using
    for x in active_weapon:
        if 'Gun' in x :
            weapon = 'Gun'
            print "so you picked a gun to fight the hordes"
        elif 'Riffle' in x:
            weapon = 'Riffle'
            print "so you've picked a riffle to kill the ghouls"
        elif 'Knife' in x:
            mag_count = 0
            weapon = 'Knife'
            print "So you have picked a blade to decimate the unrighteous ones, quite brave"

    stamina = player.Stamina_Points
    weak_z_range = zombie_classes.Zombie_Mod.Weak()
    medium_z_range = zombie_classes.Zombie_Mod.Medium()
    strong_z_range = zombie_classes.Zombie_Mod.Strong()


    Zombies = 0
    for p in player.prime_weapons:
        for x in active_weapon:
            if x in p:
                Zombies = 'Weak'
    for s in player.semi_prime:
        for x in active_weapon:
            if x in s:
                Zombies = 'Medium'
    for x in active_weapon:
        for p in player.prime_weapons:
            if x in p:
                break
        for s in player.semi_prime:
            if x in s:
                break
            elif s not in x and not Zombies:
                Zombies = 'Strong'

    #:Ammo Access and Counter
    #:mag_count is an int
    mag_cap = mag_count #This is the ammo capacity the active weapon holds
    if weapon == 'Gun' or weapon == 'Riffle':
        for w in active_weapon:
            for w_cal in caliber:
                if w_cal in w:
                    #:At this point ammo is the index-name in the dictionary caliber
                    ammo_in_bag = w_cal
                    break
        print "you have %s, rounds loaded" % mag_count
        #:This turns the value of the caliber dictionary index into a number
        ammo = caliber[ammo_in_bag]
        print "rounds in bag for this weapon %s" % caliber[ammo_in_bag]
    if partial < 3:
        print "Your stamina is %s " % stamina
    if partial == 3:
        print "let the slaughter continue"
    print "there are %r zombies" % zombie_count
    print "zombie strength is %s\n" % Zombies


    #:put bullets back in magazine when switching weps and at end of battle if left over
    def active_ammo_in_bag(mag_count,kill_range):
        global weapons_switch
        m_and_b_count = {'mag_count':0 ,'bag_count':0 }
        k_diff = kill_range - mag_count
        #:If some rounds in mag and enough in bag to complete kill
        if mag_count > 0 and caliber[ammo_in_bag] >= k_diff:
            print "the last %d rounds where not enough to kill the zombie" % mag_count
            print "you do a quick re-load and shoot some more"
            if caliber[ammo_in_bag] >= mag_cap:
                m_and_b_count['bag_count'] = caliber[ammo_in_bag] - mag_cap
                m_and_b_count['mag_count'] = mag_cap
                m_and_b_count['mag_count'] = m_and_b_count['mag_count'] - k_diff
                print "that thing is dead now"
                return m_and_b_count
            #:If I m_count + b_count = complete kill    
            elif caliber[ammo_in_bag] == k_diff:
                m_and_b_count['bag_count'] = 0
                m_and_b_count['mag_count'] = caliber[ammo_in_bag]
                m_and_b_count['mag_count'] = m_and_b_count['mag_count'] - k_diff
                print "mag should be zero %d" % m_and_b_count['mag_count']
                print "yep that did it"
                return m_and_b_count
                
        mag_count = 0  #This sets the weapon to zero so it doesn't go into negatives

        #:if no ammo for weapon in mag or bag only choice is to change weapon
        if mag_count == 0 and caliber[ammo_in_bag] == 0:
            print "You have run out of ammo for this weapon"
            weapons_switch = '2'
            return m_and_b_count
        
        #:This checks if the zombie is going to run ammo down to zero or lower
        if mag_count <= kill_range and caliber[ammo_in_bag] > 0:
            print "you mag is out of ammo"
            print "and the zombies are still coming at ya"
            print "to re-load weapon press '1' to switch weapon press '2'"
            switch_and_load = raw_input(prompt)
            #active weapons reload
            if switch_and_load == '1' and caliber[ammo_in_bag] > mag_cap:
                if caliber[ammo_in_bag] > mag_cap:
                    print "You fully re-load the weapon as fast as you can"
                    print "and start shooting"
                    m_and_b_count['bag_count'] = caliber[ammo_in_bag] - mag_cap
                    m_and_b_count['mag_count'] = mag_cap
                    m_and_b_count['mag_count'] = m_and_b_count['mag_count'] - kill_range
                #:Is this enough to kill zombie
                elif caliber[ammo_in_bag] < mag_cap and caliber[ammo_in_bag] > 0:
                    print "these are the last bullets for this weapon"
                    print "you shoot hoping they will kill the zombie"
                    m_and_b_count['bag_count'] = 0
                    m_and_b_count['mag_count'] = caliber[ammo_in_bag]
                    if m_and_b_count['mag_count'] >= kill_range:
                        m_and_b_count['mag_count'] = m_and_b_count['mag_count'] - kill_range
                        print "fate is in your favor today the deadite falls"
                    else:
                        print "the last bullets in your weapon were not enough to kill the walker"
                        m_and_b_count['mag_count'] = 0
            elif switch_and_load == '2' :            
                print "\n\nyou chose to switch weapons"
                weapons_switch = '2'
                m_and_b_count['bag_count'] = caliber[ammo_in_bag]
                return m_and_b_count
        return m_and_b_count

     #Stamina killer
    def stamina_killer():
        if stamina <= 0:
            print "all the zombies took their toll on you"
            print "and for this sin you die"
            exit()
            

    #Machine Gun Ranges
    def m_g_range():
        ma_range = 'cat'

        for x in active_weapon:
            if '9mm' not in x and '5.56' not in x:
                return 
            if '5.56 M' in x:
                wep = '5.56 M'
            elif '9mm' in x:
                wep = '9mm'
            else:
                wep = 0
        
        if player.Name == 'Anna' and wep == '9mm':
            ma_range = random.randint(3, 5)
        elif player.Name == 'Victor' and wep == '5.56 M' :
            ma_range = random.randint(5, 9)
        elif '9mm' in wep and (player.Name == 'Victor' or player.Name == 'Gabriel'):
            ma_range = random.randint(7, 11)
        elif wep == '5.56 M' and (player.Name == 'Gabriel' or player.Name == 'Anna'):
            ma_range = random.randint(15, 18)
        else:
            wep = 0
        return ma_range
    m_range = m_g_range()
    
    if weapon == 'Gun' or weapon == 'Riffle':
        print "You start shooting"
    #:Weak Zombies
    if Zombies == 'Weak' and weapon == 'Gun':
        for z in range(zombie_count):
            if m_range:
                kill_range = m_range
            elif not m_range:
                kill_range = weak_z_range.h_g_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= weak_z_range.h_g_range:
                mag_count = mag_count - kill_range
            #:This checks if the zombie is going to run ammo down to zero or lower
            elif mag_count <= weak_z_range.h_g_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
                if weapons_switch == '2':
                    partial = 3
                    print "there are %r zombies left \n\n" % zombie_count
                    return
            print "here isyou killed a zombie "
            zombie_count = zombie_count - 1
        stamina = stamina - weak_z_range.h_g_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds left in weapon" % mag_count
        print "your stamina is now %s" % stamina
    elif Zombies == 'Weak' and weapon == 'Knife':
        for z in range(zombie_count):
            print "you stabbed and killed a zombie"
        zombie_count = zombie_count - 1
        stamina = stamina - weak_z_range.k_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "Your Stamina is now %s" % stamina
    elif Zombies == 'Weak' and weapon == 'Riffle':
        for z in range(zombie_count):
            if m_range:
                kill_range = m_range
            elif not m_range:
                kill_range = weak_z_range.r_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= weak_z_range.r_range:
                mag_count = mag_count - kill_range
            #:This checks if the zombie is going to run ammo down to zero or lower
            elif mag_count <= weak_z_range.r_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
            if weapons_switch == '2':
                partial = 3
                print "there are %r zombies left \n\n" % zombie_count
                return
            print "here isyou killed a zombie "
            zombie_count = zombie_count - 1
            #print "mag count outside of func is now %d" % mag_count
        stamina = stamina - weak_z_range.r_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds in weapon" % mag_count
        print "your stamina is now %s" % stamina
    #:Medium Zombies
    if Zombies == 'Medium' and weapon == 'Gun':
        for z in range(zombie_count):
            kill_range = medium_z_range.h_g_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= medium_z_range.h_g_range:
                mag_count = mag_count - medium_z_range.h_g_range
            #:This checks if the zombie is going to run ammo down to zero or lower
            elif mag_count <= medium_z_range.h_g_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
            if weapons_switch == '2':
                partial = 3
                print "there are %r zombies left \n\n" % zombie_count
                return
            print "here isyou killed a zombie "
            zombie_count = zombie_count - 1
        stamina = stamina - medium_z_range.h_g_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds in weapon" % mag_count
        print "your stamina is now %s" % stamina
    elif Zombies == 'Medium' and weapon == 'Knife':
        for z in range(zombie_count):
            print "you slashed and killed a zombie"
            zombie_count = zombie_count - 1
        stamina = stamina - medium_z_range.k_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "Your Stamina is now %s" % stamina
    elif Zombies == 'Medium' and weapon == 'Riffle':
        for z in range(zombie_count):
            kill_range = medium_z_range.r_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= medium_z_range.r_range:
                mag_count = mag_count - medium_z_range.r_range 
            #:This checks if the zombie is going to run ammo down to zero or lower
            elif mag_count <= medium_z_range.r_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
            if weapons_switch == '2':
                partial = 3
                print "there are %r zombies left \n\n" % zombie_count
                return
            print "here isyou killed a zombie "
            zombie_count = zombie_count - 1
        stamina = stamina - medium_z_range.r_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds in weapon" % mag_count
        print "your stamina is now %s" % stamina
    #:Strong Zombies
    if Zombies == 'Strong' and weapon == 'Gun':
        for z in range(zombie_count):
            if m_range:
                kill_range = m_range
            elif not m_range:
                kill_range = strong_z_range.h_g_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= strong_z_range.h_g_range:
                mag_count = mag_count - strong_z_range.h_g_range
            #:This checks if zombie is going to run ammo down to zero or lower
            elif mag_count <= strong_z_range.h_g_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
            if weapons_switch == '2':
                partial = 3
                print "there are %r zombies left \n\n" % zombie_count
                return
            print "you killed a zombie\n...    ...    ... " 
            zombie_count = zombie_count - 1
        stamina = stamina - weak_z_range.r_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."        
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds in weapon" % mag_count
        print "your stamina is now %s" % stamina
    elif Zombies == 'Strong' and weapon == 'Knife':
        for z in range(zombie_count):
            print "you slashed and killed a zombie"
            zombie_count = zombie_count - 1
        stamina = stamina - strong_z_range.h_g_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."
        print "Your stamina is now %s" % stamina
    elif Zombies == 'Strong' and weapon == 'Riffle':
        for z in range(zombie_count):
            if m_range:
                kill_range = m_range
            elif not m_range:
                kill_range = strong_z_range.r_range
            if 1 <= mag_count < 4:
                print "You are about to run out of ammo"
            if mag_count >= strong_z_range.r_range:
                mag_count = mag_count - strong_z_range.r_range
            #:This checks if the zombie is going to run ammo down to zero or lower
            elif mag_count <= strong_z_range.r_range:
                ammo_and_bag_count = active_ammo_in_bag(mag_count,kill_range)
                caliber[ammo_in_bag] = ammo_and_bag_count['bag_count']
                mag_count = ammo_and_bag_count['mag_count']
            if weapons_switch == '2':
               partial = 3
               print "there are %r zombies left \n\n" % zombie_count
               return
            print "here isyou killed a zombie "
            zombie_count = zombie_count - 1
        stamina = stamina - strong_z_range.r_stamina
        stamina_killer()
        print "...    ...    ...    ...    ...    ...    ..."
        print "ammo left in bag for this weapon is now %r" % caliber[ammo_in_bag]
        print "you have %s rounds in weapon" % mag_count
        print "your stamina is now %s" % stamina

    print "the battle has finished"
    if mag_count > 0 and (weapon == 'Riffle'or 'Gun')   :
        caliber[ammo_in_bag] = caliber[ammo_in_bag] + mag_count
        mag_count = 0
        print "all ammo in weapon was returned to your bag"
        print "ammo: %d" % caliber[ammo_in_bag]
    if stamina < 50 > 30:
        print "watch your stamina and pick your weapons wisely"
        
    
def fire_fight():
    global player


    if 'Gun' in player.weapon[0]:
        weapon = 'gun'
    elif 'Riffle' in player.weapon[0]:
        weapon = 'riffle'
    elif 'Knife'  in player.weapon[0]:
        weapon = 'knife'

    f_fight = zombie_classes.the_fire_fight()

    if weapon == 'gun' and player.amount_of_ammo :
        print "and grab your gun"
        print "luckily the weapon is loaded and you shoot its head, the woman goes limp instantly, the adrenaline is flowing"
        print "through you now, you know how lucky yougt ,so you get up and grab your bag, you make your way past the cars"
        print "and the fire, you are happy to see a car dealer ship a few yards away."
    elif weapon == 'riffle':
        print "and grab a riffle"
        print "luckily the weapon is loaded and you shoot its head, the woman goes limp instantly, the adrenaline is flowing"
        print "through you now, you know got lucky, you get up and grab your bag, you make your way past the cars"
        print "and the fire, you are happy to see a car dealer ship a few yards away."
    elif weapon == 'knife':
        print "grab your knife and slash at its head, you miss, and slash again, this time you hit it slash sqare"
        print "in the head and the woman goes limp, quickly you get up and grab your bag, you look down on the woman and"
        print "you feel a mixture of fear and sadness, you feel like letting out a cry but its somewhere in the back of"
        print "your mind. You start to make your way past the cars and the fire, soon the fire is behind you and you see a"
        print "hummvee dealership ahead, you start to make your way towards it"

fire_fight()


def the_dealership():
    global player
    global weapon
    global active_weapon
    global zombie_count
    global stamina
    global partial
    partial = 0
    zombie_count = random.randint(4, 9)

    #:function with 'zombie_count' displays the number of zombies in the upcoming fight
    the_dealership_story = zombie_classes.the_dealership_story(zombie_count)

    shoot_or_run = raw_input(prompt)
    if shoot_or_run == '1':
        print "You choose to fight"
        l_mod(0)
    elif shoot_or_run == '2':
        mad_dash = zombie_classes.mad_dash()
        exit()
    else:
        print "wrong choice"
        return the_dealership()

    zombie_engine()
    if partial == 3:
        l_mod(3)
        zombie_engine()

the_dealership()


def the_airport():
    global player
    global weapon
    global active_weapon
    global zombie_count
    global stamina
    global partial
    partial = 0
    zombie_count = random.randint(4, 9)
    
    
    turbulence_story = zombie_classes.airport_phase()

    shoot_or_run = raw_input(prompt)
    if shoot_or_run == '1':
        print "You choose to fight"
        l_mod(0)
    elif shoot_or_run == '2':
        mad_dash = zombie_classes.mad_dash()
        exit()
    else:
        print "wrong choice"
        return the_airport()

    zombie_engine()
    if partial == 3:
        l_mod(3)
        zombie_engine()
    
the_airport()




















