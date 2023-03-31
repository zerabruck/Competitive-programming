class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ele_dict = {}
        for indx , val in enumerate(words):
            bit_map = 0
            for char in val:
                bit_map |= 1 << (ord(char) - ord('a'))
            ele_dict[indx] = bit_map
            
        max_word = 0
        for indx  in range(len(words)):

            for inner in range(indx + 1 , len(words)):

                if ele_dict[indx] & ele_dict[inner] == 0:
                    product = len(words[indx]) * len(words[inner])
                    max_word = max(max_word , product)

        return max_word
