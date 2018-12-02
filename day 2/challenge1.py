from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()


# res = reduce(lambda acc, val: val * acc,
# 	reduce(
# 		lambda acc, val:list(
# 			map(
# 				lambda x,y: x + y,
# 				acc, 
# 				(
# 				 	1 if 2 in (val.count(l) for l in set(val)) else 0,
# 				 	1 if 3 in (val.count(l) for l in set(val)) else 0
# 				)
# 			)
# 		), 
# 		(i for i in inputs), 
# 		[0,0]
# 	)
# )

print(reduce(lambda acc,val:val*acc,reduce(lambda acc, val:list(map(lambda x,y: x + y,acc, (1 if 2 in (val.count(l) for l in set(val)) else 0,1 if 3 in (val.count(l) for l in set(val)) else 0))),(i for i in inputs),[0,0])))