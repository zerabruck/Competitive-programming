# from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        dic={}

        for i in cpdomains:
            splitted_values=i.split()
            dot_index=[]
            for i in range(len(splitted_values[1])):
                if(splitted_values[1][i]=='.'):
                    dot_index.append(i)

            if(splitted_values[1] in dic):
                dic[splitted_values[1]]+=int(splitted_values[0])
            else:
                dic[splitted_values[1]]=int(splitted_values[0])

            for i in dot_index:
                sub_domain=splitted_values[1][i+1:]
                if(sub_domain in dic):

                    dic[sub_domain]+=int(splitted_values[0])
                else:
                    dic[sub_domain]=int(splitted_values[0])



        # print(dic)
        result=[]

        for i in dic:
            string=''
            string+=f'{dic[i]} '
            string+=i
            result.append(string)

        return result



    




            

            
