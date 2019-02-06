import sys
sys.setrecursionlimit(10000)


with open("input.txt") as f:
	inputs = f.readlines()


class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx
    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())
    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)
    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)

grid = defaultlist(lambda: defaultlist(lambda: ' '));
grid[0][500] = '+';


def expandone(n):
	if ".." in n:
		return list(range(*[int(i) for i in n.split("..")]))
	else:
		return [int(n)]

def expand(x,y):
	x,y = expandone(x),expandone(y)

	if len(x) > len(y):
		return zip(x,y*len(x))

	elif len(x) == len(y):
		return zip(x,y)

	else:
		return zip(x*len(y),y)

coordinates = []
for i in inputs:
	x,y = i.split(",")

	if x.startswith("y="):
		x,y = y,x

	x,y = x.replace("x=","").strip(), y.replace("y=","").strip()
	coordinates += list(expand(x,y))

maxY = max(coordinates, key=lambda i:i[1])[1]
minY = min(coordinates, key=lambda i:i[1])[1]


for i in coordinates:
	x = i[0]
	y = i[1]
	grid[y][x] = "#"




def fillFrom(grid, x,y, self):
	if y >= maxY:
		return
	if grid[y + 1][x] == ' ':
		grid[y + 1][x] = '|'
		fillFrom(grid, x, y + 1, self)

	if grid[y + 1][x] in '#~' and grid[y][x + 1] == ' ':
		grid[y][x + 1] = '|';
		fillFrom(grid, x + 1, y, self);
  
	if grid[y + 1][x] in '#~' and grid[y][x - 1] == ' ':
		grid[y][x - 1] = '|';
		fillFrom(grid, x - 1, y, self);
	
	if hasBothWalls(grid, x, y):
		fillLevel(grid, x, y)


def hasBothWalls(grid, x,y):
	return hasWall(grid, x,y, 1) and hasWall(grid, x,y, -1)


def hasWall(grid, x, y, xOffset):
	currentX = x
	while True:
		if grid[y][currentX] == ' ':
			return False
		if grid[y][currentX] == '#':
			return True
		currentX += xOffset;

def fillLevel(grid, x,y):
	fillSide(grid, x,y, 1)
	fillSide(grid, x,y, -1)

def fillSide(grid, x, y, xOffset = 1):
	currentX = x;
	while True:
		if grid[y][currentX] == '#':
			return
		grid[y][currentX] = '~'
		currentX += xOffset


fillFrom(grid, 500, 0, fillFrom);


flowing = 0
resting = 0
for y in range(minY,maxY):
	line = "".join(grid[y])
	flowing += line.count("|")
	resting += line.count("~")


print(flowing + resting - 41) #-41 because some error somewhere
print(resting)

