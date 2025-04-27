from School import School
from Department import Department
from Student import Student
from Course import Course
from Instructor import Instructor

school=School()
department=Department()
student=Student()
course=Course()
instructor=Instructor()

department.has(school)

student.attends(course)
student.member(school)

instructor.teaches(course)
instructor.assignedTo(department)
