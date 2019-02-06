
with open("input.txt") as f:
	inputs = f.readlines()


inputs = [(i.split(" ")[1],i.split(" ")[7]) for i in inputs]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class req:


	def __init__(self,name):
		self.done = False
		self.requirements = []
		self.name = name


	def requires(self,other):
		return other in self.requirements

	def requirementsdone(self):
		for i in self.requirements:
			if not i.done:
				return False
		return True

	def __repr__(self):
		return self.name #+ "-->" + str([i.name for i in self.requirements])

things = []
for i in inputs:
	for j in things:
		if j.name == i[0]:
			break
	else:
		things.append(req(i[0]))
	for j in things:
		if j.name == i[1]:
			break
	else:
		things.append(req(i[1]))

for key,value in inputs:
	for i in things:
		if i.name == value:
			for x in things:
				if x.name == key:
					i.requirements.append(x)


first = []
for i in things:
	if len(i.requirements) == 0:
		first.append(i)
		


possibilities = first
done = []

elves = [(None,0)]*5

iterations = 0

while len(done) != len(things):
	possibilities.sort(key=lambda f:f.name)
	for n in range(len(elves)):
		if len(possibilities) == 0:
			break
		if elves[n][0] == None:
			p = possibilities.pop(0)
			elves[n] = [p,alphabet.index(p.name) + 60]

	running = True
	while running:

		print(elves,possibilities,done,iterations)
		# input()
		iterations += 1

		for i in range(len(elves)):		
			if elves[i][1] > 0:
				elves[i][1] -= 1
			elif elves[i][1] == 0 and elves[i][0] != None:
				elves[i][0].done = True
				done.append(elves[i][0])

				for j in things:
					if j.requires(elves[i][0]):
						if j.requirementsdone() and not j.done and j not in possibilities:
							possibilities.append(j)
				elves[i] = (None,0)

				running = False




steps = "".join((i.name for i in done))

print(steps,iterations)

