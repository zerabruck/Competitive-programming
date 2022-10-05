class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        
        def is_vowel(letter):
            vowel=['a','e','i','o','u']
            if(letter in vowel):
                return True
            else:
                return False

        arr= s
        
        count=0

        for i in arr[:k]:
            if(is_vowel(i)):
                count+=1

        firstsum=count


        for i in range(k,len(arr)):
            if(is_vowel(arr[i-k])):
                sub_arr=firstsum-1
            else:
                sub_arr=firstsum

            if(is_vowel(arr[i])):
                add_arr=sub_arr+1
            else:
                add_arr=sub_arr

            firstsum=add_arr
            if(firstsum>=count):
                count=firstsum
                
        return count

