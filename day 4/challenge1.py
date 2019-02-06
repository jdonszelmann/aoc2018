from functools import reduce
import re


with open("input.txt") as f:
	inputs = f.readlines()




# print(
# 	(
# 		lambda oldentries:[
# 			(
# 				lambda entries,guard:[
# 					(
# 						lambda lst:lst.index(
# 							max(lst)
# 						)
# 					)(
# 						[
# 							sum(
# 								[
# 									1 for j in list(
# 										map(
# 											lambda i:[
# 												i[0]%60,i[1]%60
# 											],list(
# 												filter(
# 													lambda i: i[2] == guard, 
# 													entries
# 												)
# 											)
# 										)
# 									) 
# 									if (lambda range,number: number >= range[0] and number < range[1])(j,i)
# 								]
# 							)
# 							for i in range(60)
# 						]
# 					)*guard
# 				][0]
# 			)(
# 				oldentries,
# 				(
# 					lambda res: max(res,key=res.get)
# 				)(
# 					{	
# 						key:len(item) 
# 						for key,item in reduce(
# 							lambda acc,val:[
# 								acc,
# 								list(
# 									map(
# 										lambda i:[
# 											0,
# 											acc[
# 												val[1]
# 											].add(
# 												len(acc[
# 														val[1]
# 													]
# 												)
# 											)
# 										][0], 
# 										range(val[1])
# 									)
# 								)
# 							][0],
# 							list(map(lambda i:[abs(i[0]-i[1]),i[2]], oldentries)),
# 							{i[1]:set() for i in list(map(lambda i:[abs(i[0]-i[1]),i[2]], oldentries))}
# 						).items()
# 					}
# 				)
# 			)
# 		][0]
# 	)(
# 		[
# 			[i[0],j[0],i[2]] 
# 			for i,j in (
# 				lambda i:zip(i[::2],i[1::2])
# 			)(
# 				list(
# 					filter(
# 						lambda i: i[1] != "start",
# 						reduce(
# 							lambda acc,val:[
# 								val.append(acc[0]) if val[1] != "start" else 0,
# 								[val[2] if val[1] == "start" else acc[0], acc[1] + [val]] 
# 							][1],
# 							list(
# 								map(
# 									lambda i: [i[0],"start",i[1]] if type(i[1]) == int else i, 
# 									map(
# 										lambda i: [i[0],int(re.split(r"#(\d+)",i[1])[1])] if "#" in i[1] else i, 
# 										sorted(
# 											list(
# 												map(
# 													lambda i:[
# 														(
# 															lambda year,month,day,hour,min: int(min) + (int(hour) + (int(day) + sum([31,28,31,30,31,30,31,31,30,31,30,31][0:int(month)]) + 365*int(year))*24)*265 
# 														)(*i[:-1]),
# 														i[-1]
# 													], [
# 														re.split(r"\[(\d)+-(\d+)-(\d+) (\d+):(\d+)\] (.*)\n",i)[1:-1]
# 														for i in inputs 
# 													]
# 												)
# 											), key = lambda i:i[0]
# 										)
# 									)
# 								)
# 							),
# 							[None,[]]
# 						)[1]
# 					)
# 				)
# 			)
# 		]
# 	)
# )

print((lambda oldentries:[(lambda entries,guard:[(lambda lst:lst.index(max(lst)))([sum([1 for j in list(map(lambda i:[i[0]%60,i[1]%60],list(filter(lambda i: i[2] == guard, entries)))) if (lambda range,number: number >= range[0] and number < range[1])(j,i)])for i in range(60)])*guard][0])(oldentries,(lambda res: max(res,key=res.get))({key:len(item) for key,item in reduce(lambda acc,val:[acc,list(map(lambda i:[0,acc[val[1]].add(len(acc[val[1]]))][0], range(val[1])))][0],list(map(lambda i:[abs(i[0]-i[1]),i[2]], oldentries)),{i[1]:set() for i in list(map(lambda i:[abs(i[0]-i[1]),i[2]], oldentries))}).items()}))][0])([[i[0],j[0],i[2]] for i,j in (lambda i:zip(i[::2],i[1::2]))(list(filter(lambda i: i[1] != "start",reduce(lambda acc,val:[val.append(acc[0]) if val[1] != "start" else 0,[val[2] if val[1] == "start" else acc[0], acc[1] + [val]] ][1],list(map(lambda i: [i[0],"start",i[1]] if type(i[1]) == int else i, map(lambda i: [i[0],int(re.split(r"#(\d+)",i[1])[1])] if "#" in i[1] else i, sorted(list(map(lambda i:[(lambda year,month,day,hour,min: int(min) + (int(hour) + (int(day) + sum([31,28,31,30,31,30,31,31,30,31,30,31][0:int(month)]) + 365*int(year))*24)*265 )(*i[:-1]),i[-1]], [re.split(r"\[(\d)+-(\d+)-(\d+) (\d+):(\d+)\] (.*)\n",i)[1:-1]for i in inputs ])), key = lambda i:i[0])))),[None,[]])[1])))]))