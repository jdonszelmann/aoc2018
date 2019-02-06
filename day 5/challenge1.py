

with open("input.txt") as f:
	inputs = f.read()

def react(inp):
	lastlen = len(inp)
	for _ in iter(int,1):
		for i in range(len(inp)-1):
			if i > len(inp) - 2:
				break

			if inp[i] == inp[i+1].swapcase():
				inp.pop(i)
				inp.pop(i)


		if len(inp) == lastlen:
			break

		lastlen = len(inp)

	return len(inp)

print(react(list(inputs)))



