class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=''
        mininum=len(strs[0])

        # for i in strs:
        #     mininum=min(mininum,len(i))

        for i in range(mininum):
            temp=strs[0][i]

            for j in strs:
                if(j[i]!=temp):
                    return result

            result+=temp

        return result
                