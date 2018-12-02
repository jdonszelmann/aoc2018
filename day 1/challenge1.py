with open("input.txt") as f:
	inputs = f.readlines()




print(eval("".join((i.strip() for i in inputs))))