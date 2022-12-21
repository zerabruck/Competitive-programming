# Enter your code here. Read input from STDIN. Print output to STDOUT

first_input=int(input())
second_input=input()
dicto={}
third=list(map(int,second_input.split()))

for i in third:
    if(i in dicto):
        dicto[i]+=1
    else:
        dicto[i]=1

for i in dicto:
    if(dicto[i]==1):
        print(i)
