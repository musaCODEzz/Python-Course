class Person:
    def __init__(self, name, age):
        if not name or not age:
            raise ValueError("Name and Age must be provided")
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 

name = input("Enter your name: ").strip().title()
age = input("Enter your age: ").strip()


person_1 = Person(name, age)
#print(f"Hello my name is {person_1.name} and I am {person_1.age} years old")
person_1.greet()