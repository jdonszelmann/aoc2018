
with open("input.txt") as f:
	inputs = "(" + f.read()[1:-1] + ")"

print(inputs)

parsetree = []

index = 0

def accept(c):
	global index
	print(index,inputs[index], c)
	yes = inputs[index] in c
	index += 1
	return yes

def expr():
	global index

	res = []

	ci = index
	if accept("NESW"):
		res.append(inputs[index-1])
		ci1 = index
		e = expr()
		if e[0]:
			res.append(e[1])
			return True, res

		index = ci1
		b = bracketexpr()
		if b[0]:
			if len(b[1]) == 2 and type(b[1][0]) == list and type(b[1][1]) == list:
				res.extend(b[1])
			else:
				res.append(b[1])
			return True, res

		index = ci1

		e = expr()
		if e[0]:
			res.append(e[1])
			return True, res

		return True, res
	index = ci

	index = ci
	return False, None

def bracketexpr():
	global index
	ci = index
	res = []
	if accept("("):
		e = expr()
		if e[0]:
			res.append(e[1])
			ci1 = index
			if accept(")"):
				return True, res

			index = ci1

			if accept("|"):
				ci2 = index
				e1 = expr()
				if e1[0]:
					if accept(")"):
						res.append(e1[1])
						return True, res
				index = ci2
				if accept(")"):
					return True, []
	index = ci
	return False, None

b = bracketexpr()
if not b[0]:
	print("INVALID_EXPR")

def printtree(tree,depth=0):

	for i in tree:
		if type(i) == str:
			print(" "*depth, end="")
			print(i)
		else:
			printtree(i,depth+1)

def countdepth(tree, depth=0):
	largest = depth
	for i in tree:
		if type(i) == list:
			res = countdepth(i,depth+1)
			if res > largest:
				largest = res
	return largest

printtree(b[1])
print(countdepth(b[1]))