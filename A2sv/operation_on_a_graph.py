from collections import defaultdict

ele_dict = defaultdict(list)
input()

def AddEdge(a , b):
    ele_dict[a].append(b)
    ele_dict[b].append(a)

def Vertex( a ):
    return ' '.join(ele_dict[a])

loop = int(input())
for i in range(loop):
    ele = list(input().split())
    if ele[0]  == '1':
        AddEdge(ele[1] , ele[2])
    else:
        print(Vertex(ele[1]))
