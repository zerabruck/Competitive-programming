arr =  [7,7,7,7,7,7]
dicto={}
stack=[]
sum=0
values=0

for i in arr:
    if(i in dicto.keys()):
        dicto[i]+=1
    else:
        dicto[i]=1
for i in dicto.values():
    stack.append(i)
stack.sort(reverse=True)
for i in range(len(stack)):
    sum+=stack[i]
    if(len(arr)//2<=sum):
        values=i+1
        break
    
        





print(values)

