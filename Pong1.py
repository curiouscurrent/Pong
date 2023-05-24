import turtle

wn = turtle.Screen()
wn.title("Pong by @curiouscurrent")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # for max speed 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # for max speed 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()
ball.speed(0) # for max speed 
ball.shape("circle")
ball.color("white")

ball.penup()
ball.goto(0,0)

# Function
def paddle_a_up():
    y = paddle_a.ycor() #assigning the current y coordinate to y
    y += 20
    paddle_a.sety(y) #set y to new y

#Keyboard Binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")

# Main function
while True:
    wn.update()