from turtle import *

# t1 = Turtle()
# t1.color("red")
# t1.width(5)

# t1.begin_fill()

# for i in range(5):
#     t1.forward(150)
#     t1.right(144)
# t1.end_fill()

# done()

colors = ["red", "blue", "green", "yellow", "black"]
t = Turtle()

for i in range(5):
    t.pencolor(colors[i])
    t.forward(100)
    t.left(72)

done()