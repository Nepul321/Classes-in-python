class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Creating a student
student1 = Student("Student1", 13, 8)

# Modifying object properties
student1.age = 14

print(student1.age)