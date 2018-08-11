class Student:
    def __init__(self,name):
        print("This is a parametrized constructor")
        self.name = name
    def display(self):
        print("Hello "+self.name)
student = Student("Irfan")
student.display()
