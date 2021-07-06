class board:  # outer class
    class grid:  # inner class
        x = None
        y = None

        def __init__(self, _x_, _y_):  # coords of grid is from (0, 0) to (8, 8)
            self.x = _x_
            self.y = _y_
            self.val = None
            self.edit = True

        def set_val(self, number):
            if number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                self.val = int(number)
                self.edit = False
            else:
                raise Exception("Access Denied")

        def update_val(self, number):
            if number in [1, 2, 3, 4, 5, 6, 7, 8, 9] and self.edit:
                self.val = int(number)
            else:
                raise Exception("Operation Denied")

        def reset_grid(self):
            self.val = 0
            self.edit = True

        def __str__(self):
            return "\nvalue: " + str(self.val) + ", coords: (" + str(self.x) + ", " + str(
                self.y) + ") " + ", edit: " + str(self.edit)

    def __init__(self):
        self.figure = []  # contains the whole board
        for i in range(9):
            self.figure.append([self.grid(i, j) for j in range(9)])
        self.recent_grid = self.figure[0][0]

    def copy_board(self):
        copy = board()
        for i_ in range(9):
            for j_ in range(9):
                copy.figure[i_][j_].val = self.figure[i_][j_].val
                copy.figure[i_][j_].edit = self.figure[i_][j_].edit
        return copy

    def next_board(self):
        recent_x = self.recent_grid.x
        recent_y = self.recent_grid.y
        while recent_x != 8 or recent_y != 8:
            if recent_y < 8:
                recent_y += 1
            else:
                recent_y = 0
                recent_x += 1
            self.recent_grid = self.figure[recent_x][recent_y]
            if self.recent_grid.edit:
                break

    def prev_board(self):
        recent_x = self.recent_grid.x
        recent_y = self.recent_grid.y
        while recent_x != 0 or recent_y != 0:
            if self.recent_grid.edit:
                self.recent_grid.val = None
            if recent_y > 0:
                recent_y -= 1
            else:
                recent_y = 8
                recent_x -= 1
            self.recent_grid = self.figure[recent_x][recent_y]
            if self.recent_grid.edit:
                break

    def calibrate(self):
        recent_x = 0
        recent_y = 0
        self.recent_grid = self.figure[recent_x][recent_y]
        while True:
            if self.recent_grid.val is None:
                break
            if recent_y < 8:
                recent_y += 1
            else:
                recent_y = 0
                recent_x += 1
            self.recent_grid = self.figure[recent_x][recent_y]

    def set_sample(self):
        self.figure[0][0].set_val(5)
        self.figure[0][4].set_val(7)
        self.figure[1][0].set_val(6)
        self.figure[1][3].set_val(1)
        self.figure[1][4].set_val(9)
        self.figure[1][5].set_val(5)
        self.figure[2][1].set_val(9)
        self.figure[2][2].set_val(8)
        self.figure[2][7].set_val(6)
        self.figure[3][0].set_val(8)
        self.figure[3][4].set_val(6)
        self.figure[3][8].set_val(3)
        self.figure[4][0].set_val(4)
        self.figure[4][3].set_val(8)
        self.figure[4][5].set_val(3)
        self.figure[4][8].set_val(1)
        self.figure[5][0].set_val(7)
        self.figure[5][4].set_val(2)
        self.figure[5][8].set_val(6)
        self.figure[6][1].set_val(6)
        self.figure[6][6].set_val(2)
        self.figure[6][7].set_val(8)
        self.figure[7][3].set_val(4)
        self.figure[7][4].set_val(1)
        self.figure[7][5].set_val(9)
        self.figure[7][8].set_val(5)
        self.figure[8][4].set_val(8)
        self.figure[8][7].set_val(7)

    def __str__(self):
        return "\n___________________\n|" + "|\n|".join(
            ("|".join(("_" if grid.val is None else str(grid.val)) for grid in each_row)) for each_row in
            self.figure) + "|\n___________________\n"


if __name__ == "__main__":
    new_board = board()
    new_board.set_sample()
    print("PRINTING SAMPLE")
    print(new_board)
    print("\n#####BYE#####")
