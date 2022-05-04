# import math

# def distance(x,y):
#    return math.sqrt(x**2+y**2)


# storage = [[3,3],[5,-1],[-2,4]]
# k = 2

# counter=0
# stopper=0
# length=len(storage)
# while(True):
#     biggest=distance(storage[0][0],storage[0][1])
#     value=storage[0]
#     if(stopper==length):
#         break
#     for i in range(len(storage)-stopper):
#         if(distance(storage[i][0],storage[i][1])<=biggest):
#             biggest=distance(storage[i][0],storage[i][1])
#             value=storage[i]
#     storage.remove(value)
#     storage.append(value)
#     stopper+=1

# from turtle import distance


# points = [[1,3],[-2,2]]
# k=2
# dict_storage={}
# storage=[]
# returned_value=[]

# hello=[2,3,4,5,[4]]
# print (str(hello)[1:-1])


# for i in points:
#     value=distance(i[0],i[1])
#     if(value in dict_storage.keys()):
#         dict_storage[value].append(i)
#     else:
#         dict_storage[value]=[i]
#         storage.append(value)

# print(storage)

# for i in range(k):
#     returned_value.append((str(dict_storage[storage[i]]) [1:-1]))

# print(returned_value)

# dicto={}
# dicto['h']=3
# dicto['h']=4
# print(dicto)





# points =[[6,10],[-3,3],[-2,5],[0,2]]
# k=3
# storage=[]
# values=[]
# for i in points:
#     storage.append([distance(i[0],i[1]),i])
# count=0
# while(True):
#     smallest=storage[0]
    
#     if(storage[count][0] <=smallest[0]):
#         smallest=storage[count]

# for i in range(k):
#     values.append(storage[i][1])


# print(storage)
# print(values)

import math

def distance(x,y):
    return math.sqrt(x**2+y**2)


storage = [[1,3],[-2,2]]




counter=0
second_conunter=0
while(counter<len(storage)):  
    valu=counter
    second_conunter=counter
    while(second_conunter>=0):
        
        if(distance(storage[valu][0],storage[valu][1])<distance(storage[second_conunter][0],storage[second_conunter][1])):
            storage[second_conunter],storage[valu]=storage[valu],storage[second_conunter]
            valu=second_conunter
        second_conunter-=1
    counter+=1

print(storage)