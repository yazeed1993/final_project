"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Yazeed osama elderawy
Delivery Date :
"""
import uuid

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0
    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)
    # method to get_student_details as dict

    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Mark: {course.course_mark}")

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        if len(self.courses_list) == 0:
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)


# in Global Scope
# TODO 8 declare empty students list

students = []

while True:

    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))

        if selection == 1:

            # TODO 10 make sure that Student number is not exists before
            while True:
                student_number = input("Enter Student Number: ")

                # Check if the student_number already exists
                if any(student.student_number == student_number for student in students):
                    print("Student Number already exists. Please enter a unique Student Number.")
                else:
                    student_name = input("Enter Student Name: ")
                    while True:
                        try:
                            student_age = int(input("Enter Student Age"))
                            break
                        except:
                            print("Invalid Value")

                    # TODO 11 create student object and append it to students list


                    new_student = Student(student_name, student_age, student_number)
                    students.append(new_student)
                    print("Student Added Successfully")
                    break


        elif selection == 2:
            student_number = input("Enter Student Number")
            # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

            target_student = None
            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                students.remove(target_student)
                print("Student Deleted Successfully")
            else:
                print("Student Not Found")

        elif selection == 3:
            student_number = input("Enter Student Number")
            # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

            target_student = None
            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                student_details = target_student.get_student_details()
                print("Student Details:")
                for key, value in student_details.items():
                    print(f"{key}: {value}")
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number")
            # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

            target_student = None
            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                student_average = target_student.get_student_average()
                print(f"Student Average Mark: {student_average}")
            else:
                print("Student Not Found")

        elif selection == 5:
            student_number = input("Enter Student Number")
            # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

            target_student = None
            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                course_name = input("Enter Course Name: ")
                try:
                    course_mark = float(input("Enter Course Mark: "))
                    target_student.enroll_course(course_name, course_mark)
                    print("Course Added to Student")
                except ValueError:
                    print("Invalid Value. Please enter a valid number for the course mark.")

            else:
                print("Student Not Found")

        elif selection == 6:
            # TODO 16 call a function to exit the program
            break

        else:
            print("Invalid selection. Please choose a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
