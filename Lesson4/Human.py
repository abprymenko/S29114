class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __showInfoHuman__(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Height: {self.height}")