from functools import reduce


with open("input.txt") as f:
	inputs = f.readlines()


# print([
# 	i for i in list(
# 		map(
# 			lambda x: [
# 				int(i) for i in x.replace("#","").replace("@",",").replace("x",",").replace(":",",").replace(" ","").split(",") + [False]
# 			],
# 			inputs
# 		)
# 	) 
# 	if reduce(
# 		lambda acc,j: False if (
# 			lambda x1,y1,w1,h1,x2,y2,w2,h2: x2 < x1 + w1 and y2 < y1 + h1 and x2 + w2 > x1 and y2 + h2 > y1
# 			)(
# 				*i[1:-1], *j[1:-1]
# 			) 
# 			and i[0] != j[0] else acc,
# 		list(
# 			map(
# 				lambda x: [
# 					int(i) for i in x.replace("#","").replace("@",",").replace("x",",").replace(":",",").replace(" ","").split(",") + [False]
# 				],
# 				inputs
# 			)
# 		),
# 		True
# 		)
# 	][0][0]
# )

print([i for i in list(map(lambda x: [int(i) for i in x.replace("#","").replace("@",",").replace("x",",").replace(":",",").replace(" ","").split(",") + [False]],inputs)) if reduce(lambda acc,j: False if (lambda x1,y1,w1,h1,x2,y2,w2,h2: x2 < x1 + w1 and y2 < y1 + h1 and x2 + w2 > x1 and y2 + h2 > y1)(*i[1:-1], *j[1:-1]) and i[0] != j[0] else acc,list(map(lambda x: [int(i) for i in x.replace("#","").replace("@",",").replace("x",",").replace(":",",").replace(" ","").split(",") + [False]],inputs)),True)][0][0])
