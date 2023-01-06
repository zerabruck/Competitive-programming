from collections import Counter

input()
student_list = list(input().split())
black_list = set(input().split())
excellent_students = 0

for student in student_list:
    if student not in black_list:
        char_count = Counter(student)
        char_quantity = set()

        for i in char_count.values():
            char_quantity.add(i)

        if len(char_quantity) == 1 :
            excellent_students += 1

print(excellent_students)



