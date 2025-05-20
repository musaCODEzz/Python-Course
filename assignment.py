guests_list = ['Musa', "Maxwel", "Ochanda"]

for guest in guests_list:
    print(f"Hello {guest}, you are invited to my dinner party")


print(f"{guests_list[0]} can't make it to the dinner party")

guests_list[0] = "Abdi"

print(guests_list)

for guest in guests_list:
    print(f"Hello {guest}, you are invited to my dinner party")

print(f"Hello {guests_list}, I found a bigger dinner table, so I am inviting more guests.")

for guest in guests_list:
    print(f"Hello {guest}, I found a bigger dinner table, so I am inviting more guests. ")

guests_list.insert(0, "Mose")
guests_list.insert(2, "Gidi")
guests_list.append("Lawi")

for guest in guests_list:
    print(f"Hello {guest}, you are invited to my dinner party.")

for guest in guests_list:
    print(f"Hello {guest}, I can only invite two friends to my dinner party.")

popped_guest1 = guests_list.pop()
print(f"Sorry {popped_guest1}, I can't invite you to the dinner party.")

popped_guest2 = guests_list.pop(0)
print(f"Sorry {popped_guest2}, I can't invite you to the dinner party.")

popped_guest3 = guests_list.pop(1)
print(f"Sorry {popped_guest3}, I can't invite you to the dinner party.")

popped_guest4 = guests_list.pop(2)
print(f"Sorry {popped_guest4}, I can't invite you to the dinner party.")

print(guests_list)

for guest in guests_list:
    print(f"Hello {guest}, you are still invited to the dinner party.")

del guests_list[0]
del guests_list[0]

print(guests_list)

print(f"The number of guests invited to the dinner party is  {len(guests_list)}")
