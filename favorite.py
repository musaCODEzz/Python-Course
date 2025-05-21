# favorite_lang = {}

# name = input("Enter your name: ").strip().title()
# language = input("Enter your favorite programming language: ").strip().title()

# # Store the name and language in the dictionary
# favorite_lang[name] = language

# if favorite_lang:
#     for name, language in favorite_lang.items():
#         print(f"{name.title()}: {language}")
# else:
#     print("No favorite languages have been recorded yet.")

favorite_lang ={
    "musa": "python",
    "jane": "java",
    "john": "c++",
    "james": "javascript",
    "yveee": "python"
}

# language = favorite_lang["james"].title()
# print(f"James's favorite language is {language}.")

# alien_0 = {'color': 'green', 'speed': 'slow'}
# #print(alien_0["points"])
# point_value = alien_0.get('color', 'No point value assigned')
# print(point_value)

# user_0 = {
#     'username': 'Musa',
#     'first':'Ochanda',
#     'last':'Maxwel'
# }

# print(user_0)

# for key, value in user_0.items():
#     print(f'{key}:{value}')

# for name, language in favorite_lang.items():
#     print(f"{name.title()} favorite's language is {language.title()}")

friends = ['jane', 'john']
for name in favorite_lang.keys():
    print(f"Hi {name}")
    if name in friends:
        language = favorite_lang[name]
        print(f"\t{name}, I see you love {language}!")


# for language in favorite_lang.values():
#     print(f"These are the favorite languages {language.title()}\n")

for name in sorted(favorite_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for language in set(favorite_lang.values()):
    print(f"{language.title()}")