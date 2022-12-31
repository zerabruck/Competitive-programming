from collections import Counter
loop = int(input())

for i in range(loop):
    cost = 0
    planet_number = list(map(int,input().split()))
    c = planet_number[1]

    planets = list(map(int,input().split()))
    planet_orbit = Counter(planets)

    for i in planet_orbit.values():
        cost += min(c,i)


    print(cost)