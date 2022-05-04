
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
mapped={}
for i in range(len(position)):
    mapped[position[i]]=speed[i]
    
position.sort()

stack=position.copy()

for i in range(target):
    for i in range(len(position)):
        stack[i]=stack[i]+mapped[position[i]]

count=len(stack)-1
while(True):
    if(count==0):
        break
    print(count)
    if(stack[count]<stack[count-1]):
        stack.pop(count-1)
        
    count-=1      
        
print(stack)