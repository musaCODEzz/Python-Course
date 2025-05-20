age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age1 = 40
if age1 < 4:
    print("Your admission cost is $0.")
elif age1 < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


age2 = 30
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
else:   
    price = 10
print(f"Your admission cost is ${price}.")




# Get input from the user
user_input = input("Enter your requested toppings separated by commas: ")

# Split the input into a list and clean up each topping (remove extra spaces, convert to lowercase)
requested_toppings = [topping.strip().lower() for topping in user_input.split(',')]

# Loop through the requested toppings
for topping in requested_toppings:
    if topping == 'mushrooms':
        print("Adding mushrooms.")
    elif topping == 'extra cheese':
        print("Adding extra cheese.")
    elif topping == 'pepperoni':
        print("Adding pepperoni.")
    else:
        print(f"Sorry, we don't have {topping}.")
print("\nFinished making your pizza!")