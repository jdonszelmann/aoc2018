import numpy
from multiprocessing import Pool

with open("input.txt") as f:
	inputs = int(f.read())

def powerof(x,y):
	rackid = x + 10
	rackpower = (rackid * y)+inputs
	power = rackpower * rackid
	if power < 100:
		power = 0
	else:
		hundredsdigit = int(str(power)[-3])
		power = (hundredsdigit - 5) 
	
	return power

arr = numpy.zeros((300,300))
for x in range(0,300):
	for y in range(0,300):
		arr[x,y] = powerof(x,y)
		
def computeforsize(size):
	highest = -1e100
	highestx = None
	highesty = None
	for x in range(0,300-(size-1)):
		for y in range(0,300-(size-1)):
			
			#fassst
			powersum = numpy.sum(arr[x:x+size, y:y+size])
			#slowwww
			# powersum = 0
			# for ix in range(size):
			# 	for iy in range(size):
			# 		powersum += powerof(x+ix,y+iy)

			if powersum > highest:
				highest = powersum
				highestx = x
				highesty = y
				
	print(inputs,highestx,highesty,highest,size)
	return (highest,highestx,highesty,size)
	

if __name__ == "__main__":
	res = []
	
	with Pool() as pool:
		res = pool.map(computeforsize,range(1,301))


	print(res)
	print(max(res, key=lambda i:i[0]))


		
# 90, 201	, (89), 15