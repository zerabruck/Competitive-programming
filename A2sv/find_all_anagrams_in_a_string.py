class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        dict_p = {}
        dict_ele = {}
        if len(p) > len(s):
            return []

        for ele in p :
            if ele not in dict_p:
                dict_p[ele] = 1

            else:
                dict_p[ele] += 1


        # first window

        for char in s[:len(p)]:
            if char not in dict_ele:
                dict_ele[char] = 1

            else:
                dict_ele[char] += 1

        if dict_ele == dict_p:
            result.append(0)

        # sliding window

        for char in range(len(p),len(s)):
            remove = char - len(p)
            dict_ele[s[remove]] -= 1
            if dict_ele[s[remove]] == 0:
                del dict_ele[s[remove]]

            if s[char] not in dict_ele:
                dict_ele[s[char]] = 1

            else:
                dict_ele[s[char]] += 1

            if dict_ele == dict_p:
                result.append((char - len(p)) + 1)

        return result
        
