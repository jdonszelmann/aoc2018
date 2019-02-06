
with open("input.txt") as f:
	inputs = [i.replace("\n","") for i in f.readlines()]

class Cart:
	def __init__(self,y,x,direction):
		self.x = x
		self.y = y
		self.direction = direction
		self.lastdirection = "left"

	def move(self,rails):
		if self.direction == "up":
			nxt = rails[self.y-1][self.x]
			self.y -= 1
			if nxt == "|":
				pass
			elif nxt == "\\":
				self.direction = "left"
			elif nxt == "/":
				self.direction = "right"
			elif nxt == "+":
				if self.lastdirection == "left":
					self.direction = self.lastdirection
					self.lastdirection = "straight" 
				elif self.lastdirection == "straight":
					self.lastdirection = "right"
				elif self.lastdirection == "right":
					self.direction = self.lastdirection
					self.lastdirection = "left"

		elif self.direction == "down":
			nxt = rails[self.y+1][self.x]
			self.y += 1
			if nxt == "|":
				pass
			elif nxt == "\\":
				self.direction = "right"
			elif nxt == "/":
				self.direction = "left"
			elif nxt == "+":
				if self.lastdirection == "left":
					self.direction = "right"
					self.lastdirection = "straight" 
				elif self.lastdirection == "straight":
					self.lastdirection = "right"
				elif self.lastdirection == "right":
					self.direction = "left"
					self.lastdirection = "left"
		elif self.direction == "left":
			nxt = rails[self.y][self.x-1]
			self.x -= 1
			if nxt == "-":
				pass
			elif nxt == "\\":
				self.direction = "up"
			elif nxt == "/":
				self.direction = "down"
			elif nxt == "+":
				if self.lastdirection == "left":
					self.direction = "down"
					self.lastdirection = "straight" 
				elif self.lastdirection == "straight":
					self.lastdirection = "right"
				elif self.lastdirection == "right":
					self.direction = "up"
					self.lastdirection = "left"
		elif self.direction == "right":
			nxt = rails[self.y][self.x+1]
			self.x += 1
			if nxt == "-":
				pass
			elif nxt == "\\":
				self.direction = "down"
			elif nxt == "/":
				self.direction = "up"
			elif nxt == "+":
				if self.lastdirection == "left":
					self.direction = "up"
					self.lastdirection = "straight" 
				elif self.lastdirection == "straight":
					self.lastdirection = "right"
				elif self.lastdirection == "right":
					self.direction = "down"
					self.lastdirection = "left"

	def collide(self,carts):
		for i in carts:
			if self.x == i.x and self.y == i.y and self != i:
				print(self.x,self.y)
				exit()

	def __repr__(self):
		if self.direction == "right":
			return ">"
		elif self.direction == "left":
			return "<"
		elif self.direction == "down":
			return "v"
		else:
			return "^"

carts = []

for x in range(len(inputs)):
	for y in range(len(inputs[1])):
		j = inputs[x][y]
		if j == ">":
			carts.append(Cart(x,y,"right"))
		elif j == "<":
			carts.append(Cart(x,y,"left"))
		elif j == "v":
			carts.append(Cart(x,y,"down"))
		elif j == "^":
			carts.append(Cart(x,y,"up"))

rails = [i.replace(">","-").replace("<","-").replace("^","|").replace("v","|") for i in inputs]

def printtracks(track,carts):
	for x in range(len(track)):
		for y in range(len(track[0])):
			for i in carts:
				if i.x == y and i.y == x:
					print(i,end="")
					break
			else:
				print(track[x][y],end="")
		print()

printtracks(rails,carts)

while True:
	for i in carts:
		i.move(rails)

	for i in carts:
		i.collide(carts)

	printtracks(rails,carts)
	# input()