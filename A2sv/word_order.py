# Enter your code here. Read input from STDIN. Print output to STDOUT

dicto={}
first_input=int(input())
for i in range(first_input):
    inputs=input()
    if(inputs in dicto):
        dicto[inputs]+=1
    else:
        dicto[inputs]=1
        
print(len(dicto))
string=''
for i in dicto.values():
    string+=f"{i} "
    
print(string)
