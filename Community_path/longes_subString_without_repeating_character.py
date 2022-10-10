class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_arr=[]
        max_len=0
        beg=0
        end=0

        while(True):
            if(end==len(s)):
                max_len=max(max_len,end-beg)
                break
            elif(s[end]not in char_arr):
                char_arr.append(s[end])
                end+=1
            elif(s[end] in char_arr):
                char_arr.remove(s[beg])
                max_len=max(max_len,end-beg)
                beg+=1
                
        return max_len


        