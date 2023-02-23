class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        end = 0
        max_len = 0
        temp = 0
        ele_dict = {}
        for start in range(len(s)):
            if s[end] != s[start]:
                temp += 1

            if s[end] != s[start] and temp > k :
                while temp > k and end <= start:
                    max_len = max(start - end , max_len )
                    end += 1
            else:
                if s[start] not in ele_dict:
                    ele_dict[s[start]] = 1

                else:
                    ele_dict[s[start]] += 1
        max_len = max(start - end , max_len)
        return max_len
