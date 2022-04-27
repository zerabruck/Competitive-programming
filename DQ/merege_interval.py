intervals =[[1,4],[0,5]]
intervals.sort(key=lambda x:x[0])

final=[]

while(True):
    value=[]
    tempo=[]
    if(len(intervals)==0):
        break
    value=[]
    for j in range(intervals[0][0],intervals[0][1]+1):
       value.append(j)
    
    counter=0
    while(True):
        if(len(intervals)==0):
            break     
        if(intervals[counter][0] in value or intervals[counter][1] in value):
            tempo.append(intervals[counter][0])
            tempo.append(intervals[counter][1])
            intervals.pop(counter)
            continue
        counter+=1
        if(len(intervals)==counter):
            break
        
    tempo.sort()

 
    final.append([tempo[0],tempo[-1]])


print(final)






