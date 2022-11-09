class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        length=len(intervals)
        beg=0
        
        while(length-1!=beg):
            
            if(intervals[beg+1][0]<=intervals[beg][0] and intervals[beg][0]<=intervals[beg+1][1] or intervals[beg+1][0]<=intervals[beg][1] and intervals[beg][1]<=intervals[beg+1][1] ):
                mini=min(intervals[beg][0],intervals[beg][1],intervals[beg+1]
                         [0],intervals[beg+1][1])
                
                
                maxi=max(intervals[beg][0],intervals[beg][1],intervals[beg+1][0],intervals[beg+1][1])
                intervals.pop(beg)
                intervals.pop(beg)
                intervals.insert(beg,[mini,maxi])
                length-=1
                
                continue
                
            elif(intervals[beg][0]<=intervals[beg+1][0] and intervals[beg+1][0]<=intervals[beg][1] or intervals[beg][0]<=intervals[beg+1][1] and intervals[beg+1][1]<=intervals[beg][1] ):
                mini=min(intervals[beg][0],intervals[beg][1],intervals[beg+1]
                         [0],intervals[beg+1][1])
                
                
                maxi=max(intervals[beg][0],intervals[beg][1],intervals[beg+1][0],intervals[beg+1][1])
                intervals.pop(beg)
                intervals.pop(beg)
                intervals.insert(beg,[mini,maxi])
                length-=1
                
                continue
                
            
                
            else:
                beg+=1
                
                
        return intervals
            

        

