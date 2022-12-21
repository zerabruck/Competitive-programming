# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
array=input().split()
A=set(input().split())
B=set(input().split())

result=0
for i in array:
    if(i in A):
        result+=1
    elif(i in B):
        result-=1
        
print(result)
