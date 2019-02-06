

#475 first occurence
#503 first repeat

#476
#504

values = {0: 181485, 1: 177416, 2: 173910, 3: 167475, 4: 164424, 5: 164079, 6: 163631, 7: 163248, 8: 167090, 9: 168562, 10: 171588, 11: 172852, 12: 174900, 13: 176012, 14: 182574, 15: 187272, 16: 193888, 17: 199167, 18: 203648, 19: 204832, 20: 210504, 21: 210824, 22: 207282, 23: 205320, 24: 204125, 25: 197316, 26: 192984, 27: 188914}


# 1000000000 minutes
totaltime = 1000000000
#474 minutes setup time
setuptime = 475
timeaftersetup = totaltime - setuptime

cycles = timeaftersetup//28
rest = timeaftersetup%28

print(values[rest])

#210824

exit()


#tests to get the above constants
with open("input.txt") as f:
	inputs = f.readlines()



matrix = []
for line in inputs:
	matrix.append([])
	for i in line:
		if i != "\n":
			matrix[-1].append(i)

def stringmatrix(matrix):
	return "\n".join(["".join(i) for i in matrix])

def printmatrix(matrix):
	print(stringmatrix(matrix))

def adjacent(matrix,x,y):
	res = []
	try: res.append(matrix[y][x+1])
	except IndexError: pass
	try: 
		if x>0: res.append(matrix[y][x-1])
	except IndexError: pass
	try: res.append(matrix[y+1][x])
	except IndexError: pass
	try: 
		if y>0: res.append(matrix[y-1][x])
	except IndexError: pass
	try: 
		if y>0 and x>0: res.append(matrix[y-1][x-1])
	except IndexError: pass
	try: 
		if x>0: res.append(matrix[y+1][x-1])
	except IndexError: pass
	try: 
		if y>0: res.append(matrix[y-1][x+1])
	except IndexError: pass
	try: res.append(matrix[y+1][x+1])
	except IndexError: pass

	return str(res)

def generation(matrix):
	newmatrix = [[" "]*len(matrix[0]) for i in range(len(matrix))]

	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			adj = adjacent(matrix,x,y)
			if matrix[y][x] == "." and adj.count("|") >= 3:
				newmatrix[y][x] = "|"
			elif matrix[y][x] == "|" and adj.count("#") >= 3:
				newmatrix[y][x] = "#"
			elif matrix[y][x] == "#" and ("|" not in adj or "#" not in adj):
				newmatrix[y][x] = "."
			else:
				newmatrix[y][x] = matrix[y][x]
	return newmatrix


for i in range(1000000):
	matrix = generation(matrix)
	string = stringmatrix(matrix)
	print(string)
	wood = string.count("|")
	lumberyard = string.count("#")
	print(wood*lumberyard)

	if i > 475:
		if wood*lumberyard not in values.values():
			exit(wood*lumberyard)
