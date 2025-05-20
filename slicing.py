players = ['musa', 'maxwel', 'ochanda', 'moses', 'otieno']

print(players[0:3])
print(players[-3:])
print('These are the last three players in my team')
for player in players[-3:]:
    print(player.title())


my_food = ['pizza', 'cookies', 'chips', 'bread']

print(len(my_food))

friend_food = my_food[-3:]
my_food.append('cannoli')
friend_food.append('ice cream')
print("My favorite food are:")
for food in my_food:
    print(food.title())

print("\nMy friend's favorite food are:")

for food in friend_food:
    print(food.title())
print("\n",len(my_food))
