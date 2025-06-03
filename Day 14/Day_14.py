# Day 14: Classes & Objects

'''
Classes define the structure and behavior (data + functions), and objects are instances of those classes.
'''

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.brand} {self.model}'s engine started.")
        else:
            print("Engine is already running.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print(f"{self.brand} {self.model}'s engine stopped.")
        else:
            print("Engine is already off.")

    def info(self):
        print(f"{self.brand} {self.model} ({self.year})")

# Creating objects
my_car = Car("Tesla", "Model 3", 2022)
my_car.info()
my_car.start_engine()
my_car.start_engine() 
my_car.stop_engine()
my_car.stop_engine()  

# Another Example:
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Python Crash Course", "Eric Matthes", 544)

book1.summary()
book2.summary()
