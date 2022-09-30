people = [5,1,4,2]

limit = 6
boat=0

people.sort()
i=0
print(people)
while(True):
    if(i==len(people)):
        break
    elif(i==len(people)-1):
        boat+=1
        break

    elif(people[i]<limit):
        if(people[i]+people[i+1]<=limit):
            boat+=1
            i+=2
        else:
            boat+=1
            i+=1
    else:
        boat+=1
        i+=1
    
print(boat)
