class Animal:
    def eat(self):
        print("Eating...")
class Dog(Animal):
    def bark(self):
        print("Barking...")
class Babydog(Dog):
    def play(self):
        print("Playing")
d = Babydog()
d.eat()
d.bark()
d.play()