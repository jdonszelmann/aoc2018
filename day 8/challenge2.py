from functools import reduce

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

# def prettyprint(tree,depth=0):
# 	print("--"*depth + str(tree[1]))

# 	for i in tree[0]:
# 		prettyprint(i,depth+1)

# def treevalue(tree):
# 	if len(tree[0]) == 0:
# 		value = sum(tree[1])
# 	else:
# 		value = 0
# 		for i in tree[1]:
# 			index = i-1
# 			if index > len(tree[0])-1 or index < 0:
# 				continue
# 			value += treevalue(tree[0][index])
# 	return value

# tree = generatenode()
# prettyprint((tree))
# print(treevalue(tree))

# ------

# print(
# 	(
# 		lambda t:(
# 			lambda f, tree: f(f, tree)
# 		)(
# 			lambda recursive, tree:
# 				sum(tree[1]) if len(tree[0]) == 0
# 				else reduce(
# 					lambda acc,val: 
# 						acc + recursive(recursive,tree[0][val-1]) 
# 						if not (val-1 > len(tree[0])-1 or val-1 < 0)
# 						else acc,
# 					tree[1],
# 					0
# 				)
# 			,t
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


print((lambda t:(lambda f, tree: f(f, tree))(lambda recursive, tree:sum(tree[1]) if len(tree[0]) == 0else reduce(lambda acc,val: acc + recursive(recursive,tree[0][val-1]) if not (val-1 > len(tree[0])-1 or val-1 < 0)else acc,tree[1],0),t))((lambda iterator:(lambda f: f(f))((lambda recurse:(lambda m,c:([recurse(recurse)for i in range(m)],[next(iterator) for i in range(c)]))(next(iterator),next(iterator)))))(iter((int(i) for i in inputs.split(" "))))))
