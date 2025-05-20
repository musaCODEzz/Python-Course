class Student:
    def __init__(self, name, house):
        if not name or not house:
            raise ValueError("Name and house cannot be empty")
        if not house in ['Mandela', 'Kibaki', 'Kenyatta', 'Moi']:
            raise ValueError("House must be one of the following: Mandela, Kibaki, Kenyatta, Moi")
        self.name = name
        self.house = house



# student = Student("Harry", "Gryffindor")
# print(f"Hello my name is {student.name} and I am from {student.house} house")

name = input("Enter your name: ").strip().title()
house = input("Enter your house: ").strip().title()

student = Student(name, house)
print(f"Hello my name is {student.name} and I am from {student.house} house")