class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        
        
        
        pre_sum=[chalk[0]]
        value=0
        for i in range(1,len(chalk)):

            pre_sum.append(chalk[i]+pre_sum[i-1])
        big_val=pre_sum[-1]
        div=k//big_val
    
        if(big_val>k):
            for i in range(len(pre_sum)):
                if(pre_sum[i]>k):
                    
                    return i
                
        else:
            
            
            end_val=pre_sum[-1]*div
           

            result=[end_val+chalk[0]]


            if(result[0]>k):
                value=0
                return value



            for i in range(1,len(chalk)):

                integerr=chalk[i]+result[i-1]
                result.append(integerr)

                if(integerr>k):
                    value=i

                    return value
            