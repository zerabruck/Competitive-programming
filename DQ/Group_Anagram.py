strs =["ddddddddddg","dgggggggggg"]
final_array=[]

# if(len(strs)==1):
#         print([[strs[0]]]) 
        

# while(True):
    
#     if(len(strs)==0):
#         break
    
#     element=strs.pop(0)
#     count=len(element)
    
#     tempo=[element]
    
    
#     for i in strs:
#         if (len(element)==len(i)):
#             for j in element:
#                 if( j in i):
#                     count-=1        
#             if (count==0):
#                 tempo.append(i)
#                 strs.remove(i)
#             count=3
            
            
          
#     final_array.append(tempo)



while(True):
    
    if(len(strs)==0):
        
        break
    
    element=strs.pop(0)
    count=len(element)
    
    tempo=[element]
    copying=strs.copy()
    
    
    
    for i in range(len(copying)):

        if (len(element)==len(copying[i])):
            tempo2=copying[i]
            for j in element:
               
                if( j in tempo2):
                    count-=1
                    tempo2=tempo2.replace(j,'')   
                         
            if (count==0):
                
                tempo.append(copying[i])
                strs.remove(copying[i])
                
                
            count=len(element)
       
    final_array.append(tempo)


print(final_array)