s = "(]"
values=True
stack=[]
reference={"(":")","[":"]",'{':'}'}

for i in s:
    if(i in reference.keys()):
        stack.append(i)
        
    else:
        value=stack.pop(-1)
        if(reference[value]==i):
            print(i)
            continue
        else:
            
            values=False
            break
if(len(stack)==0):
    values=True
else:
    values=False

print(values)
