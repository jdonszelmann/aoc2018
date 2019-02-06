
with open("input.txt") as f:
	inputs = f.read()


# inputiterator = iter((int(i) for i in inputs.split(" ")))

# def generatenode():
# 	numchildren = next(inputiterator)
# 	metaentries = next(inputiterator)

# 	children = []
# 	for i in range(numchildren):
# 		children.append(generatenode())

# 	meta = []
# 	for i in range(metaentries):
# 		meta.append(next(inputiterator))

# 	return (children,meta)


# def treesum(tree):
# 	s = sum(tree[1])
# 	for i in tree[0]:
# 		s += treesum(i)

# 	return s

# def prettyprint(tree,depth=0):
# 	print("--"*depth + str(tree[1]))

# 	for i in tree[0]:
# 		prettyprint(i,depth+1)

# tree = generatenode()
# prettyprint((tree))
# print(treesum(tree))


#---

# print(
# 	(lambda tree:
# 		(
# 			lambda f,tree:f(f,tree)
# 		)(
# 			lambda recursion,tree: sum(tree[1]) + sum([
# 				recursion(recursion, i)
# 				for i in tree[0]
# 			]),
# 			tree
# 		)
# 	)(
# 		(
# 			lambda iterator:(
# 				lambda f: f(f)
# 			)(
# 				(lambda recurse:
# 					(lambda m,c:
# 						(
# 							[
# 								recurse(recurse)
# 								for i in range(m)
# 							],
# 							[
# 								next(iterator) 
# 								for i in range(c)
# 							]
# 						)
# 					)(
# 						next(iterator),
# 						next(iterator)
# 					)
# 				)
# 			)
# 		)(
# 			iter((int(i) for i in inputs.split(" ")))
# 		)
# 	)
# )


print((lambda tree:(lambda f,tree:f(f,tree))(lambda recursion,tree: sum(tree[1]) + sum([recursion(recursion, i)for i in tree[0]]),tree))((lambda iterator:(lambda f: f(f))((lambda recurse:(lambda m,c:([recurse(recurse)for i in range(m)],[next(iterator) for i in range(c)]))(next(iterator),next(iterator)))))(iter((int(i) for i in inputs.split(" "))))))

