class Animal:
    def speak(self):
        return "Sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Animal(),Dog(), Cat()]
for a in animals:
    print(a.speak())   #כל אחד עושה פעולה אחרת 
