class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        dicto={}
        checking_arr=[]
        result=[]
        def checker(val):
            dicto[val[-1]]-=1        
            for i in val:

                if(dicto[i]!=0):


                    return False
            return True

        for i in s:
            if(i not in dicto):
                dicto[i]=1

            else:
                dicto[i]+=1


        first_point=0
        second_point=0

        for i in s:


            checking_arr.append(i)
            if(checker(checking_arr)):


                result.append(len(checking_arr))
                checking_arr.clear() 
                
                
        return result
          
