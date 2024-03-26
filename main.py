import turtle
#Drawing Star
drawing_board=turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Star")
turtle_instance=turtle.Turtle()
for i in range(6):
    turtle_instance.left(60)
    turtle_instance.forward(100)
    turtle_instance.right(120)
    turtle_instance.forward(100)
turtle.done()
"""turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)

turtle_instance2=turtle.Turtle()
turtle_instance2.forward(150)
turtle_instance2.right(90)
turtle_instance2.forward(150)
turtle.done()"""
