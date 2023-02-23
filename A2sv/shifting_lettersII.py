class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_sum = [0] * len(s)
        # add pref element
        for start , end , val in shifts:
            if val == 0:
                val = -1
            pref_sum[start] += val
            if end < len(s) - 1:
                pref_sum[end + 1] += -1 * val
        # prefsum of element
        for i in range(1,len(pref_sum)):
            pref_sum[i] += pref_sum[ i - 1]

        # return string
        string = ""
        for char in range(len(s)):
            ele = ord(s[char]) + pref_sum[char] 
            ele = (ele - ord('a')) % 26 + ord('a')
            ele = chr(ele)
            string += ele

        return string
