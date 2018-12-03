from functools import reduce

with open("input.txt") as f:
	inputs = f.readlines()


#ans=111935



print(reduce(lambda acc,val:acc+1 if val>1 else acc,map(lambda i: len(i),(lambda l: [item for sublist in l for item in sublist])(reduce(lambda acc, val: [acc[val[0]][val[1]].add(len(acc[val[0]][val[1]])),acc,][1],((x,y,i) for i in list(map(lambda x: [int(i) for i in x.replace("#","").replace("@",",").replace("x",",").replace(":",",").replace(" ","").split(",")[1:]],inputs))for x in range(int(i[0]),int(i[2])+int(i[0])) for y in range(int(i[1]),int(i[3])+int(i[1]))),[[set() for j in range(1000)] for i in range(1000)])))))