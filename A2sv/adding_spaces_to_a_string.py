class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_string = ''
        space = set(spaces)

        for i in range(len(s)):
            if i in space:
                new_string += ' '

            new_string += s[i]

        return new_string