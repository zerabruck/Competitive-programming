from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        dic=defaultdict(list)

        for i in paths:
            route_split=i.split()
# don't forget to hadle when m==0

            if(route_split[0].find('.')!=-1):
                for j in range(len(route_split)):

                    string=''
                    cutting_range=[]
                    flag=True
                    folder=route_split[j]
                    for k in range(len(folder)):
                        if(folder[k]=='('):
                            cutting_range.append(k)
                            flag=False

                        elif(folder[k]==')'):
                            cutting_range.append(k)


                        if flag:
                            string+=folder[k]

                    cuttend_key=folder[cutting_range[0]+1:cutting_range[1]]

                    dic[cuttend_key].append(string)

            else:
                for j in range(1,len(route_split)):
                    string=''
                    cutting_range=[]
                    flag=True
                    folder=route_split[j]
                    for k in range(len(folder)):
                        if(folder[k]=='('):
                            cutting_range.append(k)
                            flag=False

                        elif(folder[k]==')'):
                            cutting_range.append(k)


                        if flag:
                            string+=folder[k]

                    cuttend_key=folder[cutting_range[0]+1:cutting_range[1]]

                    dic[cuttend_key].append(route_split[0] + '/' +string)


            
        result=[]
        for i in dic:
            if len(dic[i])>=2:
                result.append(dic[i])
            

        return result



