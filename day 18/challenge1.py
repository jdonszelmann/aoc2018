
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


for i in range(10):
	matrix = generation(matrix)
	string = stringmatrix(matrix)
	print(string)
	wood = string.count("|")
	lumberyard = string.count("#")
	print(wood*lumberyard)
