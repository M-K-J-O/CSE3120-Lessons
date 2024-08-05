# course.py in -> b_student_averge

"""
Title: Student Marks
Author: Marco Ou
Date: March 13th 2024
"""

from student import Student

class Course:

    def __init__(self):

        self.name = NAME
        self.courses = []
        self.mark = 0

    def getName(self):
        return self.name

    def getMark(self) -> int:
        return self.mark

    def updateMark(self, NEW_MARK):
        self.mark = NEW_MARK