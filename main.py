class Student:
    def __init__(self, last_name, first_name, course):
        self.last_name = last_name
        self.first_name = first_name
        self.course = course
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    def display_information(self):
        print("Student Information:")
        print("Last Name:", self.last_name)
        print("First Name:", self.first_name)
        print("Course:", self.course)
        print("Grades:", self.grades)
        print("Average Grade:", self.calculate_average_grade())


def create_student():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    course = input("Enter course: ")
    return Student(last_name, first_name, course)


def add_grade_to_student(student):
    grade = float(input("Enter grade: "))
    student.add_grade(grade)


def save_student_information(student):
    file_name = "student_information.txt"
    with open(file_name, "a") as file:
        file.write("Last Name: " + student.last_name + "\n")
        file.write("First Name: " + student.first_name + "\n")
        file.write("Course: " + student.course + "\n")
        file.write("Grades: " + ", ".join(map(str, student.grades)) + "\n")
        file.write("Average Grade: " + str(student.calculate_average_grade()) + "\n")
        file.write("\n")


def main():
    student = create_student()
    add_grade_to_student(student)
    student.display_information()
    save_student_information(student)


if __name__ == "__main__":
    main()
