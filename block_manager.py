import turtle as t
import random

COLORS = ['green', 'blue', 'purple','red', 'orange', 'yellow', ]

class Block_Manager():
    def __init__(self):
        self.all_blocks = []

    def create_block(self, startx ,start_y, i):
        new_block = t.Turtle('square')
        new_block.color(COLORS[i-1])
        new_block.shapesize(stretch_wid=2, stretch_len=5)  #x = 100px #y= 40px
        new_block.penup()
        y_position = start_y
        x_position = startx + (i * 110)
        new_block.goto(x_position, y_position)
        self.all_blocks.append(new_block)

