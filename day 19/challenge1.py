import copy

with open("input.txt") as f:
	program = f.readlines()

opcodes = {}


def opcode(func):
	opcodes[func.__name__] = func
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
def seti(a,b,c,registers):
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


registers = [0,0,0,0,0,0]
ip = 0

ipreg = -1
decl = 0

while ip < len(program):
	instruction = program[ip]

	if instruction.startswith("#ip"):
		ipreg = int(''.join(ch for ch in instruction if ch.isdigit()))
		ip += 1
		decl += 1
		continue

	if ipreg != -1:
		registers[ipreg] = ip-decl

	opc, *args = [i for i in instruction.split(" ")]
	args = [int(i) for i in args]

	registers = opcodes[opc](*args, registers)
	print("ip={0:<5} {1} (args:{2}):{3} registers:{4}".format(ip-decl, opc,args,opcodes[opc].__name__,registers))
	
	if ipreg != -1:
		ip = registers[ipreg]+decl

	ip += 1
	input()

