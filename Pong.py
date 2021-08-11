import turtle
import os

class Things:
    def __init__(self, x, xy, y):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.xy = xy
        self.turtle.shapesize(stretch_wid=xy, stretch_len=1)
        self.turtle.penup()
        self.x = x
        self.y = y
        self.turtle.goto(self.x, self.y)

    def up(self):
        self.ycor = self.turtle.ycor()
        self.ycor += 20
        self.turtle.sety(self.ycor)
        
    def down(self):
        ycor = self.turtle.ycor()
        ycor -= 20
        self.turtle.sety(ycor)






class Paddle(Things):
    def __init__(self, x, xy=5, y=0):
        super(Paddle,self).__init__(x, xy=5, y=0)

 





class Ball(Things):
    def __init__(self, x, xy=1, y=0):
        super(Ball,self).__init__(x, xy=1, y=0)
        self.dx = 0.3
        self.dy = 0.3






wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)




#Paddle A
paddle_a = Paddle(-350)

def paddle_a_up():
    y = paddle_a.turtle.ycor()
    y += 20
    paddle_a.turtle.sety(y)


#Paddle B
paddle_b = Paddle(350)





#Ball
ball = Ball(0)

#Keyboard binding
wn.listen()
wn.onkey(paddle_a.up, "w")
wn.onkey(paddle_a.down, "s")
wn.onkey(paddle_b.up, "Up")
wn.onkey(paddle_b.down, "Down")


# MAin game loop
while True:
    wn.update()

    #MOve ball
    ball.turtle.setx(ball.turtle.xcor() + ball.dx)
    ball.turtle.sety(ball.turtle.ycor() + ball.dy)

    #border checking
    if ball.turtle.ycor() > 290:
        ball.turtle.sety(290)
        ball.dy *= -1

    if ball.turtle.ycor() < -290:
        ball.turtle.sety(-290)
        ball.dy *= -1

    if ball.turtle.xcor() > 390:
        ball.turtle.goto(0, 0)
        ball.dx *= -1

    if ball.turtle.xcor() < -390:
        ball.turtle.goto(0, 0)
        ball.dx *= -1

    #Paddle and ball collisions
    if (ball.turtle.xcor() > 340 and ball.turtle.xcor() < 350) and (ball.turtle.ycor() < paddle_b.turtle.ycor() + 40 and ball.turtle.ycor() > paddle_b.turtle.ycor() - 40):
        ball.turtle.setx(340)
        ball.dx *= -1
    if (ball.turtle.xcor() < -340 and ball.turtle.xcor() > -350) and (ball.turtle.ycor() > paddle_a.turtle.ycor() - 40 and ball.turtle.ycor() < paddle_a.turtle.ycor() + 40):
        ball.turtle.setx(-340)
        ball.dx *= -1

