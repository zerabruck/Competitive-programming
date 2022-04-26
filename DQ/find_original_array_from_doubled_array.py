def original(changed):
    values=[] 
    if(len(changed)%2!=0 or len(changed)==0):
        return []
    
    changed.sort()
    index=-1
    while(True):
        if(len(changed)==0):
            return values
        if(changed[index]%2!=0):
            return []
        number=changed[index]//2
        changed.pop(-1)
        if(number in changed):
            print(changed)
            values.append(number)
            changed.remove(number)
        else:
            return []

print(original([0,0,4,6,8]))