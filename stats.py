# Character stats, starting with primary attributes
# Primary Attributes start at 7 and go up from there.  Attribute points start at 38 and are adjusted later
class Character(object):
	name = ''
	attributePoints = 38
	strength = 7
	constitution = 7
	coordination = 7
	adaptation = 7
	perception = 7
	intelligence = 7
	willpower = 7
	presence = 7
	_attributes = ['name','attributePoints', 'strength', 'constitution', 'coordination', 'adaptation', 'perception', 'intelligence', 'willpower', 'presence']
	def __init__(self,name):
		assert self.valid_name(name)
		self.name = name
	def add_points(self):
		accepted = ['strength', 'constitution', 'coordination', 'adaptation', 'perception', 'intelligence', 'willpower', 'presence']
		accepted_dict = dict(enumerate(accepted, start=1))
		prompt = "\nAvailable Attributes:\n\n\t" + "\n\t".join("%d. %s"%n for n in accepted_dict.items())+"\n\n Make a selection: "
		attribute = False
		while attribute not in accepted:
			attribute = raw_input(prompt)
			try:
				attribute = accepted_dict[int(attribute)]
			except:
				print "Input was invalid.  Please enter either an attribute or its corresponding number. "
		amount = None
		'''Below: Depending on the number, this variable needs to subtract more or less from the attributePoints total.
				Target Number:	Attribute Point Cost
				UPDATE:  Got the attributePoints total to adjust accordingly.  However, I cannot get the
				attribute themselves to change correctly.  I can get the attribute to adjust if I turn == into +, but it
				adjusts by the amount instead of turning the new value into the value given.
			Additionally, I'll adjust other needed things like lowering stats and whatnot once I get this piece working.	
'''
		while type(amount) != int and self.attributePoints > 0:
			amount = int(raw_input("Raise to what number? "))
			if amount == 7:
				self.attributePoints -= 0
			elif amount >= 8 and amount < 16:			
				self.attributePoints -= amount -7
			elif amount == 16:
				self.attributePoints -= 10
			elif amount == 17:
				self.attributePoints -= 12
			elif amount == 18:
				self.attributePoints -= 14
			elif amount == 19:
				self.attributePoints -= 17
			elif amount == 20:
				self.attributePoints -= 20
			elif amount > 20:
				print "You must enter a number between 7 and 20. "
		self.__setattr__(attribute, self.__getattribute__(attribute) + amount - 7) #This is my problem area
	def __str__(self):
		return "\n".join("%s\t:\t%s"%(n, self.__getattribute__(n)) for n in self._attributes)
	@staticmethod
	def valid_name(name):
		if bool(name) and type(name) == str:
			return True
		else:
			return False
if __name__ == "__main__":
	running = True
	print "Create a character!  You have 38 (or more) points to assign to various attributes."
	name = ''
	while not Character.valid_name(name):
		name = raw_input("Please enter your character's name: ")
	CHAR = Character(name)
	OPTIONS_LIST =["Set Stats", "See current attributes", "Exit"]
	OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
	PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice: "
	while running:
		CHOICE = raw_input(PROMPT)
		try:
			CHOICE = int(CHOICE)
		except:
			pass
		if CHOICE in OPTIONS_DICT.keys():
			CHOICE = OPTIONS_DICT[CHOICE]
		if CHOICE == "Set Stats":
			CHAR.add_points()
		elif CHOICE == "See current attributes":
			print CHAR
		elif CHOICE == "Exit":
			running = False

'''# Secondary Attributes
# Secondary attributes are derivied from a combination of Primary Attributes and item modifications
luck = 13
#Starting luck is 13 as we will be running Intermediary level of setting
reaction = (adaptation + perception) /2
meleeDamageModifier = 0
stunThreshold = (strength+constitution+willpower)/3
knockoutThreshold = stunThreshold+10
damageResistance = 0
naturalResistance = 0
drugResistance = 0
#Breathing is in combat rounds
suspendBreathing = (constitution+willpower)/2

#This is for Melee Damage Modifier's calculation
#Need to figure out a way to easily have it add +1 for every 2 levels above 11 to infinity
if strength < 3:
	meleeDamageModifier = -6
elif strength < 5:
	meleeDamageModifier = -4
elif strength < 7:
	meleeDamageModifier = -2
elif strength < 9:
	meleeDamageModifier = -1
elif strength < 12:
	meleeDamageModifier = 0
elif strength < 14:
	meleeDamageModifier = 1
elif strength < 16:
	meleeDamageModifier = 2
elif strength < 18:
	meleeDamageModifier = 3
elif strength < 20:
	meleeDamageModifier = 4
elif strength < 22:
	meleeDamageModifier = 5
else:
	print "Number too big for testing"

#This is for Damage Resistance.  Intervals go up from 2 to infinity at ever 4th number.  I stopped when the book stopped
if strength+constitution < 6:
	damageResistance = 6
elif strength+constitution < 10:
	damageResistance = 4
elif strength+constitution < 14:
	damageResistance = 2
elif strength+constitution < 18:
	damageResistance = 1
elif strength+constitution < 22:
	damageResistance = 0
elif strength+constitution < 26:
	damageResistance = -1
elif strength+constitution < 30:
	damageResistance = -2
elif strength+constitution < 34:
	damageResistance = -3
elif strength+constitution < 38:
	damageResistance = -4
elif strength+constitution < 42:
	damageResistance = -5
else:
	print "Number too big for testing"
#The below is just a check to make sure it works.
#print "Damage Resistance: %i" %damageResistance
#

#Natural Resistance code. Code problem the same as Melee Damage Modifier

if constitution > 3:
	naturalResistance = 6
elif constitution > 5:
	naturalResistance = 4
elif constitution > 7:
	naturalResistance = 2
elif constitution > 9:
	naturalResistance = 1
elif constitution > 12:
	naturalResistance = 0
elif constitution > 14:
	naturalResistance = -1
elif constitution > 16:
	naturalResistance = -2
elif constitution > 18:
	naturalResistance = -3
elif constitution > 20:
	naturalResistance = -4
elif constitution > 22:
	naturalResistance = -5
'''
