class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        
# Main program
students = collect_students()
print_sorted_students(students)