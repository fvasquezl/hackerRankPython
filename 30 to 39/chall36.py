from collections import namedtuple


if __name__ == "__main__":
    n = int(input())
    marks = 0
    columns = list(map(str, input().split()))
    Student = namedtuple("Student", columns)

    for i in range(1, n + 1):
        values = map(str, input().split())
        student = Student._make(values)
        marks += int(student.MARKS)

    print(marks / n)

"""
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

78.0
"""
