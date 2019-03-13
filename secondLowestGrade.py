
if __name__ == '__main__':
    N= int(input())
    students = []
    for i in range(N):
        grade = [input(), float(input())]
        students.append(grade)
    students = sorted(students, key=lambda x: x[1])
    second_highest = students[0][1]
    for name, score in students:
        if score > second_highest:
            second_highest = score
            break
    print('\n'.join([name for name, score in sorted(students) if score == second_highest]))



