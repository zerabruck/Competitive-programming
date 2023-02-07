class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True )
        count = 0
        beg = 0
        
        while len(people) != 0:  
            end = 0
            for i in range(len(people) - 1 , 0,-1):
                if people[beg]+ people[i] == limit:
                    end = i
                    break
                elif people[beg] + people[i] > limit:
                    end = i + 1 
                    if end == len(people):
                        end = 0
                    break

                elif i == 1 and people[beg] + people[i] < limit :
                    end = i
                    break

            if end == beg:
                people.pop(beg)
                count += 1
            else:
                people.pop(beg)
                people.pop(end - 1)
                count += 1

        return count
