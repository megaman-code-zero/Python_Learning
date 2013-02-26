# zombie classes
import random

def test():
    print "to access functions or classes you must type in the module name \nfirst  to access its functions and then set variables to names of classes then use\n \'.\' dot notation to access the methods and attributes"

class Avatar():
    class bag(object): 
        weapon = []
        amount_of_ammo = []
        vehicle = []

    class Anna(bag):

        Name =  'Anna'
        Anna_stats     = 'age: 19  Weight: 110 lbs Height 5\'3" Pilates Instructor, former Army medic'
        prime_vehicle  = 'choice 6: Subaru Impreza 2.0L          (Rally Car)          HP 148',
        Health_Points  = 100 
        Stamina_Points = 100
        prime_weapons  = ('Riffle 4:'  'Heckler & Koch HK416 Semi-Automatic          Cal:5.56   ''Weight:  9.05 lbs  Ammo Capacity :30',
                          'Knife 4:' 'Tops Anaconda Tanto            (Big Knife)            Weight: 1.50 lbs Blade  Length:9.5',
                          'Gun 5:' 'Heckler & Koch MP5K           ' 'Cal: 9mm    ' 'Weight: 4.78 lbs ' 'Ammo Capacity :30',)

        semi_prime     = ('Riffle 5:'  'Heckler & Koch HK417 Semi_Automatic          Cal:7.62   ''Weight: 10.93 lbs  Ammo Capacity :20',
                          'Knife 2:' 'ColdSteel  O Katana          (Samurai Sword)          Weight: 3.00 lbs Blade  Length:36.0',
                          'Gun 3:' 'Heckler & Koch P2000SK V2     ' 'Cal:.357    ' 'Weight: 1.50 lbs ' 'Ammo Capacity :13',)

    class Victor(bag):

        Name = 'Victor'
        Victor_stats   = 'age: 37  Weight: 220 lbs Height 6\'4" former amateur body builder, construction worker'
        prime_vehicle  = 'choice 2: Truck F-350 4X4 Dually (Big Construction Truck)   HP 400  Torque 800 ft-lb',
        Health_Points  = 100
        Stamina_Points = 100
        prime_weapons  = ('Riffle 1:'  'Heckler & Koch MG4  Machinegun               Cal:5.56 M ''Weight: 17.96 lbs  Ammo Capacity :200',
                          'Knife 5:' 'Stanley FatMax Drywall Hammer                         Weight: 14.0 oz  Handle Length:13.5',
                          'Gun 4:' 'Magnum Research Desert Eagle  ' 'Cal:.50     ' 'Weight: 4.46 lbs ' 'Ammo Capacity :7',)
                          
        semi_prime     = ('Riffle 5:'  'Heckler & Koch HK417 Semi_Automatic          Cal:7.62   ''Weight: 10.93 lbs  Ammo Capacity :20',
                          'Knife 1:' 'Gerber Parang            (Stout Machete Like Blade)   Weight: 1.35 lbs Blade  Length:13.5',
                          'Gun 2:' 'Smith & Wesson SW1911DK       ' 'Cal:.45 ACP ' 'Weight: 2.60 lbs ' 'Ammo Capacity :9',)

    class Gabriel(bag):
        Name = 'Gabriel'
        Gabriel_stats  = 'age: 28  Weight: 173 lbs Height 5\'9" Cycling enthusiast and rider, and videogame player'
        prime_vehicle  = 'choice 4: Yamaha YZ450F    450CC     (Off-Roading Bike)     HP  55',
        Health_Points  = 100
        Stamina_Points = 100
        
        prime_weapons  = ('Riffle 5:'  'Heckler & Koch HK417 Semi_Automatic          Cal:7.62   ''Weight: 10.93 lbs  Ammo Capacity :20',
                          'Knife 3:' 'ColdSteel Hatchet spike                               Weight: 1.53 lbs Handle Length:22.0',
                          'Gun 2:' 'Smith & Wesson SW1911DK       ' 'Cal:.45 ACP ' 'Weight: 2.60 lbs ' 'Ammo Capacity :9',)

        semi_prime     = ('Riffle 4:'  'Heckler & Koch HK416 Semi-Automatic          Cal:5.56   ''Weight:  9.05 lbs  Ammo Capacity :30',
                          'Knife 1:' 'Gerber Parang            (Stout Machete Like Blade)   Weight: 1.35 lbs Blade  Length:13.5',
                          'Gun 1:' 'Colt New Frontier 44 Special  ' 'Cal:.44     ' 'Weight: 2.80 lbs ' 'Ammo Capacity :6',)

class The_GunRoom(object):

    Riffle_rack =[                                                      
             'Riffle 1:'  'Heckler & Koch MG4  Machinegun               Cal:5.56 M ''Weight: 17.96 lbs  Ammo Capacity :200',
             'Riffle 2:'  'Remington Target Tactical Sniper riffle      Cal:308    ''Weight: 13.85 lbs  Ammo Capacity :4',
             'Riffle 3:'  'Remington Model 700 SPS Tactical BlackHawk   Cal:308    ''Weight:  8.85 lbs  Ammo Capacity :4',
             'Riffle 4:'  'Heckler & Koch HK416 Semi-Automatic          Cal:5.56   ''Weight:  9.05 lbs  Ammo Capacity :30',
             'Riffle 5:'  'Heckler & Koch HK417 Semi_Automatic          Cal:7.62   ''Weight: 10.93 lbs  Ammo Capacity :20',]

    guns =(
             'Gun 1:' 'Colt New Frontier 44 Special  ' 'Cal:.44     ' 'Weight: 2.80 lbs ' 'Ammo Capacity :6',
             'Gun 2:' 'Smith & Wesson SW1911DK       ' 'Cal:.45 ACP ' 'Weight: 2.60 lbs ' 'Ammo Capacity :9',
             'Gun 3:' 'Heckler & Koch P2000SK V2     ' 'Cal:.357    ' 'Weight: 1.50 lbs ' 'Ammo Capacity :13',
             'Gun 4:' 'Magnum Research Desert Eagle  ' 'Cal:.50     ' 'Weight: 4.46 lbs ' 'Ammo Capacity :7',
             'Gun 5:' 'Heckler & Koch MP5K           ' 'Cal: 9mm    ' 'Weight: 4.78 lbs ' 'Ammo Capacity :30',)

    Knife_rack =[
             'Knife 1:' 'Gerber Parang            (Stout Machete Like Blade)   Weight: 1.35 lbs Blade  Length:13.5',
             'Knife 2:' 'ColdSteel  O Katana          (Samurai Sword)          Weight: 3.00 lbs Blade  Length:36.0',
             'Knife 3:' 'ColdSteel Hatchet spike                               Weight: 1.53 lbs Handle Length:22.0',
             'Knife 4:' 'Tops Anaconda Tanto            (Big Knife)            Weight: 1.50 lbs Blade  Length:9.5',
             'Knife 5:' 'Stanley FatMax Drywall Hammer                         Weight: 14.0 oz  Handle Length:13.5',]

    Ammo_rack =[
             'Ammo 1: H&K Machinegun  Cal:5.56 M   '  'Ammo Weight:12.0 lbs  Amount:200',
             'Ammo 2: Rem 308         Cal:308      '  'Ammo Weight: 5.0 lbs  Amount:30',
             'Ammo 3: H&K HK416       Cal:5.56     '  'Ammo Weight: 1.5 lbs  Amount:30',
             'Ammo 4: H&K HK417       Cal:7.62     '  'Ammo Weight: 7.0 lbs  Amount:30',
             'Ammo 5: .44             Cal:.44      '  'Ammo Weight: 4.5 lbs  Amount:25',
             'Ammo 6: .45 ACP         Cal:.45 ACP  '  'Ammo Weight: 4.5 lbs  Amount:25',
             'Ammo 7: .357            Cal:.357     '  'Ammo Weight: 4.0 lbs  Amount:25',
             'Ammo 8: .50             Cal:.50      '  'Ammo Weight: 6.0 lbs  Amount:25',
             'Ammo 9: 9mm             Cal: 9mm     '  'Ammo Weight: 3.5 lbs  Amount:30',]

class Garage(object):
    suit = 'motorcycle suit',
    truck = (
    'choice 1: Toyota Tacoma 4.0           (Small Truck)         HP 236  Torque 266 ft-lb',
    'choice 2: Truck F-350 4X4 Dually (Big Construction Truck)   HP 400  Torque 800 ft-lb',
              )

    Motorcycle = (
    'choice 3: Suzuki Hayabusa 1340CC        (Super Bike)        HP 197',
    'choice 4: Yamaha YZ450F    450CC     (Off-Roading Bike)     HP  55',
                 )
    Car = (
    'choice 5: Porche 911 Turbo S 3.8L      (Super Car)          HP 530',
    'choice 6: Subaru Impreza 2.0L          (Rally Car)          HP 148',
          )

class Zombie_Mod(object): # this is actually just the ranges

    #:Make 3 ranges of zombies
    #:if you pick knife, then stamina goes down fastest
    #:Order of stamina going down independent of wether prime or not prime weapon picked
    #:  Gun,Riffle,Blade weapon

    class Weak(object):
        h_g_range = random.randint(1, 3)
        h_g_stamina = random.randint(11, 15)

        r_range = random.randint(1, 2)
        r_stamina = random.randint(15, 23)

        k_stab = random.randint(2, 3)
        k_stamina = random.randint(15, 30)

    class Medium(object):
        h_g_range =random.randint(2, 4)
        h_g_stamina =  random.randint(17, 27)

        r_range = random.randint(2, 3)
        r_stamina = random.randint(20, 30)

        k_stab = random.randint(3, 5)
        k_stamina = random.randint(23, 32)

    class Strong(object):
        h_g_range = random.randint(4, 5)
        h_g_stamina = random.randint(20, 35)

        r_range = random.randint(4, 5)
        r_stamina = random.randint(25, 40)

        k_stab = random.randint(5, 7)
        k_stamina = random.randint(27, 45)

def remain_in_mansion():
    print "you chose to stay in the mansion in hope that your friend will make"
    print "it back and you might just ride out the horrors outside"
    print "you search around the house to board it up or make it safer"
    print "to your dismay you find nothing"
    print "You hear another explosion closer this time, and you realize you"
    print "have to barricade yourself somewhere, as you are headed to the basement"
    print "you see the weapons room and grab a machine gun a piston and a parang"
    print "quickly you go down to the basement and are relieved to find stocks of water"
    print "and canned food. As you wait you hear noises coming from the basement vent window"
    print "soon you hear noise coming from within the house"
    print " you have the door locked and as you look on the TV\n"
    print "The picture from a newscopter shows you that all of LA is burning"
    print "you hear movement coming from the house, a few minutes later more noise"
    print "then you hear a thud on the door, then another"
    print "soon you hear the door creaking and a lot of noise just ouside the door"
    print "you steel yourself and grab the machinegun and shoot at the door"
    print "but the noise doesn't stop and you've ran out of ammo"
    print "so you grab the parang on one knife and the parang on the other"
    print "the door bursts open and there are badly wounded people making their way"
    print "to you , the adrenaline is now running strongly in your veins"
    print "you aim carefully but its difficult, you get the person closes to you"
    print "it's a heashot, you do the same three more times but now the place "
    print "is full of the beasts, you empty the gun an take out a few more"
    print "now you scream as you take the parang and aim for their necks"
    print "you take out 6 or 7 but you see they have no fear of you at all"
    print "you scream like a madman as they continue to come to you,"
    print "you swing again and one grabs your hand and bites it"
    print "you pull back and another one grabs your leg and bites it"
    print "you take out 3 more but now its too late"
    print "luckily you see the gun and remember you have another clip"
    print "on your pocket, through the pain you reload the gun and finish yourself"
    print "Bang"
    exit()

def foot_fault():
    print "You've decided to leave on foot"
    print "you head outside the mansion and you hear gunshots near and far, and then a scream"
    print "coming from the neighbors house, you start to feel the adrenaline in your blood"
    print "you make your way out the mansion and are now on the street headed south towards the marina"
    print "you make it about a mile and a half when you hear a car coming, it gets nearer and then you "
    print "hear a thud and the car starts to swerve, you know it hit something but cannot tell what it is"
    print "the car crashes and you start to walk a little faster"
    print "soon you feel the weight of the weapons bag and wonder if you will make it so far on foot"
    print "soon you hear a scream, and then you see two kids come from a house runing"
    print "after them are two other people but they are moving slower, you keep moving"
    print "soon you are near a church, and you hear a great deal of noise, as you are passing by it"
    print "you notice bits of flesh on the ground and bright red blood\n"
    print "A few yards in front you see one of the kids that ran passed you earlier"
    print "soon you see about a dozen or so people walking your way and more further out"
    print "they walk just like the ones that were after the kids earlier, they get closer, you dodge"
    print "two of them and one of them just barely touches you, they are mumbling and not really"
    print "saying anythin coherent, one of them grabs your arm and you shoot it in the head"
    print "some blood spatters on you, as you continue you see that all the people are now"
    print "headed your way, you dodge a few more and start to shoot as you walk but you miss"
    print "or so you think, but you notice that bullets don't affect them, soon all the people from the church"
    print "are making their way towards you; you continie to shoot and miss, soon you are out of ammo"
    print "someone grabs you and bites you. you look for another gun and then another one bites you in the leg"
    print "soon there are 10 people next to you all of them grabbing at you, then one of them grabs your head"
    print "and bites and rips through your throat, blood starts to gush out, with in seconds you are unconscious"
    print "you die"
    print "yuuuummmmmmmyyyyyyyyy...."

def no_weapons_death():
    print "you picked your vehicle and you are about to get on it when you hear some"
    print "noise from the garage door, so you hurry into your vehicle and open the "
    print "garage door with the remote, as it opens up you see a bunch of people going"
    print "for your vehicle, and you take off, as you make your way towards the street"
    print "you try to avoid some of the people, you see the gate doors opening, but in"
    print "your attempt to avoid people you hid the corner of the gate and the car stalls"
    print "the airbags deployed, you are stunned for just a second, and panic grips you"
    print "soon all the people that were in the way start to make their way towards the"
    print "car, you have no weapons and no way out, they can't make it into the car, but"
    print "you know that no one is coming to save you either, you wait it out for about an"
    print "hour, the people don't seem to have any direction but they are still hanging "
    print "around the car, you try to make a run to the mansion but somone grabs you and"
    print "take a chunk of your arm, you fight the woman off and keep moving, another "
    print "person grabs you and bites you on your side and you fight them off as well"
    print "you finally make it inside the mansion and you hole up in the basement"
    print "thirty minutes later you feel feverish, and then dizzy, you lay down to sleep"
    print "your breathing slows down as you are sleeping, soon your chest hardly rises"
    print "your heart stops"
    print "mrrrraaaawwwrrrrrr...braaaaaaiiiiinnnnnssss"

def flee():

    print "You hop on your ride and check the fuel gauge, you see that you have plenty"
    print "to make it to the marina with plenty left to spare, you open the garage door"
    print "and you hit the road. You head down Crenshaw Blvd, and you make all the way down"
    print "to Torrance; as you were driving you noticed the mayhem around you, people walking into"
    print "cars and being fatally hit yet not dying. It seemed like every other house or"
    print "structure was on fire, the electricity worked on some places and not others."
    print "You come up on an instersection, Crenshaw and 235 there are two huge blazing fires"
    print "and cars everywhere. It appears like you cannot make it through.There is a hill to your"
    print "left and your vehicle will make it since its made for off-roading too"
    print "you are getting down and a person with a missing arm looking at you, bearing their teeth"
    print "he lunges at you and you kick the top of his head and he stumbles back and you rush into"
    print "your vehicle you get in and make your way to the hill, you make it past the curb"
    print "the terrain is rough but thanks to the high suspension and all wheel drive, traverse it with"
    print "ease and soon you are past the fire and on your way to the marina\n"

def motor_death():
    print "You hop on the motorcycle and make your way out of the mansion "
    print "you feel somewhat unconfortable on the bike due to the weapons bag"
    print "however you are able to get out of the way of the people that are "
    print "walking along the street with ease"
    print "you see cars crashed here and there and you realize you have to "
    print "make your way to the marina fast if you are going to survive this"
    print "so you hit the gas, as you are going uphill the bike jumps a bit"
    print "but you are able to control it somehow, and now you are headed "
    print "downhill, as you accelerate you feel you'recoming around a curve much faster"
    print "then you anticipated you see a body and you try to miss it"
    print "but the weapons bag stops you from maneuvering out in time"
    print "the front wheel hits the body and lifts the front of the bike"
    print "an instant later the back wheel hits it and it kicks you off the "
    print "bike, you go flying in the air for a hundred feet and hit the pavement"
    print "you skull bursts open and the bag over your shoulder whips your arm in"
    print "front of you and dislocates your shoulder"
    print "you die instantly"
    print "SPLAT!!!"

def gabriel_m_death():
    print "So you see the busa and put on a helmet, if you are going "
    print "out, you are going out in style, you hop on the bike and make"
    print "Your way out of the mansion and onto the street, you tied the bag"
    print "close to your body so that you can maneuver the bike well"
    print "You start to haul ass up the hill, pretty soon you are almost"
    print "half way out of the peninsula, so make your way down the hill"
    print "you are on the road and notice the mayhem around you, people walking"
    print "into cars and being fatally hit, yet not dying. It seemed like every"
    print "other house and structure was on fire, the electricity worked"
    print "on some places and not others. You come up on an intersection"
    print "Crenshaw and 235, there are two huge blazing fires from the gas stations"
    print "there are cars everywhere, some crashed most just abandoned"
    print "It appears like your busa cannot make it trough, so get off the bike"
    print "and get on top of a car to see look for a way around, you see"
    print "that there isn't, you regret not taking the off-roading bike"
    print "you notice that there are people looking at you and they start to"
    print "make their way towards you, you know you have to ditch the bike"
    print "and find another way to the marina, not too far you see two people"
    print "on fire approaching you, you must make it pass the fire on foot"
    print "you check your bag to see what you have just for reassurance"

def gabriel_hop():

    print "You get on the bike and make your way onto the street soon you are riding"
    print "down Crenshaw blvd, the bike is noisy and as you pass by you see people"
    print "look towards you and start to follow you, everything goes fine and you make it"
    print "to Torrance; as you were driving you noticed the mayhem around you, people walking into"
    print "cars and being fatally hit yet not dying. It seemed like every other house or"
    print "structure was on fire, the electricity worked on some places and not others."
    print "You come up on an instersection, Crenshaw and 235 there are two huge blazing fires"
    print "and cars everywhere. It appears like you cannot make it through.You get off of the bike"
    print "and hop on top of a car to see if there is a way through the cars, but due to the fire"
    print "and debris you cannot make it trough the cars on the bike, so you decide to chance it"
    print "you get back on the dirt bike you rev it up and you hop on top of the vehicles"
    print "you have a hard time keeping your balance but you are able to make it sometimes hopping"
    print "on the hoods of the cars or by going in between them, in no time you make it past the fire"
    print "and are on your way to the airport.\n"

def vehicle_ditch():
    print "you get on your vehicle and make your way onto the street, and soon you are on the main Blvd"
    print "as you wind down the hill you see people with horrible injuries walking on the street"
    print "some people are attacking each other, some are running from others you make it"
    print "to Torrance; as you were driving you noticed the mayhem around you, people walking into"
    print "cars and being fatally hit yet not dying. It seemed like every other house or"
    print "structure was on fire, the electricity worked on some places and not others."
    print "You come up on an instersection, Crenshaw and 235 there are two huge blazing fires"
    print "everywhere you look there are abandoned or crashed cars, you get out of your vehicle"
    print "and hop on top of it to check if there is anyway you can make it through"
    print "you realize the only way out is to get pass the wreckage on foot, as you are getting down"
    print "you notice that there are people slowly walking your way and your insticts tell you"
    print "that you should not stay there thinking too long, you grab the bag from your car and"
    print "start to make your way trough the mess\n"

def the_fire_fight():
    print "The fires are blazing, you can feel the heat from the fire and can smell the scent of the"
    print "diesel and gas burning, you hope that the propane tanks don't explode as you try to make your"
    print "way past the fire. You see a person approaching you, he doesn't say anything, it gets closer"
    print "you keep making your way towards the fire but the heat starts to get more and more intense,"
    print "you look behind you and notice that there are more people approaching you, you hop on the hood"
    print "of a car, you jump onto another, then there is some space between some vechicles, as you get down"
    print "a person approches you, it grabs at you and you stumble back and hit a car, she comes toward you,"
    print "you notice the singed hair and burned arms, you can see the bones from some of her fingers, and smell"
    print "the burnt flesh, fear grips you in an instant, the woman starts to hiss and grabs your leg, you kick"
    print "her and she keeps grabbing at you, you keep kicking and suddenly you remember your bag, you reach in"

def the_dealership_story(zombie_count):

    print "You made it to the dealership you notice that the entrance to the showroom is"
    print "shattered, the lights are off, you start looking around to see if you can find"
    print "where they keep the keys to the vehicles outside, your eyes start getting used to the"
    print "darkness and you keep looking, then you hear someone stepping on glass and a snort of"
    print "some sort, your body instantly tenses up and your heart starts to feel like its going to"
    print "burst out of your chest, you hear more steps, you can tell that they are random, quietly"
    print "you bear crawl using the desks as cover, you think you see what looks to be a keybox, and"
    print "you make your way towards it, you hear more people stepping on the glass, there are keys"
    print "strewn about, as you crawl toward them you hit a chair that hits a desk and the spheres on"
    print "the Newtons Cradle start to hit each other making noise, the steps start to get louder and"
    print "this time they are coming your way, you grab a bunch of keys and throw them in your bag"
    print "you get up and now you see that there are about !!**!! %d zombies !!**!!" % zombie_count
    print "shit you think, I'm fucked, you look for another exit but realize the only way out is the"
    print "same way you came in, you know you have to run or fight your way out."
    print "\n\nto check your weapons bag press '1' to make a run for it press '2'"

def mad_dash():
    print "so you decide to make a run for it, you have your goal set up to make it to the exit"
    print "there are two zombies right in front of you and you manage to evade them and you"
    print "you're doing good and are almost near the exit, there are zombies just outside as well"
    print "just as you are about to make it you trip over a a lamp on the ground, the zombies"
    print "that were barely outside come in and grab for you, you try to fight them off, and then"
    print "try to reach for whats in your bag but now more are on top of you and they start to bite"
    print "into every body part, you hope for a quick death, but it doesn't come...you grab some "
    print "some of the glass from the shattered entrance and with your final strength you manage to cut"
    print "your own throat, blood gushes out and in about 20 seconds you are dead..."
    print "GRRLLLRLRLRLLRGGRLL..."

def turn_key():
    print "You managed to kill the zombies coming at you inside the dealership, your heart is pumping"
    print "and make it pass the broken glass with your bag held tightly and start looking for they keys"
    print "they are at the bottom of the bag and you grabb them, as fast as you can you press the alarm"
    print "on them several click but they are mostly small cars and finally the one hummer sounds"
    print "you run to it and struggle with putting the key in the key hole..your hand is shaking"
    print "you finally think of the lock button on the remote..the locks pop up and you feel relieved"
    print "you put the key in and it turns on, a small smile flashes on your face"
    print "it quickly vanishes as you hear thuds against the vehicle, there are 'People' grabbing at "
    print "the truck, you put in gear and take off, the truck lunges and stops, you failed to see the"
    print "parking brake still engaged you look around and see the small pedal and disengage it"
    print "you take off and run down a few of the people and finally make it to the street.\n"
    
def bag_check():
    #:#################################################################################################"
    print "As you make it on the road again, and feeling calm for a minute you see helicopters"
    print "flying all over the place, the main roads have vehicles of all types crashed burning"
    print "or flipped upside down, you see injured people walking on the street bleeding, some "
    print "are running , others are being attacked and stores are being looted"
    print "you turn on the radio and all the stations seemed to be saying the same thing, there"
    print "is a city wide mass hysteria, people are urged to stay home and to call 911 in case "
    print "of emergency. A sense of urgency starts to come over you, as the thought of not making"
    print "it to the marina grips your mind, you come on to an instersection that seems to be blocked"
    print "you don't dare get out of the truck to check, you see that all the vehicles blocking the"
    print "way are abandoned, it seems that you cant get through, so you decide to put the hummer into"
    print "4-wheel drive, you bump into the car blocking the way and it doesn't budge, so you back up"
    print "about a foot and and hit the gas, it gives you enough momentum to budge the car a bit and"
    print "it starts to move, the truck shakes as the bumpers of the car you moved and the one"
    print "next to it start grinding on the sides. You hear the tires squeel and hope they don't"
    print "burst from some sharp metal, but you make it through.\n"
    
    print "Because of all the traffic you decided to take mostly residential streets and only got on"
    print "major streets when necessary, you've spent two hours driving and the low fuel light turns on"
    print "because of the chaos you are forced to take a major road and it takes you near the airport"
    print "you have passed through there a few times before so you are passingly familiar with the area"
    print "however as you keep driving the truck starts to stutter and you it finally runs out of fuel"
    print "and coasts to a stop. You become freightened knowing that you have about 4 miles to traverse"
    print "on foot, and its been almost three hours since you left your friends mansion you hope that"
    print "no one has stolen the boat or that the docks are still serviceable, you open the door slowly"
    print "and hop down as quietly as you can at least all the street lights are on you think, you start"
    print "to make your way to the marina, all that cardio you use to do at the gym has not gone to waste"
    print "you think to yourself with a quick smile\n"
    print "A few yards ahead you see a few people walking very strangely and you decide you're not going"
    print "to take any chances, you get besides a car and check your bag\n"
    
def take_off():
        
    print "there weren't that many walkers so you were able to just walk around them"
    print "soon you make it to sepulveda blvd, there are cars everywhere, there is a"
    print "huge fire on one of the airstrips and you can feel a faint, heat coming"
    print "from it, sirens are sounding all around, some people are trapped in their"
    print "cars, others walking aimlessly, the vast majority are attacking or"
    print "fending off the attackers, you know that getting through this mess is not"
    print "going to be easy, you get between some cars and start making way, fast enough"
    print "some of the attackers try to get at you, so you get ready and you start fighting"
    print "back"
    print "\n\n"
      
def death_march():
    print "You barely made it through that parking lot of death at the airport and you still"
    print "have a few miles to make it to the marina but you are close and even with all the"
    print "scrapes and tiredness you are starting to feel, you have a glimmer of hope, you"
    print "continue to march away from the madness behind you, and you quickly learn to avoid"
    print "people dead, alive or otherwise, you run a few yards then walk everytime you see one"
    print "if those undead people, you can avoid them as long as you don't get pinned down it"
    print "appears that they cannot see all too well in the dark but their sense of hearing seems"
    print "to be very keen,thirty five minutes later you make it to LMU and you can see what has"
    print "happened around the city trough that vantage point, there are inumberable fires all over"
    print "the skies seem to be infested with helicpoters and you hear what seem to be fighter jets"
    print "in the skies, like a searing flash of pain, a feeling of deep sadness comes and passes"
    print "you have to continue, you can see the marina from where you stand but as all those painful"
    print "runs you have gone on before, you know that seeing the end does not help your cause at all"
    print "your body starts to feel weary from all the exersion back there, and you continue if a bit"
    print "slower. \n"
    
    print "with only a mile to go you are at the Lincol Jefferson intersection, you can see the bridge"
    print "up ahead, there are cars there and people walking around, if you get lucky the canal will be"
    print "low, otherwise you will have a tough time making it through, you start to become a bit agitated"
    print "the bridge is about 50 yards away and you can hear grunting and some screams, cars are blocking"
    print "the way through, so you decide to go by the side and check the water level but it's too dark"
    print "and you know that one wrong step and you will not be able to survive, you curse yourself"
    print "the situation has forced you to take the bridge and you have to fight your way through again"
    print "just before you head to the bridge you check you bag once more.\n"
    
def road_runner():
    print "\n\nYou just made it out alive, there were not that many monsters to get trough but"
    print "your weak muscles along with the cramped spaces almost got you killed, you thought you"
    print "were bitten but you see the wound is a slice from a loose metal body part, you start"
    print "to feel the pain, and start shuffleling as fast as you can towards the marina, it"
    print "appears the bleeding is pretty severe, there is a medkit in the yacht you just need"
    print "to get to it, just up ahead is the entrance to the marina.\n\n"

def final_run():    
    
    print "There are surprisingly few people there, it seems most rich boat owners couldn't"
    print "make it to their boats, the few walkers around even in your wounded state are easy"
    print "to evade as long as you are quiet, since all the lights in the docks are out."
    print "ten minutes later you make it to the docks on Midano way, you head to the slips"
    print "of course you think things couldn't be this easy, there are walkers moving about"
    print "and some of them you can tell from the faint light came from the various restaurants"
    print "around the area, some hav napkins hanving on their necks others are covered in foods"
    print "of different kinds, the whole bunch give off a disgusting smell from their medley of"
    print "fancy aromatic dinners.\n"
    
    print "With not much time before one of them notices you, you decide that you are going to"
    print "bang on one of the cars to draw most of them away from the dock entrance and then"
    print "move in between the parked cars making more noise to distract them that should"
    print "reduce the number of walkers you have to evade or kill to make it to the dock\n"
    
    print "You look into your bag hoping there is something you can use to make it to the yacht"
   
def sail_away():
    print "The gambit worked as you planned, you made it past the majority and were able"
    print "to kill the rest, unfortunately you had to leave all your weapons behind you"
    print "did not have the strength to climb the fence,with anything after falling on your"
    print "first try, but it doesn't matter now, you limp along onto the slip your friends boat is in"
    print "you get in and find the control board and do the checks you remember your friend teaching you"
    print "once, you hit a switch and all the lights on the boat turn on including some very bright"
    print "search lights, immediately you hear grunting and hissing coming from the gate to the dock"
    print "and you see that there are far more zombies then you had imagined, a face of terror flashes on"
    print "your face, adrenaline hits you again and with a quick limp you go and untie the yacht"
    print "the key was were your buddy always keeps it and you turn on the engines, they come alive instantly"
    print "and loudly, you check the fuel gauge..!Yes! you think its nice to have a rich friend, with the most"
    print "delicacy you can manage you manuever the boat out of the slip , it scrapes along the side but it makes"
    print "it through intact, you move through the marina and then passed it, you are on your way to catalina"
    print "you look for the medkit and find it, doing the best you can looking at your wound most of the bleeding"
    print "stopped, now your body cries for sleep and it will be at least an hour and a half til you make it to "
    print "the island, you set an alarm next to your ear for an our and set the boat on a straight heading\n"
    
    print "A great thundering wall of sound awakens you, the alarm clock is sounding you are hanging on the side of"
    print "the yacht water is splashing and you inadvertantly drink some sea water, its darnk and you can't see much"
    print "you move about and soon end on the top of the slowly sinking remains of the yacht, the boats auto made it"
    print "to the marina on catalina but couldn't avoid another boat that was going in circles"
    print "you don't have the strength to swim to shore, but luck is on your side, you see anothe boat moving about"
    print "it looks like they saw what happened and are going over to investigate, its dawn now, the sun is breaking"
    print "just.\n"
    print "The yacht approaches, its an old couple"
    print "'hey' says the old man, you need any help"
    print "'sure could use some you say, they toss you a rope and they will drag you up over the water , so you wrap"
    print "the rope around your waist your arm and legs you don't want to die now you think and you couldn't swim"
    print "in your weakened state..you slowly begin to get as close to the couples yacht as you can, as you dip your"
    print "foot into the water, a shark flies trough the air, its fin and part of its tail missing, it aimed for"
    print "your head and got it, both you and the shark land on the wrekage, the shark is cut open by some sharp"
    print "edges protruding from the debri, half your face is gone and neck broken, the shark continues flopping"
    print "around, it has clearly fatal wounds..the Fucking Zombie Shark got you..\n\n"
    
    print "the End"
    

















