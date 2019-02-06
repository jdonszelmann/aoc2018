from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()



coordinates = []

for i in inputs:
	coordinates.append(tuple([int(j.strip()) for j in i.split(",")]))



def distance(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y2-y1)


res = {key:[0,False] for key in range(len(inputs))}


r = 1000


for y in range(-r,r):
	for x in range(-r,r):
		closest = 1e100
		closestpoint = None
		claims = 0
		for index,i in enumerate(coordinates):
			d = distance(x,y,i[0],i[1])
			if d < closest:
				closest = d
				closestpoint = index
				claims = 1
			elif d == closest:
				claims+=1
		if claims != 1:
			continue

		res[closestpoint][0] += 1
		if x == r-1 or x == -r or y == r-1 or y == -r:
			res[closestpoint][1] = True

	print(y)

noninfinite = {key:item for key,item in res.items() if not item[1]}

values = list(noninfinite.values())
print(max(values)[0])