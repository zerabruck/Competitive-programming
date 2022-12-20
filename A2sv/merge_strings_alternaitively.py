class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        loop=min(len(word1),len(word2))
        result=''

        for i in range(loop):
            result+=word1[i]
            result+=word2[i]

        if(len(word1)==loop):
            result+=word2[loop:]

        else:
            result+=word1[loop:]

        return result

