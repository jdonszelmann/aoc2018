
with open("input.txt") as f:
	inputs = f.readlines()


inputs = [(i.split(" ")[1],i.split(" ")[7]) for i in inputs]


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
		return self.name + "-->" + str([i.name for i in self.requirements])

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
		

print(">>>",first)

possibilities = first
done = []

while len(done) != 26:
	possibilities.sort(key=lambda f:f.name)
	current = possibilities.pop(0)
	current.done = True
	done.append(current)

	for i in things:
		if i.requires(current):
			print(">>",i)
			if i.requirementsdone() and not i.done and i not in possibilities:
				possibilities.append(i)

	if len(possibilities) == 0:
		possibilities = done

	print(current,possibilities)



print("".join((i.name for i in done)))