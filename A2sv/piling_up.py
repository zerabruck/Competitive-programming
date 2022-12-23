# Enter your code here. Read input from STDIN. Print output to STDOUT

loop=int(input())

for i in range(loop):
    answer='Yes'
    input()
    
    
    array=list(map(int,input().split()))
    last_element=max(array[0],array[-1])  # I think this is the bug
    # example test case -> 1, 23, 433, 1000
    # now you picked 1 as your last element but it should have been 1000
    beg=0
    end=len(array)-1
    
    
    while(beg<=end):
        if(array[beg]>=array[end]):
            if(array[beg]>last_element):
                answer='No'
                break
            else:
                last_element=array[beg]
                beg+=1       
                
        else:
            if(array[end]>last_element):
                answer='No'
                break
            else:
                last_element=array[end]
                end-=1
                
    print(answer)
        
        
            
            
        
    
    
                
            
