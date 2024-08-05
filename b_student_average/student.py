# student.py in -> b_student_average

"""
Title: Student Info
Author: Marco Ou
Date: March 13th 2024
"""
from course import Course

class Student:

    def __init__(self, NAME: str, GRADE: int):
        self.name = NAME
        self.grade = GRADE
        self.courses = []
        self.average = 0

    def updateCourse(self):
        for i in range(len(self.courses)):
            print(f"{i+1}, {self.courses[i].getName()}")
        selection = int(input("> ")) - 1
        new_mark = int(input("New mark:"))
        self.courses[selection].updateMark(new_mark)


    def addCourse(self, COURSE: Course):
        self.courses.append(COURSE)

    def calculateAverage(self):
        total = 0
        for course in self.courses:
            total += course.getMark()
        self.average = total/len(self.courses)

    def displayAverage(self):
        print(self.average)

