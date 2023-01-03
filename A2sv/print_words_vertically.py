class Solution:
    def printVertically(self, s: str) -> List[str]:
        """
        the question here is saying that to concatenate every word in a string 
        that is in the same column and return it in a array

        so i am going to first split the strings then i will go through the len of the splited 
        string to find the maximum length
        then i will go through the column to concatenate it with the character of the same column
         and if the char dosen't exist i will append a space on it behalf
        """

        array_words = s.split()
        max_word = max(array_words,key= lambda x:len(x))
        max_len = len(max_word)
        result = []

        for i in range(max_len):
            string = ""

            for row in array_words:
                if i >= len(row):
                    string += " "
                else:
                    string += row[i]

            string = string.rstrip()
            result.append(string)

        return result