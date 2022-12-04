from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.starting_pos = STARTING_POS
        self.whole_s = list()
        self.create_snake()
        self.head = self.whole_s[0]


    def create_snake(self):
        for pos in STARTING_POS:
            self.add_snake(pos)

    def add_snake(self, pos):
        new_s = Turtle("square")
        new_s.color("black")
        new_s.penup()
        new_s.setpos(pos)
        self.whole_s.append(new_s)

    def extend(self):
        self.add_snake(self.whole_s[-1].position())
    
    def move(self):
        for s in range(len(self.whole_s)-1, 0, -1):
            new_x = self.whole_s[s-1].xcor()
            new_y = self.whole_s[s-1].ycor()
            self.whole_s[s].setpos(new_x, new_y)
        self.head.forward(DISTANCE)
        

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)