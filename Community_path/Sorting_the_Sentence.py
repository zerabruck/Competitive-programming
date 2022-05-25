class Solution:
    def sortSentence(self, s: str) -> str:
        
        list_of_words=s.split()
        dicto={}
        answer=''

        for i in list_of_words:
            index=i[-1]

            word=i[:-1]

            dicto[int(index)]=f'{word} '

        for i in range(1,len(list_of_words)+1):
            answer+=dicto[i]
        return answer[:-1]
        