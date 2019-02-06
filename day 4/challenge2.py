import re
from functools import reduce


with open("input.txt") as f:
	inputs = f.readlines()


# print(
# 	(
# 		lambda entries:(
# 			(
# 				lambda res: 
# 					(lambda newentries:[
# 						(lambda guard:[
# 							guard * {
# 								key:(lambda lst:lst.index(max(lst)))(value)	
# 								for key,value in res.items()
# 							}[guard]
# 						][0])(
# 							max(newentries,key=newentries.get)
# 						)
# 					][0])(
# 						{
# 							key:max(value)	
# 							for key,value in res.items()
# 						}
# 					)	
# 			)(
# 				{
# 					key:[len(i) for i in item]
# 					for key,item in (
# 						lambda res:[
# 							[
# 								(
# 									lambda i,j: res[i[2]][j].add(len(res[i[2]][j]))
# 								)(i,j)
# 								for i in entries
# 								for j in range(i[0],i[1])
# 							],
# 							res
# 						][1]
# 					)(
# 						{
# 							i[2]:[set() for i in range(60)] 
# 							for i in entries
# 						}
# 					).items() 
# 				}
# 			)
# 		)
# 	)(
# 		list(
# 			map(
# 				lambda i:[i[0]%60,i[1]%60,i[2]],
# 				[
# 					[i[0],j[0],i[2]] 
# 					for i,j in (
# 						lambda i:zip(i[::2],i[1::2])
# 					)(
# 						list(
# 							filter(
# 								lambda i: i[1] != "start",
# 								reduce(
# 									lambda acc,val:[
# 										val.append(acc[0]) if val[1] != "start" else 0,
# 										[val[2] if val[1] == "start" else acc[0], acc[1] + [val]] 
# 									][1],
# 									list(
# 										map(
# 											lambda i: [i[0],"start",i[1]] if type(i[1]) == int else i, 
# 											map(
# 												lambda i: [i[0],int(re.split(r"#(\d+)",i[1])[1])] if "#" in i[1] else i, 
# 												sorted(
# 													list(
# 														map(
# 															lambda i:[
# 																(
# 																	lambda year,month,day,hour,min: int(min) + (int(hour) + (int(day) + sum([31,28,31,30,31,30,31,31,30,31,30,31][0:int(month)]) + 365*int(year))*24)*265 
# 																)(*i[:-1]),
# 																i[-1]
# 															], [
# 																re.split(r"\[(\d)+-(\d+)-(\d+) (\d+):(\d+)\] (.*)\n",i)[1:-1]
# 																for i in inputs 
# 															]
# 														)
# 													), key = lambda i:i[0]
# 												)
# 											)
# 										)
# 									),
# 									[None,[]]
# 								)[1]
# 							)
# 						)
# 					)
# 				]
# 			)
# 		)
# 	)
# )

print((lambda entries:((lambda res:(lambda newentries:[(lambda guard:[guard*{key:(lambda lst:lst.index(max(lst)))(value) for key,value in res.items()}[guard]][0])(max(newentries,key=newentries.get))][0])({key:max(value)for key,value in res.items()}))({key:[len(i) for i in item]for key,item in (lambda res:[[(lambda i,j: res[i[2]][j].add(len(res[i[2]][j])))(i,j) for i in entries for j in range(i[0],i[1])],res][1])({i[2]:[set() for i in range(60)] for i in entries}).items()})))(list(map(lambda i:[i[0]%60,i[1]%60,i[2]],[[i[0],j[0],i[2]] for i,j in (lambda i:zip(i[::2],i[1::2]))(list(filter(lambda i: i[1] != "start",reduce(lambda acc,val:[val.append(acc[0]) if val[1] != "start" else 0,[val[2] if val[1] == "start" else acc[0], acc[1] + [val]]][1],list(map(lambda i: [i[0],"start",i[1]] if type(i[1]) == int else i, map(lambda i: [i[0],int(re.split(r"#(\d+)",i[1])[1])] if "#" in i[1] else i,sorted(list(map(lambda i:[(lambda year,month,day,hour,min: int(min) + (int(hour) + (int(day) + sum([31,28,31,30,31,30,31,31,30,31,30,31][0:int(month)]) + 365*int(year))*24)*265 )(*i[:-1]),i[-1]], [re.split(r"\[(\d)+-(\d+)-(\d+) (\d+):(\d+)\] (.*)\n",i)[1:-1]for i in inputs])), key = lambda i:i[0])))),[None,[]])[1])))]))))
