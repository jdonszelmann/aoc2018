from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()


# reduce(lambda acc1,val1:
# 	[
# 		reduce(
# 			lambda acc, val: [
# 				[acc[0] + int(val) if acc[0] not in acc1[1] else acc[0],acc[0]],
# 				acc1[1].add(acc[0]),
# 				[print(acc[0]),exit()][0] if acc[0] == acc[1] and acc[0] != 0 else 0
# 			][0], 
# 			inputs,
# 			[acc1[0],0]
# 		)[0],
# 		acc1[1]
# 	],
# 	iter(int, 1),
# 	[0,set()]
# )

reduce(lambda acc1,val1:[reduce(lambda acc, val:[[acc[0] + int(val) if acc[0] not in acc1[1] else acc[0],acc[0]],acc1[1].add(acc[0]),[print(acc[0]),exit()][0] if acc[0] == acc[1] and acc[0] != 0 else 0][0],inputs,[acc1[0],0])[0],acc1[1]],iter(int, 1),[0,set()])

