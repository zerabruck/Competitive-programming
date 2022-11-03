class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        beg=-1
        minus_start=-1
        max_count=0
        arrr=[]
        
        i=0
                
        while(i<len(arr)):
            
            
            if(i==len(arr)-1 and minus_start==0):
               
                
                max_count=max(max_count,(i-beg)+1)
                arrr.append(max_count)
                break
            elif(i==len(arr)-1):
                break
            
            elif(arr[i]<arr[i+1] and beg==-1 ):
                beg=i
                
                
            elif(arr[i]==arr[i+1] and beg!=-1 and minus_start==-1):
                beg=-1
            
                
            elif(arr[i]>arr[i+1] and beg!=-1 and minus_start==-1): 
                minus_start=0
    
            elif(arr[i]==arr[i+1] and minus_start==0):
                
                
                max_count=max(max_count,(i-beg)+1)
                beg=-1
                minus_start=-1
 
                
            elif(arr[i]<arr[i+1] and minus_start==0):
                
                max_count=max(max_count,(i-beg)+1)
               
                beg=-1
                minus_start=-1
               
                
                continue 
                
            
                
                
            i+=1
       
        return max_count
            
            

                

                
                
                
                
        
                