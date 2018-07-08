class Person:
    #constructor
    def __init__(self,personName,personAge):
        self.name = personName
        self.age = personAge
    #class methods
    def shownName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student:
    #constructor
    def __init__(self,id):
        self.studentId = id
    #method
    def getId(self):
        return self.studentId
class Resident(Person, Student): #extends both person and student class
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)

#create an object of the subclass
resident1 = Resident('John',30,'102')
resident1.shownName()
print(resident1.getId())