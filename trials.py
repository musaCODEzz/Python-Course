print(0o123)

numbers = list(range(2, 11, 2))
print(numbers)

squares = []

for value in range(1,11):
    squares.append(value**2)
print(squares)


digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

roots = [value ** 2 for value in range(1, 11)]
print(roots)
# List comprehension

# Exercise

for value in range(1,21):
    print(value)

one_million = []

for value in range(1, 10):
    one_million.append(value)
print(one_million)
print(min(one_million))
print(max(one_million))
print(sum(one_million))

odd = []
for value in range(1, 21, 2):
    odd.append(value)
print(odd)

threes = []

for value in range(3, 31, 3):
    threes.append(value)
print(threes)

cube = []

for value in range(1, 11):
    cube.append(value**3)
print(cube)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)