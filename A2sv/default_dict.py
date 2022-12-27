# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

loops = list(map(int,input().split()))
group_a = []
group_b = []

for i in range(loops[0]):
    group_a.append(input())
    
for i in range(loops[1]):
    group_b.append(input())
    

d=defaultdict(list)

for index,value in enumerate(group_a):
    d[value].append(index+1)
    
    
for i in group_b:
    if(i not in d):
        print(-1)
        
    else:
        string=''
        for i in d[i]:
            string += f'{i} '
            
            
        print(string)
         
    
        
        
    
    