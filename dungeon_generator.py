import random
######################################################

def rolld8():
	return random.randint(1,8)
def rolld10():
	return random.randint(1,10)
def rolld12():
	return random.randint(1,12)
def rolld20():
	return random.randint(1,20)
def rolld24():
	return random.randint(1,24)
def rolld75():
	return random.randint(1,75)
def rolld100():
	return random.randint(1,100)

######################################################

def base_value_of_the_hoard():
	r = rolld100()
	if r == 1: return 1
	if r >= 2 and r <= 3: return 10
	if r >= 4 and r <= 8: return 25
	if r >= 9 and r <= 14: return 50
	if r >= 15 and r <= 24: return 75
	if r >= 25 and r <= 76: return 100
	if r >= 77 and r <= 86: return 150
	if r >= 87 and r <= 92: return 200
	if r >= 93 and r <= 97: return 300
	if r >= 98 and r <= 99: return 500
	if r == 100: return 1000

def type_of_treasure():
	r = rolld20()
	if r == 1: return "art"
	if r >= 2 and r <= 3: return "jeweled items"
	if r >= 4 and r <= 7: return "goods"
	if r >= 8 and r <= 13: return "coins"
	if r >= 14 and r <= 17: return "furnishings and clothing"
	if r >= 18 and r <= 19: return "gems"
	if r == 20: return "special and magic items"

#uncomplete
def hoard_size():
	r = rolld20()
	if r == 1: return "individual treasure\t1 treasure unit"
	if r >= 2 and r <= 3: return "small (unguarded) hoard\t1-3 treasure units"

def treasure_containers():
	r = rolld10()
	if r == 1: return "bags or sacks"
	if r == 2: return "barrels or chest"
	if r == 3: return "coffer or kist"
	if r == 4: return "chest"
	if r == 5: return "huge chest"
	if r == 6: return "trunk"
	if r == 7: return "urn"
	if r == 8: return "jar"
	if r == 9: return "niche"
	if r == 10: return "loose"

def treasure_is_hidden_by():
	r = rolld10()
	if r >= 1 and r <= 2: return "concealed"
	if r == 3: return "invisible"
	if r == 4: return "secret space under container"
	if r == 5: return "secret compartment"
	if r == 6: return "inside an ordinary item in plain view"
	if r == 7: return "disguised to appear as something else"
	if r == 8: return "under a heap of trash or dung"
	if r == 9: return "under a loose stone in the floor or wall"
	if r == 10: return "in a nearby secret or concealed room"

def treasure_is_trapped_by():
	r = rolld20()
	if r == 1: return "contact poison on treasure"
	if r == 2: return "contact poison on container"
	if r >= 3 and r <= 4: return "poison needles in lock"
	if r >= 5 and r <= 6: return "poison needles in handle"
	if r >= 7 and r <= 8: return "poisoned spring darts in front"
	if r >= 9 and r <= 10: return "poisoned spring darts on top"
	if r >= 11 and r <= 12: return "poisoned spring darts from inside lid"
	if r >= 13 and r <= 14: return "poisoned spring darts from inside bottom"
	if r == 15: return "blade scythe across top"
	if r == 16: return "poisonous vermin (insects, reptiles)"
	if r == 17: return "poison gas released"
	if r == 18: return "trap door opens"
	if r == 19: return "stone block drops"
	if r == 20: return "magic"

def you_find_art():
	r = rolld20()
	if r >= 1 and r <= 2: return "paper art (prints, calligraphy, illustrated manuscript)"
	if r >= 3 and r <= 4: return "fabric art (tapestry, embroidery, quilt)"
	if r >= 5 and r <= 6: return "painting (watercolour, oils, acrylics, enamels)"
	if r >= 7 and r <= 8: return "crafts (doll making, book binding)"
	if r >= 9 and r <= 10: return "carving (woodwork, scrimshaw, bone, ivory, scales)"
	if r >= 11 and r <= 12: return "ceramics (pottery, urns, statuary, china)"
	if r >= 13 and r <= 14: return "glasswork (decanters, chandeliers, goblets, pipes, bowls, windows)"
	if r >= 15 and r <= 17: return "stonework (statues, birdbaths, plaques)"
	if r >= 18 and r <= 19: return "metalwork (sculpture, furnishings, decorative)"
	if r == 20: return "magical"

def you_find_a_room():
	r = rolld8()
	if r == 1:	print "room of public assembly..."+you_find_a_room_of_public_assembly()
	if r == 2:	print "room of containment and imprisonment..."+you_find_a_room_of_containment_and_imprisonment()
	if r == 3:	print "room of pleasure and relaxation..."+you_find_a_room_of_pleasure_and_relaxation()
	if r == 4:	print "room of general function..."+you_find_a_room_of_general_function()
	if r == 5:	print "room of war and conflict..."
	if r == 6:	print "room of deities and worship..."
	if r == 7:	print "room of learning and knowledge..."
	if r == 8:	print "room of room of specific utility..."

def you_find_a_room_of_public_assembly():
	r = rolld8()
	if r == 1: return "assemblage"
	if r >= 2 and r <= 3: return "antechamber"
	if r == 4: return "amphitheater"
	if r == 5: return "audience hall"
	if r == 6: return "courtroom"
	if r == 7: return "great hall"
	if r == 8: return "throne room"

def you_find_a_room_of_containment_and_imprisonment():
	r = roll1d12()
	if r == 1: return "aviary"
	if r == 2: return "bestiay"
	if r == 3: return "cage"
	if r >= 4 and r <= 5: return "cell"
	if r == 6: return "kennel"
	if r == 7: return "oubliette"
	if r == 8: return "padded room"
	if r == 9: return "pen"
	if r == 10: return "prison"
	if r == 11: return "stockade"
	if r == 12: return "zoo"

def you_find_a_room_of_pleasure_and_relaxation():
	r = rolld20()
	if r == 1: return "arena"
	if r >= 2 and r <= 3: return "banquet"
	if r == 4: return "combat pit"
	if r >= 5 and r <= 6: return "den"
	if r == 7: return "game room"
	if r >= 8 and r <= 9: return "gallery"
	if r == 10: return "harem"
	if r == 11: return "maze"
	if r >= 12 and r <= 13: return "museum"
	if r == 14: return "music room"
	if r == 15: return "pool"
	if r == 16: return "sauna"
	if r == 17: return "seraglio"
	if r == 18: return "statuary"
	if r == 19: return "torture chamber"
	if r == 20: return "trophy room"

def you_find_a_room_of_general_function():
	r = rolld24()
	if r == 1: return "bathroom"
	if r == 2: return "bedroom"
	if r == 3: return "cistern room"
	if r >= 4 and r <= 5: return "closet"
	if r == 6: return "dining room"
	if r == 7: return "dressing room"
	if r == 8: return "foyer (entry room)"
	if r == 9: return "hall"
	if r == 10: return "lair"
	if r == 11: return "larder / pantry"
	if r == 12: return "lounge"
	if r == 13: return "map room"
	if r == 14: return "privy"
	if r == 15: return "planning room"
	if r == 16: return "reception chamber"
	if r == 17: return "salon"
	if r == 18: return "servants dorm"
	if r == 19: return "storage"
	if r == 20: return "waiting room"
	if r == 21: return "wardrobe"
	if r == 22: return "well room"
	if r == 23: return "vault"
	if r == 24: return "vestibule"

#incomplete
def you_hear_a_sound():
	r = rolld75()
	if r == 1: return "bang/slam"
	if r == 2: return "bellow"
	if r == 3: return "bong"
	if r == 4: return "bubbling"
	if r == 5: return "buzzing"
	if r == 6: return "chirping"
	if r == 7: return "chanting"
	if r == 8: return "chiming"
	if r == 9: return "clanking"
	if r == 10: return "clashing"
	if r == 11: return "clicking"
	if r == 12: return "coughing"
	if r == 13: return "creaking"
	if r == 14: return "drumming"
	if r == 15: return "footsteps ahead"
	if r == 16: return "footsteps approaching"
	if r == 17: return "footsteps behind"
	if r == 18: return "footsteps receding"
	if r == 19: return "footsteps to the side"
	if r == 20: return "footsteps that are faint"
	if r == 21: return "gong"
	if r == 22: return "grating"
	if r == 23: return "groaning"
	if r == 24: return "grunting"
	if r == 25: return "hissing"
	if r == 26: return "hooting"
	if r == 27: return "horn/trumpet"
	if r == 28: return "howling"
	if r == 29: return "humming"
	if r == 30: return "jingling"
	if r == 31: return "knocking"
	if r == 32: return "laughter"
	if r == 34: return "moaning"
	if r == 35: return "murmuring"
	if r == 36: return "music"
	if r == 37: return "rattling"
	if r == 38: return "ringing"
	if r == 39: return "roaring"
	if r == 40: return "rustling"
	if r == 41: return "scratching/scrabbling"
	if r == 42: return "screaming"
	if r == 43: return "scuttling"
	if r == 44: return "shuffling"
	if r == 45: return "slithering"
	if r == 46: return "snapping"
	if r == 47: return "sneezing"
	if r == 48: return "sobbing"
	if r == 49: return "splashing"
	if r == 50: return "splintering"
	if r == 51: return "squeaking"
	if r == 52: return "squealing"
	if r == 53: return "tapping"
	if r == 54: return "thud"
	if r == 55: return "thumping"
	if r == 56: return "tinkling"
	if r == 57: return "twanging"
	if r == 58: return "whining"
	if r == 59: return "whispering"
	if r == 60: return "whistling"
	if r == 61: return 
	if r == 62: return 
	if r == 63: return 
	if r == 64: return 
	if r == 65: return 
	if r == 66: return 
	if r == 67: return 
	if r == 68: return 
	if r == 69: return 
	if r == 70: return 
	if r == 71: return 
	if r == 72: return 
	if r == 73: return 
	if r == 74: return 
	if r == 75: return  

def interfering_with_rest():
	r = rolld12()
	if r == 1: return "sheer number of potential foes who occupy the region makes it precarious"
	if r == 2: return "the adventure site is especially creepy and disturbing"
	if r == 3: return "the deathly chill of the area makes you continually uncomfortable"
	if r == 4: return "the area smells really really bad for some reason"
	if r == 5: return "the opposition are engaging in guerilla warfare against you"
	if r == 6: return "the area is flooded and damp, making it hard to stay dry and find a dry place to sleep"
	if r == 7: return "it is almost impossible to find doors, such as the area is filled with chambers."
	if r == 8: return "most of the occupants are nocturnal, i.e they barricade themselves in during the day"
	if r == 9: return "some act of sabotage interfers with the party, such as the food disappearing"
	if r == 10: return "some objective is time sensitive; there is no time to rest"
	if r == 11: return "the air itself is laced with magic, making you drowsy."
	if r == 12: return ""

def interfering_with_lighting():
	r = rolld10()
	if r == 1: return "water"
	if r == 2: return "maze / caverns"
	if r == 3: return "wind"
	if r == 4: return "rain"
	if r == 5: return "enclosed environments"
	if r == 6: return "enemies attracted to light"
	if r == 7: return "foes attacking an ioun stone"
	if r == 8: return "trap!"
	if r == 9: return "highly flammable environment"
	if r == 10: return "'Guards and Wards' spell"

def you_find_a_merchant():
	r = rolld10()
	if r == 1: return "grave robber"
	if r == 2: return "bandit merchant"
	if r == 3: return "trades with the enemy"
	if r == 4: return "recycles goods from higher level adventurers to lower level ones"
	if r == 5: return "crafts everything he makes, for maximum profit"
	if r == 6: return "adventuring merchant"
	if r == 7: 
		a = "a neutral monster... "
		s = rolld10()
		if s == 1: return a+"drow"
		if s == 2: return a+"duergar"
		if s == 3: return a+"hobgoblin"
		if s == 4: return a+"aasimar"
		if s == 5: return a+"dryad"
		if s == 6: return a+"dragon"
		if s == 7: return a+"catfolk"
		if s == 8: return a+"tiefling"
		if s == 9: return a+"merfolk"
		if s == 10: return a+"dwarf"
	if r == 8: return "seems to use a child proxy, possibly organised crime"
	if r == 9: return "an illusion greets you, such as magic mouth"
	if r == 10: return "monopolist"
######################################################

def npc_emotion():
	r = rolld75()
	if r == 1: return "adoration"
	if r == 2: return "agitation"
	if r == 3: return "amazement"
	if r == 4: return "amusement"
	if r == 5: return "anger"
	if r == 6: return "anguish"
	if r == 7: return "annoyance"
	if r == 8: return "anticipation"
	if r == 9: return "anxiety"
	if r == 10: return "confidence"
	if r == 11: return "conflicted"
	if r == 12: return "confusion"
	if r == 13: return "contempt"
	if r == 14: return "curiousity"
	if r == 15: return "defeat"
	if r == 16: return "defensiveness"
	if r == 17: return "denial"
	if r == 18: return "depression"
	if r == 19: return "desire"
	if r == 20: return "desperation"
	if r == 21: return "determination"
	if r == 22: return "disappointment"
	if r == 23: return "disbelief"
	if r == 24: return "disgust"
	if r == 25: return "doubt"
	if r == 26: return "dread"
	if r == 27: return "eagerness"
	if r == 28: return "elation"
	if r == 29: return "embarrassment"
	if r == 30: return "envy"
	if r == 31: return "excitement"
	if r == 32: return "fear"
	if r == 33: return "frustration"
	if r == 34: return "gratitude"
	if r == 35: return "guilt"
	if r == 36: return "happiness"
	if r == 37: return "hatred"
	if r == 38: return "hopefulness"
	if r == 39: return "humiliation"
	if r == 40: return "hurt"
	if r == 41: return "impatience"
	if r == 42: return "indifference"
	if r == 43: return "insecurity"
	if r == 44: return "irritation"
	if r == 45: return "jealousy"
	if r == 46: return "loneliness"
	if r == 47: return "love"
	if r == 48: return "nervousness"
	if r == 49: return "nostalgia"
	if r == 50: return "overwhelmed"
	if r == 51: return "paranoia"
	if r == 52: return "peacefulness"
	if r == 53: return "pride"
	if r == 54: return "rage"
	if r == 55: return "regret"
	if r == 56: return "relief"
	if r == 57: return "reluctance"
	if r == 58: return "remorse"
	if r == 59: return "resentment"
	if r == 60: return "resignation"
	if r == 61: return "sadness"
	if r == 62: return "satisfaction"
	if r == 63: return "scorn"
	if r == 64: return "shame"
	if r == 65: return "skepticism"
	if r == 66: return "smugness"
	if r == 67: return "somberness"
	if r == 68: return "surprise/shock"
	if r == 69: return "suspicion"
	if r == 70: return "sympathy"
	if r == 71: return "terror"
	if r == 72: return "uncertainty"
	if r == 73: return "unease"
	if r == 74: return "wariness"
	if r == 75: return "worry"

def town_generator():
	# name (and epithets)
	# alignment and type
	# size (small, large. if large, can raise dead, else not)
	# dangers (supernatural, mundane, )
	# government (feudal, council, secret council, eccliastical, colonial, dynasty, magical, military, syndicate )
	# notables (wealthy, powerful adventurers, bureaucrats, nobles)
	# law (vigilance of guard, lawfulness of citizens, )
	# spellcasting (commoner approach to mages, magic laws, criminal mages, wizard towers / organisations, mythals, )
	# markets (taxation, supply/demand, black market)
	# notable history
	# first impressions
	# interesting events (tournaments, celebrations, holidays, )
	# adventure sites (mountain, sewers, aqueducts, city of the dead, underwater ruins, ruins, )
	# architecture

def reputation_or_personality():
	r = rolld26()
	if r == 1: return "chaste"
	if r == 2: return "lustful"
	if r == 3: return "energetic"
	if r == 4: return "lazy"
	if r == 5: return "forgiving"
	if r == 6: return "vengeful"
	if r == 7: return "generous"
	if r == 8: return "selfish"
	if r == 9: return "honest"
	if r == 10: return "deceitful"
	if r == 11: return "just"
	if r == 12: return "arbitrary"
	if r == 13: return "merciful"
	if r == 14: return "cruel"
	if r == 15: return "modest"
	if r == 16: return "proud"
	if r == 17: return "prudent"
	if r == 18: return "reckless"
	if r == 19: return "spiritual"
	if r == 20: return "worldly"
	if r == 21: return "temperate"
	if r == 22: return "indulgent"
	if r == 23: return "trusting"
	if r == 24: return "suspicious"
	if r == 25: return "valorous"
	if r == 26: return "cowardly"

######################################################

#number_of_rooms = raw_input("How many rooms?")
number_of_rooms = 20
room_number = 1
print "#\tRoom Type"
while number_of_rooms != 0:
	number_of_rooms-=1
	chamber_or_room_contents = rolld20()
	if chamber_or_room_contents <= 12:
		print str(room_number)+"\tempty"
	if chamber_or_room_contents <= 14 and chamber_or_room_contents >= 13:
		print str(room_number)+"\tmonster only"
	if chamber_or_room_contents <= 17 and chamber_or_room_contents >= 15:
		print str(room_number)+"\tmonster and treasure"
	if chamber_or_room_contents == 18:
		print str(room_number)+"\tspecial"
	if chamber_or_room_contents == 19:
		print str(room_number)+"\ttrick/trap"
	if chamber_or_room_contents == 20:
		print str(room_number)+"\ttreasure"
		print "\t\t"
	room_number+=1