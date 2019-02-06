
with open("input.txt") as f:
	inputs = f.read().strip()

scores = [3,7]
resscores = []

elve1 = 0
elve2 = 1


while True:
	for i in str(scores[elve1] + scores[elve2]):
		if len(scores) >= int(inputs):
			resscores.append(int(i))
		if len(resscores) == 10:
			print("".join((str(i) for i in resscores)))
			exit()
		scores.append(int(i))


	elve1 += (1 + scores[elve1])
	elve1 %= len(scores)
	elve2 += (1 + scores[elve2])
	elve2 %= len(scores)

	# print(elve1)
	# print(elve2)
	# input()