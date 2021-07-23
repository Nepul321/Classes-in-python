class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Creating a student
student1 = Student("Student1", 13, 8)

# To delete objects you can use the del keyword
del student1.age

print(student1.age)
# Running this program will give you an error because we deleted student.age