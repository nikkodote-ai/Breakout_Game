import turtle as t

from block_manager import Block_Manager


#-----WINDOW----#
window = t.Screen()
window.title("BreakOut Game")
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0, 0)
window.delay(0)

#---BLOCKS/BRICKS---#
block_manager = Block_Manager()

# make block objects
for i in range(7):
    for j in range(5):
        # block_manager.create_block(-335, -50,i)
        block_manager.create_block(-335, -50 + j * 60, i)

# create paddle
paddle = t.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('blue')
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0, -200)

# create ball
ball = t.Turtle()
ball.speed(3)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, -80)
ball.dx = 0.2
ball.dy = 0.2

def paddle_right():
    x = paddle.xcor()
    x += 80
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 80
    paddle.setx(x)


window.listen()
window.onkey(paddle_right, 'Right')
window.onkey(paddle_left, 'Left')

continue_game = True

while True:
    window.update()

    if len(block_manager.all_blocks) != 0:
        # keep the ball moving
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # contain the ball within the borders
        # bounce when it hits the top and sides
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy = ball.dy * -1

        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx = ball.dx * -1

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx = ball.dx * -1

        # when it reaches the bottom, reset
        if ball.ycor() < -290:
            ball.goto(0, -100)
            ball.dy = -ball.dy
            # add score

        # ball collision with paddle
        if (ball.ycor() < -190 and ball.ycor() > -210) and (
                ball.xcor() < paddle.xcor() + 100 and ball.xcor() > paddle.xcor() - 100):
            ball.sety(-190)
            ball.dy *= -1

        # Detect if the ball hits a block. if yes, remove the block
        for block in block_manager.all_blocks:
            if (ball.ycor() < block.ycor() + 20 and ball.ycor() > block.ycor() - 20) and (
                    ball.xcor() < block.xcor() + 67 and ball.xcor() > block.xcor() - 67):
                ball.dy *= -1
                block.hideturtle()
                block_manager.all_blocks.remove(block)
    else:
        continue_game = False
window.exitonclick()
