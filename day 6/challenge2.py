from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()



coordinates = []

for i in inputs:
	coordinates.append(tuple([int(j.strip()) for j in i.split(",")]))



def distance(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y2-y1)




# r = 500

# count = 0

# for y in range(-r,r):
# 	for x in range(-r,r):
# 		s = 0
# 		for index,i in enumerate(coordinates):
# 			s += distance(x,y,i[0],i[1])
		
# 		if s < 10000:
# 			count += 1
		
# print(count)


print(
	(lambda r:(
			lambda f:(
				lambda a,b: a if a == b and a != 0 else "BIGGER"
			)(
				f(r),
				f(r+1)
			)
		)(
			(
				lambda r:reduce(
					lambda acc, xy:(
						lambda s:
							acc + 1 if s < 10000 else acc
					)(
						reduce(
							lambda acc1,val1:acc1 + (
								lambda x1,y1,x2,y2: abs(x1-x2) + abs(y2-y1)
							)(
								xy[0],xy[1],val1[0],val1[1]),[
									tuple([
											int(j.strip()) 
											for j in i.split(",")
									]) 
									for i in inputs
								],0
							)
					),
					((x,y) 
						for x in range(-r,r) 
						for y in range(-r,r)
					),
					0
				)
			)
		)
	)(500)
)
