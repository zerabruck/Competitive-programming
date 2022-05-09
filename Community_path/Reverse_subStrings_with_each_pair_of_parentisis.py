s = "(u(love)i)"
stack=[]
tempo=''
cutting=None
closing=None
starting=None
finish=None
for i in range(len(s)):
    if(s[i]=='(' and starting==None ):
        starting=i
        
    elif(s[i]==')'):
        finish=i
  
new_s=s
s=new_s[starting:finish+1]

for i in range(len(s)):
    
    if(s[i]=='(' and cutting==None):
        cutting=i
    
        
    elif(cutting!=None and s[i]=='('):
        
        

        if(cutting+1!=i):
            stack.append(s[cutting+1:i])
        
        
        cutting=i

    elif(s[i]==')' and closing==None):
        
        if(len(stack)==0):
            resulting=s[cutting+1:i]
            resulting=resulting[::-1]
            resulting=new_s[:starting] +resulting +new_s[finish+1:]
            break
        valu=''
        
        if(cutting+1!=i):
            valu=s[cutting+1:i]


        
        reversed_string=valu[::-1]
        stack[-1]+=reversed_string
        
        closing=i
        
        
    elif(s[i]==')' and closing!=None):
        
        
        tempo=''
        if(closing+1!=i):
            tempo=s[closing+1:i]
        
        
        stack[-1]+=tempo
        valueing=stack.pop(-1)
        valueing=valueing[::-1]
        if(i==len(s)-1):
            
            valueing=new_s[:starting] +valueing +new_s[finish+1:]
            break
        stack[-1]+=valueing
        closing=i

        
print(valueing)
