from sudoku_solver import *
from random import randint


def generate_sudoku():
    _board_ = board()
    for k in range(6):
        x = randint(0, 2)
        y = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
        x = randint(3, 5)
        y = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
        x = randint(6, 8)
        y = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
        y = randint(0, 2)
        x = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
        y = randint(3, 5)
        x = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
        y = randint(6, 8)
        x = randint(0, 8)
        _board_.figure[x][y].set_val(randint(1, 9))
        while not is_valid(_board_):
            _board_.figure[x][y].set_val(randint(1, 9))
    _board_.calibrate()
    backtrack(_board_, 1)
    _board_.recent_grid.edit = False  # reassuring of starting blockages
    if len(ans_boards) > 1:
        print("Just wait a few seconds more...we are almost ready...")
        choice = randint(0, len(ans_boards) - 1)
        while len(ans_boards) > 1:
            row = randint(0, 8)
            col = randint(0, 8)
            while not _board_.figure[row][col].edit:
                row = randint(0, 8)
                col = randint(0, 8)
            value = ans_boards[choice].figure[row][col].val
            j = 0
            while j != len(ans_boards):
                if ans_boards[j].figure[row][col].val != value:
                    del ans_boards[j]
                    _board_.figure[row][col].set_val(value)  # assures minimum one deletion of excess possibilities
                    if j < choice:
                        choice -= 1
                else:
                    j += 1
    elif len(ans_boards) == 1:
        pass
    else:
        print("... ... ... ... ...")
        return generate_sudoku()
    _board_.recent_grid.val = None
    _board_.recent_grid.edit = True
    return _board_
