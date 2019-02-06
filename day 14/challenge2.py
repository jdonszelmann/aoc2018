
with open("input.txt") as f:
	inputs = f.read().strip()

scores = [3,7]

elve1 = 0
elve2 = 1

iterations = 0
while True:
	for i in str(scores[elve1] + scores[elve2]):
		if "".join((str(i) for i in scores[-len(inputs):])) == inputs:
			print(len(scores)-len(inputs))
			exit()
		scores.append(int(i))


	elve1 += (1 + scores[elve1])
	elve1 %= len(scores)
	elve2 += (1 + scores[elve2])
	elve2 %= len(scores)

	iterations+=1
	if iterations%10000==0:
		print(iterations)
	# print(elve1)
	# print(elve2)
	# input()