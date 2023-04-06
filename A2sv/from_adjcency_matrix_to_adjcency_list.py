from collections import defaultdict
nodes = int(input())

adj_matrix = [] 

#  data intake

for i in range(nodes):
    eles = list(input().split())
    adj_matrix.append(eles)

adj_list = defaultdict(list)

for row_indx , row_val in enumerate(adj_matrix):
    for col_indx , col_val in enumerate(row_val):
        if col_val != '0':
            adj_list[row_indx + 1] .append(str(col_indx + 1))

for ele in adj_list.values():
    ele_string = ' '.join(ele)
    print(f'{len(ele)} {ele_string}')
