class Student:
    name = "Student1"
    age = 13
    grade = 8

    def __str__(self):
        return self.name

print(Student())

# __str__ function can be used to return a string inside the class