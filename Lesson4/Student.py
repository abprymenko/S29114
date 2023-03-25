import Lesson4.Human as h
import Lesson4.Moveable as m
class Student(h.Human, m.Moveable):
    def __init__(self, name, age, height, speed, mark = 12, subject = "OOP Python"):
        h.Human.__init__(self, name, age, height)
        m.Moveable.__init__(self, speed)
        self.mark = mark
        self.subject = subject

    def showInfo(self):
        h.Human.__showInfoHuman__(self)
        print(f"Subject: {self.subject}\n"
              f"Mark: {self.mark}\n"
              f"Speed: {self.speed}")