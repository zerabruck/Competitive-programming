


pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
stack=[]

for i in popped:
    if(i in pushed):
        while(True):
            if(pushed[0]==i):
                pushed.remove(i)
                break
            else:
                stack.append(pushed[0])
                pushed.remove(pushed[0])
    elif(i ==stack[-1]):
        stack.pop(-1)
    else:
        print(False)
        break
print(stack)