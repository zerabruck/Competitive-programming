temperatures = [30,40,50,60]
answer=[]
for i in range(len(temperatures)):
    value=0
    if(i==len(temperatures)-1):
        answer.append(value)
        break
    temp=temperatures[i:]
    for j in range(len(temp)):
        if(temperatures[i]<temp[j]):
            value=j 
            answer.append(value)
            break
        elif(j==len(temp)-1):
            answer.append(value)




print(answer)