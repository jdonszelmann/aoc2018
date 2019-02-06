
with open("input.txt") as f:
	inputs = int(f.read())

highest = -1e100
highestx = None
highesty = None


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

for x in range(1,301-2):
	for y in range(1,301-2):
	
		powersum = 0
		for ix in range(3):
			for iy in range(3):
				powersum += powerof(x+ix,y+iy)

		if powersum > highest:
			highest = powersum
			highestx = x
			highesty = y
		print(x,y,powersum)

print(inputs,highestx,highesty,highest)