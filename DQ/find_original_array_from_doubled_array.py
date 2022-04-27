
changed = [0,0,0,2,2,0]
length=len(changed)
result=[]
changed.sort()


if(len(changed)==0 or len(changed)%2!=0):
    result=[]
while(True):
    if(len(changed)==0):
        break
    value=changed.pop(0)
    try:
        changed.remove(value*2)
        result.append(value)
    except:
        result=[]
        break
    # if(value/2 in changed):
    #     changed.remove(value//2)
    #     result.append(value//2)
    # else:
    #     result=[]
    #     break

if(len(result)==length//2):
    result=result
else:
    result=[]


print(result)