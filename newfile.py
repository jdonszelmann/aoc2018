import os

path = os.path.dirname(os.path.realpath(__file__))

number = max([int(i.split(" ")[1]) for i in os.listdir(path) if os.path.isdir(i) and i.startswith("day")])

newdir = os.path.join(path,"day " + str(number+1))
os.mkdir(newdir)
os.chdir(newdir)

with open("input.txt","w") as f:
	pass

with open("challenge1.py","w") as f:
	f.write("""
with open("input.txt") as f:
	inputs = f.readlines()

		""")


with open("challenge2.py","w") as f:
	f.write("""
with open("input.txt") as f:
	inputs = f.readlines()

		""")

os.system("cd {}".format(newdir))