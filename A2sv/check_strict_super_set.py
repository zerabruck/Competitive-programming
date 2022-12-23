# Enter your code here. Read input from STDIN. Print output to STDOUT
truth_value='True'
def super_set_checker(bigger_set,smaller_set):
    for i in smaller_set:
        if(i not in bigger_set):
            return 'False'
        
    for i in bigger_set:
        if(i not in smaller_set):
            return 'True'
        
    return 'False'

    
    
setA=list(map(int,input().split()))
loop=int(input())

for i in range(loop):
    setB=list(map(int,input().split()))
    
    truth_value=super_set_checker(setA,setB)
    if(truth_value=='False'):
        break
print(truth_value)