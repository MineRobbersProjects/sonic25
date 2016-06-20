def beginning():
	dialogue("Sonic","Well, Tails, Knuckles, are you guys in?")
	dialogue('Tails',"Why not?")
	dialogue('Knuckles',"I guess so?")
	print("----")
	print("Sonic, Tails, and Knuckles went off to go find Eggman.")
	save['levelid'] = 1
	go()
	handlelevel()
def boss1():
	print("Eggman appears in front of our heroes.")
	dialogue('Eggman',"Ho ho ho! You shall not defeat me!")
	bosshandler("Eggman",8,2)
	dialogue('Eggman',"I'll be back!")
	dialogue("Sonic","Pfft. Yeah right.")
	save["levelid"] = 2
	go()
	handlelevel()
def boss2():
	print("Our heroes are off having fun in Station Square when suddenly...")
	dialogue("???","Hohoho!")
	dialogue("Knuckles","Uh oh. It's Eggface again!")
	dialogue("Eggman","Who are you calling Eggface? I am Dr. Ivo Robotnik-")
	dialogue("Sonic","-the greatest scientific genius in the world. We already knew that, Egghead.")
	dialogue("Egghead","Hey! It's Egg- wait what?")
	dialogue("Sonic","Haha! Even the programmer agrees!")
	programmer("Yes, Egghead.")
	dialogue("Egghead","Oh, I'll get you for this, Sonic!")
	bosshandler("Egghead",8,1)
	dialogue("Egghead","Seriously? The programmer made EVERY HIT COUNT?!?!?!?!?!?!?!?!")
	programmer("Okay, I'm done.")
	dialogue("Sonic","Hahahahahahaha!")
	print("Although Tails is a little hurt and bruised, his state isn't so bad as to attract Sonic's attention.")
	save["levelid"] = 3
	go()
	handlelevel()
def boss3():
	print("Well, Sonic defeated Eggman. Tails is a little hurt however, and Knuckles is helping him heal, when all of a sudden...")
	dialogue("Sonic","Seriously? Try and be more creative than that!")
	print("Umm... okay... how about:\nAfter Sonic defeated Eggman, Knuckles helped Tails heal up from the bruises he incurred during Sonic's fight with Eggman, but something felt off...")
	dialogue("Sonic","When is Egghead going to show again? This is getting boring.")
	dialogue("Tails","Oww...")
	dialogue("Knuckles","Don't move!")
	print("Knuckles wrapped Tails's arm in a bandage.")
	bosshandler("Eggman",6,3,ambush=True)
	dialogue("Eggman","Why won't it work! Ugghhh!!!!!")
	print("Eggman flies away.")
	dialogue("Knuckles","Oww...")
	dialogue("Tails","OWWWWW!!!!!!!")
	print("Sonic didn't notice. He was too busy gloating.")
	dialogue("Sonic","Hell yeah! Eggman's the loser, I am the winner! Me 3, Eggman 0!")
	save['levelid'] = 4
	go()
	handlelevel()
def boss4():
	dialogue("Tails","Sonic, can we stop now?")
	dialogue("Sonic","No way! We gotta finally defeat Egghead once and for all.")
	bosshandler("Eggman",9,2,ambush=True)
	dialogue("Knuckles","You know, Sonic, Tails is really hurt right now, so maybe we should rest for a while.")
	dialogue("Sonic","No rest, gotta keep going!")
	sleep(1)
	dialogue("Tails","THAT'S IT!!!!! I'm sick and tired of Sonic being an insufferable prick! I have a headache, I can see 20 Sonics, and I have a splitting headache!")
	dialogue("Sonic","Also short term memory loss, but whatever! We have to defeat Egghead before he tries to kill everyone!")
	dialogue("Tails","UGGH!!!!!!!!!!")
	dialogue("Knuckles","Now look at what you've done! That's it! I'm outta here! Tails, do you want to come with me? We'll defeat Eggman at our own pace!")
	dialogue("Tails","Sure.")
	print("Sonic continues on, alone.")
	save["levelid"] = 5
	go()
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
def bosshandler(name, hp, chance, ambush=False):
	if ambush:
		print("{} has ambushed our heroes!".format(name))
	else:
		print("{} has appeared.".format(name))
	print("It will take {!s} hits to defeat {}'s machine.".format(hp,name))
	hits = hp
	while hits >= 1:
		if random.randint(1,chance) == 1:
			hits -= 1;
			print("{} was hit!".format(name))
			if hits > 0:
				print("Remaining hits: {:>15}".format(str(hits)))
		if hits > 0:
			sleep(1)
	print("{} has been defeated!".format(name))
