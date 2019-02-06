import re
import numpy
import decimal
import matplotlib.pyplot as plt
import matplotlib.animation as animationplot
import sys,os

with open("input.txt") as f:
	inputs = f.readlines()

def remap(value, src, dst):

	s0, s1 = src
	t0, t1 = dst
	S = s1 - s0
	T = t1 - t0
	return t0 + ((value - s0) / S) * T

def plot(points):

	a = numpy.zeros((25,100))

	for i in points:
		x = remap(i[1],(100,150),(0,25))#top/bottom
		y = remap(-i[0],(-80,-200),(-25,75))#left/right
		if x > a.shape[0]-1 or y > a.shape[1]-1 or x < 0 or y < 0:
			continue
		a[int(x),int(y)] = 1

	print("|" + "-"*100 + "|\n|",end="")
	for x in range(25):
		for y in range(100):
			print(" " if a[x,y] == 0 else "#",end="")
		print("|\n|",end="")
	print("-"*100 + "|")

coordinates = []
for i in inputs:
	res = re.split(r"<(.*?), (.*?)>",i)
	x,y = res[1:3]
	vx,vy = res[4:6]
	coordinates.append([int(x),int(y),int(vx),int(vy)])

iterations = 0

for i in range(10105):
	for i in coordinates:
		i[0] += i[2]
		i[1] += i[3]

	iterations+=1
plot(coordinates)
print(iterations)

