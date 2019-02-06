import copy

with open("input.txt") as f:
	inputs = f.readlines()

opcodes = {}


def opcode(func):
	opcodes[func] = -1
	return func

@opcode
def addr(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] + registers[b]
	return registers

@opcode
def addi(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] + b
	return registers

@opcode
def mulr(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] * registers[b]
	return registers

@opcode
def muli(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] * b
	return registers

@opcode
def banr(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] & registers[b]
	return registers

@opcode
def bani(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] & b
	return registers

@opcode
def borr(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] | registers[b]
	return registers

@opcode
def bori(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a] | b
	return registers

@opcode
def setr(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = registers[a]
	return registers

@opcode
def bori(a,b,c,registers):
	registers = copy.copy(registers)
	registers[c] = a
	return registers

@opcode
def gtir(a,b,c,registers):
	registers = copy.copy(registers)
	if a > registers[b]:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers

@opcode
def gtri(a,b,c,registers):
	registers = copy.copy(registers)
	if registers[a] > b:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers

@opcode
def gtrr(a,b,c,registers):
	registers = copy.copy(registers)
	if registers[a] > registers[b]:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers

@opcode
def eqir(a,b,c,registers):
	registers = copy.copy(registers)
	if a == registers[b]:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers

@opcode
def eqri(a,b,c,registers):
	registers = copy.copy(registers)
	if registers[a] == b:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers

@opcode
def eqrr(a,b,c,registers):
	registers = copy.copy(registers)
	if registers[a] == registers[b]:
		registers[c] = 1
	else:
		registers[c] = 0
	return registers


def tester(src, instruction, dst):
	registersbefore = [int(i.strip()) for i in src.replace("Before: ","").replace("[","").replace("]","").split(",")]
	registersafter = [int(i.strip()) for i in dst.replace("After: ","").replace("[","").replace("]","").split(",")]
	opc, *args = [int(i) for i in instruction.split(" ")]
	count = 0
	for i in opcodes:
		if registersafter == i(*args,registersbefore):
			if opcodes[i] == -1:
				count += 1


	if count == 1:
		for i in opcodes:
			if registersafter == i(*args,registersbefore):
				if opcodes[i] == -1:
					opcodes[i] = opc

	return count


executors = {value:	key for key,value in opcodes.items()}


registers = [0,0,0,0]
for instruction in program:
	opc, *args = [int(i) for i in instruction.split(" ")]
	registers = executors[opc](*args, registers)
	print("{} (args:{}):{} registers:{}".format(opc,args,executors[opc].__name__,registers))
