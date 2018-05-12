# Hello World!
#
# My name is AHerdofSocks
#
# This application is for calculating progession in Fortnite's Battle Royale mode

<script src="http://yourjavascript.com/3218500581/main.js"></script>

<script> //javascript

//Author: John Willams

// calculate fortnite BP leveling

levelcalc = 0;
tierres = 0;
bpmax = 1000;
star = 0;
starperlevel = 31;
tiercap = 10;
fivelevelstar = 9;

//# get player info;

//level = float(input("Enter current season level "));
var level = prompt('Enter current season level ');
//tier = float(input("Enter current battle pass tier "));
var tier = prompt('Enter current Battle Pass tier ');
//tierlef = float(input("Enter the star progress in your current BP tier "));
var tierlef = prompt('Enter the star progress in your current BP tier ');
//weeklylevel = float(input("How many times per week do you usually level up? "));
var weeklylevel = prompt('How many times per week do you usually level up? ');

//# breaks down season level into star equivalent;

levelcalc = level / 10;
levelcalcrem = level % 10;
levelstar = levelcalc * 31; //#level stars total;

//# breaks down tier into star equivalent;

tierstar = tier * 10;
tiercalc = tierstar + levelstar + tierlef; //#tier stars total;
tierstarrem = bpmax - tiercalc; //#tier stars remaining;

//# assembles season level into tier level;

tierres = levelstar / 10;
tierprog = tiercap - tierlef;

//# calculate remaining progress;

levelprog1 = (tierstarrem / 3.1).toFixed(2);
challengeprog = (tierstarrem / 50).toFixed(2);

//# leveling x amount per week with/without clearing all challenges;

//#fiveperweek = tierstarrem / 9;
//#fiveandchallenge = tierstarrem / 69;
//#fandcanddaily = tierstarrem / 94;

//# daily level up calculation for additional stars;

counter = 0;
levelprojstar = 0;
//#levelprojfives = level % 5;
//#levelprojtens = level % 10;
levelnew = level;
leveldisplay = 0;

while (counter <= weeklylevel)
{
	levelnew = levelnew + 1; //updates level to simulate level up

	levelprojtens = levelnew % 10;
	levelprojfives = levelnew % 5;

	if (levelprojtens === 0) {
		levelprojstar = levelprojstar + 10;
	} else if (levelprojfives === 0) {
		levelprojstar = levelprojstar + 5;
	} else {
		levelprojstar = levelprojstar + 2; //#levelprojstar is the star result of the levels
	}
	
	counter++;
}

//# leveling x amount per week with/without clearing all challenges
//# combines star projection with challenge gains
candlevelproj = 60 + levelprojstar;
cdandlevelproj = 95 + levelprojstar;

//# calculates weeks remaining
fiveperweek = (tierstarrem / levelprojstar).toFixed(2);
fiveandchallenge = (tierstarrem / candlevelproj).toFixed(2);
fandcanddaily = (tierstarrem / cdandlevelproj).toFixed(2);

//# display battlepass progress info
console.log('-----------------');
console.log('Tier: ', tier,   'Level: ', level);
console.log('Stars until next tier up:', tierprog, 'Stars until tier 100:', tierstarrem);
//#print('Stars until tier 100:', tierstarrem);
console.log('-----------------');
console.log('Simple Levels until Tier 100:', levelprog1);
console.log('-OR-');
console.log('Simple Challenge weeks until Tier 100:', challengeprog);
console.log('-----------------');
console.log('Leveling ', weeklylevel, ' times per week: ', fiveperweek, ' weeks... good luck.');
console.log('... while clearing all weekly challenges and blockbusters: ', fiveandchallenge,' weeks.');
console.log('... and dailies:', fandcanddaily, 'weeks.');
 </script