import random

LENGTH = 4
WIDTH = 4


class Board:
    # LIST OF METHODS:
    # - move(dir input)
    # - concat (dir input)

    def __init__(self):
        self.board = {}
        self.creating_board()

    def printing_board(self):
        for i in range(0, LENGTH):
            line = ""
            for k in range(0, LENGTH):
                line += str(self.board[(i, k)])
                line += " "
            print(line)

    def creating_board(self):
        for i in range(0, LENGTH):
            for k in range(0, LENGTH):
                self.board[(i, k)] = 0
        self.random_2_4()

    def random_2_4(self):
        temp = list(map(lambda n: n[0], filter(lambda n: n[1] == 0, self.board.items())))
        if temp:
            random.shuffle(temp)
            lst = [2, 2, 2, 2, 4]  # chance of 2 should be higher
            random.shuffle(lst)
            self.board[temp[0]] = lst[0]

            # if element is added for the first time
            if len(temp) == 16:
                self.board[temp[1]] = lst[1]

    def move(self, direction):
        for i in range(0, LENGTH):
            index = 0
            last = 0
            step = 1
            if direction == "right" or direction == "down":
                index = LENGTH - 1
                last = LENGTH - 1
                step = -1
            while 0 <= index < LENGTH:
                if direction == "right" or direction == "left":
                    if self.board[(i, index)] != 0:
                        if self.board[(i, last)] == 0:
                            self.board[(i, last)] = self.board[(i, index)]
                            self.board[(i, index)] = 0
                        last += step
                else:
                    if self.board[(index, i)] != 0:
                        if self.board[(last, i)] == 0:
                            self.board[(last, i)] = self.board[(index, i)]
                            self.board[(index, i)] = 0
                        last += step
                index += step

    def concatinate(self, direction):
        score_gained = 0
        if direction == "left" or direction == "right":
            for i in range(0, LENGTH):
                index = 0
                step = 1
                if direction == "right":
                    index = LENGTH - 1
                    step = -1
                while (direction == "left" and index < LENGTH - 1) or (direction == "right" and index > 0):
                    if self.board[(i, index)] == self.board[(i, index + step)] and self.board[(i, index)] != 0:
                        self.board[(i, index)] = self.board[(i, index)] * 2

                        score_gained += self.board[(i, index)]

                        self.board[(i, index + step)] = 0
                    index += step
        else:
            for i in range(0, LENGTH):
                index = 0
                step = 1
                if direction == "down":
                    index = LENGTH - 1
                    step = -1
                while (direction == "up" and index < LENGTH - 1) or (direction == "down" and index > 0):
                    if self.board[(index, i)] == self.board[(index + step, i)]:
                        self.board[(index, i)] = self.board[(index, i)] * 2

                        score_gained += self.board[(index, i)]

                        self.board[(index + step, i)] = 0
                    index += step
        return score_gained

    def game_continues(self):
        temp = list(map(lambda n: n[0], filter(lambda n: n[1] == 0, self.board.items())))
        if not temp:
            for i in range(0, LENGTH):
                for k in range(0, LENGTH):
                    if i != LENGTH - 1 and self.board[(i, k)] == self.board[(i + 1, k)]:
                        return True
                    elif k != LENGTH - 1 and self.board[(i, k)] == self.board[(i, k + 1)]:
                        return True
            return False
        else:
            return True
