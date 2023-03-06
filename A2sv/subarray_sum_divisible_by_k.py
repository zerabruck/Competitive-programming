class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # pref sum
        pref = [0]
        for i in nums:
            pref.append( pref[-1] + i)

        rem_dict = { }
        count = 0
        #  check the reminder if its in the dict and count it then add it to dict

        for num in pref :
            reminder = num % k           
            if reminder in rem_dict :
                count  += rem_dict[reminder]
                rem_dict[reminder] += 1
            else:
                rem_dict[reminder] = 1

        return count
