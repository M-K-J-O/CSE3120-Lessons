# main.py in -> b_student_average

"""
Title: student info display
Author: Marco
Date: March 13th 2024
"""

from student import Student
from course import Course

class Main:

    def __init__(self):
        self.student = Student

    def setup(self):
        print(" --- * Student Info Organizer * ---")
        name = input("Name:")
        self.student = Student(name, 12)

    def run(self):
        while True:
            choice = self.menu()
            if choice == 1:
                course_name = input("Course Name:")
                self.student.addCourse(Course(course_name))
            elif choice == 2:
                self.student.updateCourse()
            elif choice == 3:
                self.student.calculateAverage()
                self.student.displayAverage()
            else:
                quit()

    def menu(self):
        pass



if __name__ == "__main__":
    MAIN = Main()
    MAIN.setup()
    MAIN.run()