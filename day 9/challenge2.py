from cll import *

with open("input.txt") as f:
	players, lastmarble = f.readlines()


lst = CircularDoublyLinkedList()
lst.insert_at_beg(Node(0))
player = 0
points = [0]*int(players)

for i in range(1,int(lastmarble)*100):
	player = (player + 1) % int(players) 

	if i%23 != 0:
		lst.rotate(2)
		lst.insert_at_beg(Node(i))
	else:
		score = i
		lst.rotaten(7)
		n = lst.get_node(0)
		lst.remove(n)

		score += n.data
		points[player] += score


print("points...", points, max(points))

