motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)


for motorcycle in motorcycles:
    print(motorcycle.upper())

books = []

books.append('The Hitchhiker\'s Guide to the Galaxy')
books.append('The Lord of the Rings')
books.append('The Catcher in the Rye')
print(books)

books[0] = "The Loggerhead's Guide to the Galaxy"
print(books)
books.insert(0, 'The Great Gatsby')
print(books)

# removing an element from the list
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)

#if you know the position of the element you want to remove

del cars[2]
print(cars)

# if you don't know the position of the element you want to remove
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
popped_bike = bikes.pop(1)
print(bikes)
print(f"The last bike I bought was a {popped_bike.title()}.")



