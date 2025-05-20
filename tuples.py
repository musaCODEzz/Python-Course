
words = ("hello", "world", "python")
print(words[0])
print(words[1])
print(words[2])


dimensions = [(200, 50)]  # List with one tuple
for dimension in dimensions:
    print(dimension[1] * dimension[0], "\n")


buffet_foods = ("pizza", "chicken", "rice", "samosa", "chips")

for food in buffet_foods:
    print(food.title())

#buffet_foods[0] = "pasta"  # This will raise a TypeError because tuples are immutable
print("\nThe buffet has been updated with new foods.\n")
buffet_foods =("pasta", "juice", "rice", "samosa", "chips")

for food in buffet_foods:
    print(food.title())