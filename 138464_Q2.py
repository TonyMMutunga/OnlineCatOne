class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no grades recorded.")
        else:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_students_and_grades(self):
        if not self.students:
            print("No students enrolled in this course.")
        else:
            print(f"Students and grades for the course '{self.course_name}':")
            for student in self.students:
                print(f"\n{student.name} (ID: {student.student_id}):")
                student.display_grades()


# Interactive code to allow an instructor to add students and assign grades
def main():
    # Create an instructor for a course
    instructor = Instructor("Dr. Mutunga", "Introduction to Python")

    # Interact with the course management system
    while True:
        print("\nCourse Management System Menu:")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new student
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            # Assign a grade to a student
            student_id = input("Enter the student ID: ")
            assignment_name = input("Enter the assignment name: ")
            try:
                grade = float(input("Enter the grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid input for grade. Please enter a numeric value.")

        elif choice == "3":
            # Display all students and their grades
            instructor.display_students_and_grades()

        elif choice == "4":
            print("Exiting the Course Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive course management system
main()
