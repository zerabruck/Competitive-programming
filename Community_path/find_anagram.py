s="cbaebabacd"
p="abc"

new_p=[i for i in p]

reuslt=[]

for i in range(len(p)):
    if(s[i] in new_p):
        new_p.remove(s[i])
        
if(len(new_p)==0):
    reuslt.append(0)
for i in range(len(p),len(s)-len(p)+1):
    print(i)
   
    if(s[i-len(p)] in p):
        new_p.append(s[i-len(p)])
    
    if(s[i] in new_p):
        new_p.remove(s[i])

    print('0000')
    print(new_p)
        
    if(len(new_p)==0):
        reuslt.append(i-len(p)+1)
        
        
print(reuslt)