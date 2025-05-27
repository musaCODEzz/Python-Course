class Person:
    def __init__(self, name, age):
        if not name or not age:
            raise ValueError("Name and Age must be provided")
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 

#first person input
name = input("Enter your name: ").strip().title()
age = input("Enter your age: ").strip()
person_1 = Person(name, age)
person_1.greet()

#second person input
name = input("Enter your name: ").strip().title()
age = input("Enter your age: ").strip()
person_2 = Person(name, age)
person_2.greet()