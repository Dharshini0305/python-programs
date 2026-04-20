Task:
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
Program:
n, x = map(int, input().split())
subject_marks = []
for _ in range(x):
    subject_marks.append(list(map(float, input().split())))
for student_scores in zip(*subject_marks):
    average = sum(student_scores) / x
    print(f"{average:.1f}")