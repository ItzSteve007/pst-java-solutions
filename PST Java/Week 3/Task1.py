def topStudents(students):
    for s,m in students:
        result=students[m].sort(reverse=True)
        if students[m]==students[m+1]:
            result=students[s].sort(reverse=True)
    return result
n=int(input("No. of students:"))
for _ in range(n):
    student_details=map(int,input().split())
topStudents(student_details)