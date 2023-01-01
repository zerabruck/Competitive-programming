input()

best = 0
worst = 0
count = 0
scores = list(map(int, input().split()))
best=scores[0]
worst=scores[0]
for i in scores[1:]:
    if(i > best):
        count+=1
        best=i
    elif(i < worst):
        count+=1
        worst=i

print(count)

