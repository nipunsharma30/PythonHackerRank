if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        inputarray = input().split()
        marks = list(map(float, inputarray[1:]))
        student_marks[inputarray[0]] = sum(marks)/len(marks)

    query_name = input()
    print("%.2f" % student_marks[query_name])