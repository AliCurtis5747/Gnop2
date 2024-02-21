import turtle as turt
import time


window = turt.Screen()
window.title("GNOP 2")
window.bgcolor("white")
window.setup(width = 800, height = 750)

pen = turt.Turtle()
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 330)



paddle1 = turt.Turtle()
paddle1.speed(0)
paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(stretch_wid = 2, stretch_len = 0.5)
paddle1.color("black")
paddle1.goto(-320, 0)

paddle2 = turt.Turtle()
paddle2.speed(0)
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(stretch_wid = 2, stretch_len = 0.5)
paddle2.color("black")
paddle2.goto(320, 0)

gnopBall = turt.Turtle()
gnopBall.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
gnopBall.speed(0)
gnopBall.penup()
gnopBall.shape("circle")
gnopBall.color("black")
gnopBall.goto(0,0)

#methods for moving the player's paddle
def paddle1_moveUp():
    y = paddle1.ycor() + 10
    paddle1.sety(y)

def paddle1_moveDown():
    y = paddle1.ycor() - 10
    paddle1.sety(y)


pen.write("player 1 :: 0 ", align = "right", font = ('Arial', 23, 'normal'))
pen.write("player 2 :: 0 ", align = "left", font = ('Arial', 23, 'normal'))
window.listen()

    
def main():
    dx = 2
    dy = 2
    player1 = 0
    player2 = 0

    while(True):
        if(player1 < player2 and player2 - player1 > 3):
            print("YOU LOSE! Please relaunch the program to play again")
            return 0

        window.update()
        window.onkeypress(paddle1_moveUp, "Up")
        window.onkeypress(paddle1_moveDown, "Down")

#scripts for scoring
        if(gnopBall.xcor() < -350):
            pen.clear()
            dx = 2
            dy = 2
            gnopBall.goto(0,0)
            dx *= -1
            player2 += 1
            pen.write("player 1 :: {} player 2 :: {} ".format(player1, player2), align = "center", font = ('Arial', 23, 'normal'))
            window.update()
        if(gnopBall.xcor() > 350):
            pen.clear()
            dx = 2
            dy = 2
            gnopBall.goto(0,0)
            dx *= -1
            player1 += 1
            pen.write("player 1 :: {} player 2 :: {} ".format(player1, player2), align = "center", font = ('Arial', 23, 'normal'))
            window.update()

# collision for the ball, walls and paddles
        if(gnopBall.xcor() <= paddle1.xcor() and gnopBall.ycor() < (paddle1.ycor() + 40) and gnopBall.ycor() > (paddle1.ycor() - 40)):
            dx -= 2
            dx *= -1
            gnopBall.sety(gnopBall.ycor() + dy)
            gnopBall.setx(gnopBall.xcor() + dx)

        if(gnopBall.xcor() >= paddle2.xcor() and gnopBall.ycor() < (paddle2.ycor() + 40) and gnopBall.ycor() > (paddle2.ycor() - 40)):
            dx += 2
            dx *= -1
            gnopBall.sety(gnopBall.ycor() + dy)
            gnopBall.setx(gnopBall.xcor() + dx)

        if(gnopBall.ycor() > 325 or gnopBall.ycor() < -325):
            dy *= -1
            gnopBall.sety(gnopBall.ycor() + dy)
            gnopBall.setx(gnopBall.xcor() + dx)
        window.update()

#the AI script that moves the CPU paddle
        if(gnopBall.xcor() > -100):
            if(paddle2.ycor() > gnopBall.ycor()):
                y = paddle2.ycor() - 5
                paddle2.sety(y)
                window.update()
            if(paddle2.ycor() < gnopBall.ycor()):
                y = paddle2.ycor() + 5
                paddle2.sety(y)
                window.update()
        
            
#moves the ball
        gnopBall.sety(gnopBall.ycor() + dy)
        gnopBall.setx(gnopBall.xcor() + dx)

main()


    
