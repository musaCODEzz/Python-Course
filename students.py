class Student:
    ...

def main():
    student = get_student()
    
    print(f"Hello my name is {student.name} and I am from {student.house} house")



def get_student():
    # name = input("Enter your name: ")
    # house = input("Enter your house: ")
    # return [name, house]
    # name = input("Enter your name: ")
    # house = input("Enter your house: ")
    # return {"name": name, "house": house}
    student = Student()
    student.name = input("Enter your name: ")
    student.house = input("Enter your house: ")
    return student

if __name__ == "__main__":
    main()