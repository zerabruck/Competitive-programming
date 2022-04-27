strs = ["a"]
dicto={}
every=[]
for i in strs:
    sum=sorted(i)
    
    if(f'{sum}' in dicto.keys()):
        dicto[f'{sum}'].append(i)
    else:
        dicto[f'{sum}']=[i]


for i in dicto.keys():
    every.append(dicto[i])
print(every)