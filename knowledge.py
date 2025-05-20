# user_input  = input("Enter your requested toppings separated by commas: ")

# requested_toppings = [topping.strip().lower() for topping in user_input.split(',')]


# if requested_toppings:

#     for topping in requested_toppings:
#         if topping == 'mushrooms':
#             print("Adding mushrooms.")
#         elif topping == 'extra cheese':
#             print("Adding extra cheese.")
#         elif topping == 'pepperoni':
#             print("Adding pepperoni.")
#         # else:
#         #     print(f"Sorry, we don't have {topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# user_input = input("Enter a topping: ")

# requested_toppings = [user_input.strip().lower()] if user_input.strip() else []

# if requested_toppings:
#     for topping in requested_toppings:
#         if topping == 'mushrooms':
#             print("Adding mushrooms.")
#         elif topping == 'extra cheese':
#             print("Adding extra cheese.")
#         elif topping == 'pepperoni':
#             print("Adding pepperoni.")
#         else:
#             print(f"Sorry, we don't have {topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

user_input = input("Enter toppings (comma-separated): ")

requested_toppings = [topping.strip().lower() for topping in user_input.split(',') if topping.strip()]

if requested_toppings:
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
else:
    print("Are you sure you want a plain pizza?")