s = " 3+5 / 2 "
stack=[]
counter=0
while(True):
    if(counter==len(s)):
        break
    if(s[counter]!=' '):
        if(s[counter]=="*"):
            value=stack.pop(-1)
            value2=s[counter+1]
            value3=value * value2
            value.append(value3)
            counter+=2
            continue
        elif(s[counter]=="/"):
            value=stack.pop(-1)
            value2=s[counter+1]
            value3=value // value2
            value.append(value3)
            counter+=2
            continue
        else:
            try:
                value.append(int(s[counter]))
                counter+=1
            except:
                value.append(s[counter])
                counter+=1
        

while(True):
    if(len(value)==1):
        break
    value_1=value.pop(0)
    value_2=value.pop(1)
    value_3=value.pop(2)
    if(value_2=="+"):
       value_4= value_1 + value_2
       value.insert(0,value_4)
    elif(value_2=="-"):
       value_4= value_1 - value_2
       value.insert(0,value_4)