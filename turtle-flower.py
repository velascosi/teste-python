import turtle

window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("arrow")
brad.color("black")
brad.speed(6)

brad.shape("classic")
brad.color("blue")
brad.speed(10)

brad.pu()
brad.setpos(-200,0)
brad.pd()

for i in range(1,37):  
    brad.left(35)
    brad.forward(50)
    brad.right(35)
    brad.forward(50)
    brad.right(145)
    brad.forward(50)
    brad.right(35)
    brad.forward(50)
    brad.right(10)
brad.seth(270)
brad.forward(200)
        
window.exitonclick()
