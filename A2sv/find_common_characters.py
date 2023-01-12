
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        duplicates = list(words[0])

        for word in words[1:]:
            new_dup = []
            for char in word:
                
                if char in duplicates:
                    index = duplicates.index(char)
                    value = duplicates.pop(index)
                    new_dup.append(value)

            duplicates = new_dup

        return duplicates


        

    