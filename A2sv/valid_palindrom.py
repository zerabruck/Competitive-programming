class Solution:
    def isPalindrome(self, s: str) -> bool:

        small_letter=s.lower()
        clarified_string=''

        for i in small_letter:
            if(i.isalnum() ):
                clarified_string+=i

        beg=0
        end=len(clarified_string)-1
        if(len(clarified_string)==1):
            return True

        while(beg<end):
            if(clarified_string[beg]==clarified_string[end]):
                beg+=1
                end-=1

            else:
                return False 

        return True

        
# alternative
        # if(clarified_string[::-1]==clarified_string):
        #     return True
        # else:
        #     return False