# https://www.hackerrank.com/challenges/nested-list/problem



def sagird(n):
    studentsAndGrades = []
    grades = []
    for i in range(0,n):
        if 2 <= n <= 5:
            studentAndGrade = []
            sagird = input('ad:')
            bal = float(input(f'{sagird} bali:'))
            studentAndGrade.append(sagird)
            studentAndGrade.append(bal)
            grades.append(bal)
            studentsAndGrades.append(studentAndGrade)
    grades.sort()
    print(grades)
    for i in range(0, n):
        if grades[0] != grades[1] and grades[1] == studentsAndGrades[i][1]:
            print(studentsAndGrades[i][0])
sagird(int(input()))



