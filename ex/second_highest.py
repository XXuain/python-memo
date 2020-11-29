# 印出成績第二高的，如果超過一個人都依依列出人名
students = [['Jerry', 90], ['Justin', 89], ['Tom', 99], ['Harsh', 90]]


def second_hights(students):
    grades = [g[1] for g in students]
    grades = sorted(grades, reverse=True)
    second = grades[1]
    print(second)

    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)


second_hights(students)
