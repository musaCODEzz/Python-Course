class Dog:
    def __init__(self, name, breed, owner):
        if not name or not breed or not owner:
            raise ValueError("Name, breed and owner cannot be empty")
        self.name = name
        self.breed = breed
        self.owner = owner


name = input("Enter the dog's name: ").strip().title()
breed = input("Enter the dog's breed: ").strip().title()
#owner = input("Enter the owner's name: ").strip().title()

class Owner:
    def __init__(self, owner_name, address, contact_number):
        if not owner_name or not address or not contact_number:
            raise ValueError("Name, address and contact number cannot be empty")
        self.owner_name = owner_name
        self.address = address
        self.contact_number = contact_number


owner_name = input("Enter the owner's name: ").strip().title()
address = input("Enter the owner's address: ").strip().title()
contact_number = input("Enter the owner's contact number: ").strip().title()



owner_11 = Owner(owner_name, address, contact_number)
dog_11 = Dog(name, breed, owner_11)

#print(f"Dog's name: {dog_11.name }, and its a {dog_11.breed} dog.")
print(f"Dog's name: {dog_11.name}, and it's a {dog_11.breed} dog. Owner: {owner_11.owner_name}, Address: {owner_11.address}, Contact: {owner_11.contact_number}")
print(dog_11.owner.contact_number)