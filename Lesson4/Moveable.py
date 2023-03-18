class Moveable:
    def __init__(self, speed):
        self.speed = speed
    def Move(self):
        print(f"Run {self.speed}!")