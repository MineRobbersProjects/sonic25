def beginning():
	print('Sonic: "Well, Tails, Knuckles, are you guys in?"')
	print('Tails: "Why not?"')
	print('Knuckles: "I guess so?"')
	print("----")
	print("Sonic, Tails, and Knuckles went off to go find Eggman.")
	save['levelid'] = 1
	raw_input("Press enter to continue.")
	handlelevel()
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
