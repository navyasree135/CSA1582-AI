student_subject(john, math, 101).
student_subject(john, physics, 102).
student_subject(alice, chemistry, 103).
student_subject(alice, biology, 104).
student_subject(michael, english, 105).
student_subject(michael, history, 106).
student_subject(susan, math, 101).
student_subject(susan, biology, 104).
student_subject(peter, physics, 102).
student_subject(peter, chemistry, 103).
teacher_subject(mr_smith, math, 101).
teacher_subject(mr_jones, physics, 102).
teacher_subject(mrs_brown, chemistry, 103).
teacher_subject(mr_doe, biology, 104).
teacher_subject(mrs_white, english, 105).
teacher_subject(mr_black, history, 106).
subjects_studied_by_student(Student, Subject, Code) :-
    student_subject(Student, Subject, Code).
subjects_taught_by_teacher(Teacher, Subject, Code) :-
    teacher_subject(Teacher, Subject, Code).
