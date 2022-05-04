sorte=[4,4,76,344,0,1,1]
counter=0
second_conunter=0
while(counter<len(sorte)):  
    valu=counter
    second_conunter=counter
    while(second_conunter>=0):
        
        if(sorte[valu]<sorte[second_conunter]):
            sorte[second_conunter],sorte[valu]=sorte[valu],sorte[second_conunter]
            valu=second_conunter
        second_conunter-=1
    counter+=1
print(sorte)