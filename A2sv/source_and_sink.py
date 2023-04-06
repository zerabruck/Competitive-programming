def is_zeros(eles):
    set_ele = set(eles)
    if '0' in set_ele and len(set_ele) == 1:
        return True
    return False

nodes = int(input())

adj_matrix = [] 

#  data intake

for i in range(nodes):
    eles = list(input().split())
    adj_matrix.append(eles)

sources = []
sinks = []

# sinks thorugh rows
for indx , row in enumerate(adj_matrix):
    if is_zeros(row):
        sinks.append(str(indx + 1))

# sources thorugh col
for col in range(nodes):
    col_val = []
    for row in adj_matrix:
        col_val.append(row[col])
    if is_zeros(col_val):
        sources.append(str(col + 1))
sources_string = " ".join(sources)
print(f'{len(sources)} {sources_string}')
sinks_string = " ".join(sinks)
print(f'{len(sinks)} {sinks_string}')
