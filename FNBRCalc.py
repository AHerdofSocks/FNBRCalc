__author__ = 'John Williams'

'''Calculate Fortnite Battle Pass leveling'''

# base level 31
# pass 35 with 3/10
# 8 weeks remain
# 20 points from blockbuster (2 tiers)
# 20 pts from starter challenges
# 10 levels = 31 pts

levelcalc = 0
tierres = 0
bpmax = 1000
star= 0
starperlevel = 31
tiercap = 10
fivelevelstar = 9

# get player info

level = float(input("Enter current season level "))
tier = float(input("Enter current battle pass tier "))
tierlef = float(input("Enter the star progress in your current BP tier "))
weeklylevel = float(input("How many times per week do you usually level up? "))

# breaks down season level into star equivalent

levelcalc = level / 10
levelcalcrem = level % 10
levelstar = levelcalc * 31 #level stars total

# breaks down tier into star equivalent

tierstar = tier * 10
tiercalc = tierstar + levelstar #tier stars total
tierstarrem = bpmax - tiercalc #tier stars remaining

# assembles season level into tier level

tierres = levelstar / 10
tierprog = tiercap - tierlef

# calculate remaining progress

levelprog1 = tierstarrem / 3.1
challengeprog = tierstarrem / 50

# leveling x amount per week with/without clearing all challenges

#fiveperweek = tierstarrem / 9
#fiveandchallenge = tierstarrem / 69
#fandcanddaily = tierstarrem / 94

# daily level up calculation for additional stars

counter = 1
levelprojstar = 0
#levelprojfives = level % 5
#levelprojtens = level % 10
levelnew = level
leveldisplay = 0

while counter <= weeklylevel:

    levelnew = levelnew + 1

    #levelproj = levelproj + 2
    levelprojtens = levelnew % 10
    levelprojfives = levelnew % 5

    #levelnew = levelnew + 1

    if levelprojtens == 0:
        levelprojstar = levelprojstar + 10

    elif levelprojfives == 0:
        levelprojstar = levelprojstar + 5

    #elif levelprojtens == 0:
        #levelproj = levelproj + 10

    else:
        levelprojstar = levelprojstar + 2 #levelprojstar is the star result of the levels

    counter = counter + 1
    #level = level + 1
    # no leveldisplay = leveldisplay + levelprojstar

# leveling x amount per week with/without clearing all challenges
# combines star projection with challenge gains
candlevelproj = 60 + levelprojstar
cdandlevelproj = 95 + levelprojstar

# calculates weeks remaining
fiveperweek = tierstarrem / levelprojstar
fiveandchallenge = tierstarrem / candlevelproj
fandcanddaily = tierstarrem / cdandlevelproj



# display battlepass progress info
print('-----------------')
print('Tier: ', tier, '    Level: ', level)
print('Stars until next tier up:', tierprog, 'Stars until tier 100:', tierstarrem)
#print('Stars until tier 100:', tierstarrem)
print('-----------------')
print('Simple Levels until Tier 100:', '%.2f' % levelprog1)
print('-OR-')
print('Simple Challenge weeks until Tier 100:', '%.2f' % challengeprog)
print('-----------------')
print('Leveling ', weeklylevel, ' times per week: ', '%.2f' % fiveperweek,' weeks... good luck.')
print('... while clearing all weekly challenges and blockbusters: ', '%.2f' % fiveandchallenge, ' weeks.')
print('... and dailies:', '%.2f' % fandcanddaily, 'weeks.')
