class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        listing=[]
        zeros=[]
        result=0
        count=0
        beg=0
        
    
        
        for i in nums:
            if(i%2==0):
                listing.append(1)
            else:
                listing.append(0)
                
        
                
                
                
        for i in range(len(listing)):
            if(listing[i]==0):
                count+=1
                zeros.append(i)
                
            if(count>k):
                first=zeros[0]-beg
                second=i-1-zeros[k-1]
                result+=(first+second)+1
                result+=first*second
                beg=zeros.pop(0)+1
                count-=1
                
        
                
        if(count==k):
            first=zeros[0]-beg
            second=len(listing)-1-zeros[k-1]
            
            result+=first*second
            result+=(first+second)+1
            
        return result
            
                
        
                    
        
       