intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x:x[0])
results=[]
counter=0
while(len(intervals)!=0):
    second_counter=1
    valeing=intervals[counter][1]
    smaling=intervals[counter][0]
    while(second_counter<len(intervals)): 
        if(valeing>=intervals[second_counter][0]):
            if(valeing<intervals[second_counter][1]):
                valeing=intervals[second_counter][1]
            if(smaling>intervals[second_counter][0]):
                smaling=intervals[second_counter][0]
            intervals.remove(intervals[second_counter])   
            continue
        
        second_counter+=1
    
    results.append([smaling,valeing]) 
    intervals.remove(intervals[counter])
        

print(results)
    










