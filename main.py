from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("white")
screen.title("SnakeGame")
screen.tracer(0)

sc = Scoreboard()



snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sc.increase_score()

    if snake.head.xcor() > 500 or snake.head.xcor() < -500 or snake.head.ycor() > 500 or snake.head.ycor() < -500:
        game_is_on = False
        sc.game_over()

    for s in snake.whole_s[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            sc.game_over()



screen.exitonclick()