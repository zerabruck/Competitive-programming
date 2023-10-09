class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lcp = [0] * len(needle)
        back, front = 0, 1
        while front < len(needle):
            if needle[front] == needle[back]:
                lcp[front] = back + 1
                front += 1
                back += 1
            elif back == 0:
                front += 1
            else:
                back = lcp[back - 1]

        match_hay, match_needle = 0, 0
        while match_hay < len(haystack):
            if haystack[match_hay] == needle[match_needle]:
                match_hay += 1
                match_needle += 1

            elif match_needle == 0:
                match_hay += 1
            else:
                match_needle = lcp[match_needle - 1]

            if match_needle >= len(needle):
                return match_hay - len(needle)
        return -1     
