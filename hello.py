print("Musa")
message = "This is my first message"
#print(message)

message = "This is my second message"
print(message)

name = "Musa Maxwel"
print(name.lower())

first_name = "Musa"
last_name = "Maxwel"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello my name is {first_name} {last_name}")

lowercase_name = full_name.lower()
stripped_name = lowercase_name.strip()
print(stripped_name)
print(f"Hello my name is {stripped_name}")



my_name = "Musa"
message = f"Hello {my_name}, would you like to learn some python Today?"
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for bike in bicycles:
    print(bike.title())
print(bicycles[2].upper())

my_message  = f"My first bicycle was a {bicycles[2].title()}"
print(my_message)
def add_num(a, b):
    return int(a) + int(b)
print(add_num("2", 3))