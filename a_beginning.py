import pickle
print("Sonic 25 - A text adventure by ImANoob")
print("--------------------------------------")
try:
	save = pickle.load(open("sonic25.save"))
except:
	save = {"rings":0,"levelid":0}
print("Begin? (y/N):")
if raw_input("> ").lower()[0] != "y":
	print("Goodbye!")
	exit()
