def beginning():
	dialogue("Sonic","Well, Taill, Knuckles, are you guys in?")
	# print('Sonic: "Well, Tails, Knuckles, are you guys in?"')
	print('Tails: "Why not?"')
	print('Knuckles: "I guess so?"')
	print("----")
	print("Sonic, Tails, and Knuckles went off to go find Eggman.")
	save['levelid'] = 1
	raw_input("Press enter to continue.")
	handlelevel()
def boss1():
	print("Eggman appears in front of our heroes.")
	print('Eggman: "Ho ho ho! You shall not defeat me!"')
	bosshandler("Eggman",8,2)
	print('Eggman: "I\'ll be back!"')
def end():
	print("Sonic, Tails, and Knuckles saved the day, and have become a little closer now.")
	print("The End.")
	credits()
	save['levelid'] = 0
	save['rings'] = 0
	saveData(save)
	exit()
def credits():
	print("Adapted from an idea by reddit user /u/neohylanmay")
	print("Code made by ImANoob (reddit user /u/kd2bwz2)")
	print("Goodbye!")
	raw_input("Press enter to exit.")
def bosshandler(name, hp, chance):
	print("{} has appeared.".format(name))
	hits = hp
	while hits >= 1:
		print("Remaining hits: {:>15}".format(str(hits)))
		if random.randint(1,chance) == 1:
			hits -= 1;
			print("The boss was hit!")
		else:
			print("The boss was not hit!")
		sleep(1)
