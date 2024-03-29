from turtle import *

from baord import Board


def max_history():
    with open("max_score", 'r') as file:
        cont = file.read()
    return cont


class Cube:

    def __init__(self):
        self.brd = Board()
        self.cubes = {}  # abstract pos-> real pos
        self.txts = {}  # abstract pos -> Turtles
        self.point = 0
        self.prev_max = max_history()

        self.point_obj = Turtle()
        self.create_cubes()
        self.create_numbers()
        self.score_txt()
        self.game_goes = True
        self.end_of_the_game_happened = False

    def update_max(self):
        with open("max_score", 'r') as file:
            cont = file.read()
        if int(cont) < self.point:
            with open("max_score", 'w') as file:
                file.write(str(self.point))
            self.prev_max = self.point
            return True
        return False

    def create_cubes(self):
        y = 200
        for i in range(0, 4):
            x = -200
            for k in range(0, 4):
                t = Turtle()
                t.shape("square")
                t.shapesize(6.2, 6.2)
                t.color("blue")
                t.penup()
                t.goto(x, y)
                self.cubes[(i, k)] = t.pos()
                x += 130
            y -= 130

    def create_numbers(self):
        for x, y in self.cubes.items():
            txt = Turtle()
            txt.color("white")
            txt.hideturtle()
            self.txts[x] = txt
            txt.penup()
            pp = self.cubes[x]
            txt.goto(pp[0], pp[1] - 12)

    def write_txt(self, value_board):
        for p, val in value_board.items():
            self.txts[p].clear()
            if val != 0:
                self.txts[p].write(f"{val}", align="center", font=("Arial", 28, "normal"))

    def left(self):
        direction = "left"
        self.brd.move(direction)
        self.point += self.brd.concatinate(direction)
        self.brd.move(direction)
        self.brd.random_2_4()
        self.write_txt(self.brd.board)
        self.update_score()

    def up(self):
        direction = "up"
        self.brd.move(direction)
        self.point += self.brd.concatinate(direction)
        self.brd.move(direction)
        self.brd.random_2_4()
        self.write_txt(self.brd.board)
        self.update_score()

    def down(self):
        direction = "down"
        self.brd.move(direction)
        self.point += self.brd.concatinate(direction)
        self.brd.move(direction)
        self.brd.random_2_4()
        self.write_txt(self.brd.board)
        self.update_score()  # amat shevucvale adgili

    def right(self):
        direction = "right"
        self.brd.move(direction)
        self.point += self.brd.concatinate(direction)
        self.brd.move(direction)
        self.brd.random_2_4()
        self.write_txt(self.brd.board)
        self.update_score()

    def score_txt(self):
        self.point_obj.color("red")
        self.point_obj.hideturtle()
        self.point_obj.penup()
        self.point_obj.goto(0, 300)
        self.point_obj.write(f"Score: {self.point}, MAX: {self.prev_max}", align="center", font=("Arial", 28, "normal"))

    def update_score(self):
        if not self.brd.game_continues():
            if not self.end_of_the_game_happened:
                self.end_of_the_game_happened = True
                self.end_of_the_game()
            else:
                pass
        else:
            if not self.end_of_the_game_happened:
                self.point_obj.clear()
                self.point_obj.write(f"Score: {self.point}, MAX: {self.prev_max}", align="center",
                                     font=("Arial", 28, "normal"))

    def end_of_the_game(self):
        self.game_goes = False
        self.point_obj.clear()
        if self.update_max():
            self.point_obj.write(f"Congrats! You achieve new MAX {self.prev_max}", align="center",
                                 font=("Arial", 28, "normal"))
        else:
            self.point_obj.write(f"End of the game ;( Score: {self.point}, MAX: {self.prev_max}", align="center",
                                 font=("Arial", 28, "normal"))


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
