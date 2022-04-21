def original(changed):
    values=[]
    
    if(len(changed)%2!=0 or len(changed)==0):
        return []
    lentght=len(changed)
    changed.sort()
    index=0
    counter=0
    for i in changed:
        if(i!=0):
            break        
        if (i ==0):
            counter+=1
            

        if(counter%2==0 and counter!=0):       
            values.append(0)  
    
    while(True):
        try:
            number=changed[index]*2
        except:
            
            if(lentght//2==len(values)):
                return values
               
                
            else:
                
                return []
        if(changed[index]==0):
            changed.remove(0)
            
            continue
        
        if(number in changed):
            
            values.append(changed[index])

            changed.remove(number)
        else:
            return []

        index+=1

print(original([0,0]))