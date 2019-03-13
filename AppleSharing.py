def apples(students,apples):
    if apples < students:
        eachStudentGets = students // apples
        print("Each student gets", eachStudentGets, "apples")
        Remaining = students % apples
        print("Apples remaining in the basket are ", Remaining)
    elif apples == students:
        # print("Each student gets exactly 1 apple")
        eachStudentGets = 1
        Remaining = apples - students
        print("Each student gets exactly ",eachStudentGets, "apples")
        print("Apples remaining in the basket are ", Remaining)
    else:
        if apples % students == 0:
            eachStudentGets = apples // students
            Remaining = 0
            print("Each student gets ",eachStudentGets, "apples")
            print("Apples remaining in the basket are ", Remaining)

        else:
            eachStudentGets = apples//students
            Remaining = apples % students
            print("Each student gets ", eachStudentGets, "apples")
            print("Apples remaining in the basket are ", Remaining)


if __name__=='__main__':
    numberOfStudents = int(input("Enter the number of students "))
    numberOfApples = int(input("Enter the number of apples "))
    apples(numberOfStudents,numberOfApples)


