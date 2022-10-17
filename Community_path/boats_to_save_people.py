class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        
        
        people.sort()
        
        first_val=0

        second_val=len(people)-1
        
        while(True):
            if(second_val<first_val):
                break
            elif(second_val==first_val):
                boats+=1
                break
            elif(people[first_val]+people[second_val]<=limit):
                first_val+=1
                second_val-=1
                boats+=1
            else:
                second_val-=1
                boats+=1
                
                
        return boats
                
                
                
        
            
            

        
        
                
        

        