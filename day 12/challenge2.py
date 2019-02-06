
with open("input.txt") as f:
	inputs = f.readlines()

padding = 200
originalstate = list("."*padding + inputs[0].replace("initial state: ","").replace("\n","") + "."*padding)
zero = originalstate[padding]

rules = inputs[2:]


def match(state,index,rules):
	try:
		for i in rules:
			if (
				state[index-2] == i[0] and 
				state[index-1] == i[1] and
				state[index] == i[2] and
				state[index+1] == i[3] and
				state[index+2] == i[4]
				):
				# print("{} at {} ".format(i,index), end="")
				return i[9]

		return state[index]
	except IndexError:
		return state[index]

print("".join(originalstate))

lastcount = 0
for i in range(105):
	newstate = ["."]*len(originalstate)

	for j in range(len(originalstate)):
		newstate[j] = match(originalstate,j,rules)

	originalstate = newstate
	print("generation {}".format(i))
	print("".join(originalstate))
	# input()

	count = 0
	for i in range(-padding, len(originalstate)-padding):
		if originalstate[i+padding] == "#":
			count += i

	print(count, lastcount, abs(count-lastcount))
	lastcount = count




print((50000000000 - 99)*62 + 5629)

# 3099999999369
# 3099999999431
# 3099999999999
# 3099999999491


#dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait ip=192.168.1.160:::255.255.255.0
#dwc_otg.lpm_enable=0 console=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
	


