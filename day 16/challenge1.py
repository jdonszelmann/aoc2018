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
			count += 1
	return count

def chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]

threeopcodes = 0
for i in chunks(inputs,4):
	if tester(*i[:-1]) >= 3:
		threeopcodes+=1
print(threeopcodes)