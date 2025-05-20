cars = ['bmw', 'audi', 'mercedes', 'vw']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer try again")

banned_users = ['anne', 'ben', 'charlie']
user = 'anne'

if user not in banned_users:
    print(f"{user.title()}, you are allowed to post anytging since you are not banned")
else:
    print(f"{user.title()}, you are banned from posting")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')