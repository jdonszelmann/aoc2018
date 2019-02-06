import copy

with open("input.txt") as f:
	inputs = f.read()

		
units = [[j if j in ".#" else j + "200" for j in i ] for i in inputs.split("\n")]

def printunits(un, lstxy=[], lstxy2=[]):
	for y in range(len(un)):
		for x in range(len(un[0])):
			for i in lstxy:
				if (y,x) == i:
					print("!   ",end="")
					break
			else:
				for i in lstxy2:
					if (y,x) == i:
						print("@   ",end="")
						break
				else:
					print(un[y][x].ljust(4),end="")
		print()

def Etargets(un,x,y):
	targets = []

	for y in range(len(un)):
		for x in range(len(un[0])):
			if un[y][x].startswith("E"):
				if un[y+1][x] != "#":
					targets.append((y+1,x))
				if un[y-1][x] != "#":
					targets.append((y-1,x))
				if un[y][x+1] != "#":
					targets.append((y,x+1))
				if un[y][x-1] != "#":
					targets.append((y,x-1))
	return targets


def Gtargets(un,x,y):
	targets = []

	for y in range(len(un)):
		for x in range(len(un[0])):
			if un[y][x].startswith("G"):
				if un[y+1][x] != "#":
					targets.append((y+1,x))
				if un[y-1][x] != "#":
					targets.append((y-1,x))
				if un[y][x+1] != "#":
					targets.append((y,x+1))
				if un[y][x-1] != "#":
					targets.append((y,x-1))
	return targets

def coordinlist(x,y,lstxy):
	for i in lstxy:
		if (x,y) == i:
			return True
	return False	


def distance(un,x,y,a,b):
	todo = [(x,y)]
	had = []
	index = 0


	while True:
		newtodo = []
		index+=1

		if index > 100:
			return -1

		for current in todo:
			if current == (b,a):
				return index

			# printunits(un,todo+had,[(b,a),()])


			if current not in had:
				had.append(current)
				if un[current[0]+1][current[1]] == ".":
					newtodo.append((current[0]+1,current[1]))
				if un[current[0]-1][current[1]] == ".":
					newtodo.append((current[0]-1,current[1]))
				if un[current[0]][current[1]+1] == ".":
					newtodo.append((current[0],current[1]+1))
				if un[current[0]][current[1]-1] == ".":
					newtodo.append((current[0],current[1]-1))

		todo = newtodo

def adjacentto(x,y,a,b):
	if (x+1,y) == (a,b):
		return True
	if (x-1,y) == (a,b):
		return True
	if (x,y+1) == (a,b):
		return True
	if (x,y-1) == (a,b):
		return True

	return False

def path(un,x,y,a,b):
	todo = [(x,y)]
	had = []

	labels = {}

	index = 0

	while True:
		newtodo = []
		index+=1

		for current in todo:
			if index not in labels:
				labels[index] = [current]
			else:
				labels[index].append(current)

			if current == (b,a):
				route = [current]
				last = current
				while True:
					index -= 1
					if index < 2:
						return route
					adjecent = []
					try:
						for i in labels[index]:
							if adjacentto(*i,*last):
								adjecent.append(i)
					except KeyError:
						print(labels)
						raise

					i = min(adjecent, key=lambda i: i[0]*len(un[0]) + i[1])
					route.append(i)
					last = i
				return

			if current not in had:
				had.append(current)
				if un[current[0]+1][current[1]] == ".":
					newtodo.append((current[0]+1,current[1]))
				if un[current[0]-1][current[1]] == ".":
					newtodo.append((current[0]-1,current[1]))
				if un[current[0]][current[1]+1] == ".":
					newtodo.append((current[0],current[1]+1))
				if un[current[0]][current[1]-1] == ".":
					newtodo.append((current[0],current[1]-1))

		todo = newtodo

rounds = 0
try:
	while True:
		hadthisround = []
		for y in range(len(units)):
			for x in range(len(units[0])):
				if (y,x) in hadthisround:
					continue
				if units[y][x].startswith("G"):
					utype = units[y][x]
					targets = Etargets(units,x,y)
					units[y][x] = "."
				elif units[y][x].startswith("E"):
					targets = Gtargets(units,x,y) 
					utype = units[y][x]
					units[y][x] = "."
				else:
					continue

				if targets == []:
					units[y][x] = utype
					raise EOFError


				if not coordinlist(y,x,targets):

					mindist = 1e100
					mincoord = None
					for index,(a,b) in enumerate(targets):
						d = distance(units,y,x,b,a)
						if d == -1:
							continue
						if d < mindist:
							mincoord = (b,a)
							mindist =  d
						if d == mindist:
							if a*len(units[0]) + b < mincoord[1]*len(units[0]) + mincoord[0]:
								mincoord = (b,a)


					if mincoord == None:
						units[y][x] = utype
						continue

					p = path(units,y,x,*mincoord)
					nextpos = p[-1]

					# printunits(units,p)
					# print(nextpos)
					hadthisround.append(nextpos)
					units[nextpos[0]][nextpos[1]] = utype
					ny,nx = nextpos
				else:
					nx,ny = x,y
					hadthisround.append((y,x))
					units[y][x] = utype



				if units[ny][nx].startswith("G"):
					mattackloc = None
					attackhp = 1e100
					if units[ny-1][nx].startswith("E"):
						attackloc = (ny-1,nx)
						hp = int(units[ny-1][nx][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny][nx+1].startswith("E"):
						attackloc = (ny,nx+1)
						hp = int(units[ny][nx+1][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny][nx-1].startswith("E"):
						attackloc = (ny,nx-1)
						hp = int(units[ny][nx-1][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny+1][nx].startswith("E"):
						attackloc = (ny+1,nx)
						hp = int(units[ny+1][nx][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp

					if mattackloc != None:
						units[mattackloc[0]][mattackloc[1]] = "E" + str(attackhp-3)
						if attackhp-3 < 0:
							units[mattackloc[0]][mattackloc[1]] = "."	

				elif units[ny][nx].startswith("E"):
					mattackloc = None
					attackhp = 1e100
					if units[ny-1][nx].startswith("G"):
						attackloc = (ny-1,nx)
						hp = int(units[ny-1][nx][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny][nx+1].startswith("G"):
						attackloc = (ny,nx+1)
						hp = int(units[ny][nx+1][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny][nx-1].startswith("G"):
						attackloc = (ny,nx-1)
						hp = int(units[ny][nx-1][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp
					if units[ny+1][nx].startswith("G"):
						attackloc = (ny+1,nx)
						hp = int(units[ny+1][nx][1:])
						if hp <= attackhp:
							mattackloc = attackloc
							attackhp = hp

					if mattackloc != None:
						units[mattackloc[0]][mattackloc[1]] = "G" + str(attackhp-3)
						if attackhp-3 < 0:
							units[mattackloc[0]][mattackloc[1]] = "."

		rounds += 1
		printunits(units)
		# input(rounds)	

		print("--------")
except EOFError:
	pass

total = 0
for y in range(len(units)):
	for x in range(len(units[0])):
		if units[y][x].startswith("G") or units[y][x].startswith("E"):
			total += int(units[y][x][1:])

print(total,rounds,total * rounds)


# 197409
# 200270
# 
# 197616