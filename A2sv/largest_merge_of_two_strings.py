class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        first = 0
        second = 0

        while first < len(word1) and second < len(word2):
            if word1[first : ] < word2[second : ] and word1[first] == word2[second]:
                merge += word2[second]
                second += 1
            elif word1[first] >= word2[second]:
                merge += word1[first]
                first += 1
            else:
                merge += word2[second]
                second += 1

        merge += word1[first : ]
        merge += word2[second : ]    
        return merge
