class Solution:
    def compress(self, chars: List[str]) -> int:
        runner = 1
        holder = 0
        counter = 1
        while runner < len(chars):
            if chars[holder] == chars[runner]:
                counter += 1
                chars.pop(runner)

            elif counter != 1 :
                string = str(counter)
                for i in string:
                    chars.insert(runner,i)
                    runner += 1

                holder = runner
                runner += 1
                counter = 1

            else:
                runner += 1
                holder += 1

        if counter != 1 :
            string = str(counter)
            for i in string:
                chars.append(i)
                runner += 1


        return len(chars)        
