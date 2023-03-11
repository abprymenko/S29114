class Student:
    amount_students = 0
    def __init__(self, name, age, height):
        self.height = height
        self.age = age
        self.name = name
        Student.amount_students += 1
    def GetFullInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nHeight: {self.height}\nTotal amount of students: {Student.amount_students}"