# Day 15: Inheritance & Polymorphism

'''
1. Inheritance: Allows a class (child) to inherit attributes and methods from another class (parent).
2. Polymorphism: Let's have different classes implement the same method in different ways.
'''

# --- Inheritance Example ---
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Cat also inherits from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Dog says Woof!
cat.speak()  # Cat says Meow!

'''
So here, Dog and Cat inherited the Animal class but overrode the `speak()` method. 
This is polymorphism in action — the same method name behaves differently depending on the object.
'''

# --- Polymorphism using functions ---
def animal_sound(animal):
    animal.speak()

animal_sound(dog)  
animal_sound(cat)  

'''
Even though the function `animal_sound()` takes an `animal`, 
it works for any object that has a `speak()` method - this is also polymorphism.
'''

# --- One more example with Shape ---
class Shape:
    def area(self):
        print("Area not defined for generic shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]

for s in shapes:
    print(f"Area: {s.area()}") 
