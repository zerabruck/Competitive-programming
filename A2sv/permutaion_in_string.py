class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str_dict = {}
        s1_dict = {}
        if len(s1) > len(s2):
            return False

        # add s1 to dict
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1 

        # crate first window

        for char in s2[:len(s1)]:
            if char not in str_dict:
                str_dict[char] = 1
            else:
                str_dict[char] += 1

        if str_dict == s1_dict:
            return True

        # create static sliding window

        for char in range(len(s1), len(s2)):
            ele = char - len(s1)
            str_dict[s2[ele]] -= 1
            if str_dict[s2[ele]] == 0 :
                del str_dict[s2[ele]]

            if s2[char] not in str_dict:
                str_dict[s2[char]] = 1
            else:
                str_dict[s2[char]] += 1

            if str_dict == s1_dict:
                return True

        return False
