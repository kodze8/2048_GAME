from turtle import *
from Cubes import Cube

scr = Screen()
scr.screensize(400, 400)

scr.tracer(0)
cube = Cube()
scr.update()

cube.write_txt(cube.brd.board)

while cube.game_goes:
    scr.listen()
    scr.onkey(cube.left, "Left")
    scr.onkey(cube.right, "Right")
    scr.onkey(cube.up, "Up")
    scr.onkey(cube.down, "Down")
    cube.game_goes = False

scr.exitonclick()
cube.update_max()
