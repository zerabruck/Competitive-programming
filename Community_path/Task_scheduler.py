tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]

n = 2

answers=[]
dic_t={}

for i in tasks:
    if(i not in dic_t.keys()):
        dic_t[i]=1
    else:
        dic_t[i]+=1

print(dic_t)

point=len(dic_t.keys())
while(point!=0):
    
    if(point<=n):
        value=n-point
        for i in dic_t.keys():
            if(dic_t[i]!=0):
                answers.append(dic_t[i])
                dic_t[i]-=1
            else:
                point-=1 
        print('hi')      
        for j in range(value):
            answers.append(0)
    else:
        for i in dic_t.keys():
            if(dic_t[i]!=0):
                answers.append(dic_t[i])
                dic_t[i]-=1
            else:
                point-=1

        
print(answers)

































# tasks.sort()

# inital=0
# counter=n+1
# prev=tasks[0]
# answers.append(tasks[0])

# for i in range(1,len(tasks)):
    
#     print(answers)
#     print(tasks[i])
#     if(prev==tasks[i] and counter>=len(answers)):
#         value=counter-len(answers)
#         for j in range(value):
#             answers.append(0)
        
        
#         answers.append(tasks[i])
#         counter+=value+1
#     elif(prev==tasks[i]):
        
#         if(answers[counter]!=0):
#             counter+=1
#             continue
#         else:
#             answers[counter]=tasks[i]
#         counter+=n+1
#     elif(prev!=tasks[i]):
#         counting=inital
#         while(True):
#             if(counting==len(answers)):
#                 answers.append(tasks[i])
#                 break

#             elif(answers[counting]==0):
#                 answers[counting]=tasks[i]
#                 break
#             counting+=1
#         inital=counting
#         counter=inital+n+1
#         prev=tasks[i]
        




# print(answers)
# print(len(answers))
            



        












































# prev=0
# initial=0
# counter=initial
# for i in range(len(tasks)):
#     print(answers)
    
    
    
#     if(prev==0):
        
#         answers.append(tasks[i])
#         initial+=1
#         prev=tasks[i]
#         counter=initial

       
#     elif(prev==tasks[i]):
        
#         if(len(answers)-1>counter):
#                 if(answers[counter]!=0):
#                     counter+=1
                    
#                 else:
#                     answers[counter]=tasks[i]
#                     counter+=n
                     
                
#         else:
#             for i in range(n):
#                 answers.append(0)
#             answers.append(tasks[i])
#             counter+=n+1

            
        
       
#     elif(prev!=tasks[i]):
#         while(True):
#             if(initial==len(answers)):
#                 answers.append(tasks[i])
#                 initial+=1
#                 counter=initial
#                 break
#             elif(answers[initial]==0):
#                 answers[initial]=tasks[i]
#                 initial+=1
#                 counter=initial
#                 break
            
#             initial+=1
#         prev=tasks[i]
# print(answers)

        
        
            





    



