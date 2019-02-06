
import colorama
colorama.init()

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
		colisions = []
		for i in carts:
			if self.x == i.x and self.y == i.y and self != i:
				colisions.append(i)
		if len(colisions) != 0:
			colisions.append(self)
		return colisions

	def __str__(self):
		return "{},{} {}".format(self.x,self.y,self.direction)

	def __repr__(self):
		if self.direction == "right":
			return ">"
		elif self.direction == "left":
			return "<"
		elif self.direction == "down":
			return "v"
		else:
			return "^"

	# def __str__(self):
		# return "{} {} {}".format(self.x,self.y,self.direction)

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
					print(colorama.Fore.RED + repr(i),end="")
					print(colorama.Style.RESET_ALL,end="")
					break

			else:
				print(track[x][y],end="")
		print()

# printtracks(rails,carts)

while True:
	for i in carts:
		i.move(rails)

	colisions = []
	for i in carts:
		n = i.collide(carts)
		if len(n) != 0:
			colisions.append(n)

	# if len(colisions) != 0:
		# print(colisions[0][0].x,colisions[0][0].y)
		# input()

	for i in colisions:
		for j in i:
			if j in carts:
				carts.remove(j)

	# print(colisions)

	# printtracks(rails,carts)
	print([str(i) for i in carts])

	if len(carts) <= 1:
		for i in carts:
			i.move(rails)
		printtracks(rails,carts)
		print(carts[0].x, carts[0].y)
		exit()


#116, 98
#98,117
#116,97
#117,98
#145,88 <--


#multithreaded max

# import threading

# arr = [1,3,5,2,9,7,5,8]

# class findmax(threading.Thread):
# 	def __init__(self,arr):
# 		self.value = None
# 		self.arr = arr
# 		super().__init__()
# 		self.start()


# 	def run(self):
# 		if len(self.arr) == 1:
# 			self.value = self.arr[0]
# 			return

# 		middle = len(self.arr)//2
# 		left = self.arr[:middle]
# 		right = self.arr[middle:]

# 		leftthread = findmax(left)
# 		rightthread = findmax(right)

# 		leftthread.join()
# 		rightthread.join()

# 		self.value = max(leftthread.value,rightthread.value)
# 		return


# t = findmax(arr)
# t.join()
# print(t.value)