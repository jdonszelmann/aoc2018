from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()

for i,j in [(a,b) for a in inputs for b in inputs]: print("".join([a for a,b in zip(i,j) if a == b]) if reduce(lambda acc,item: acc + int(item[0] != item[1]),zip(i,j),0) == 1 else "",end="")
