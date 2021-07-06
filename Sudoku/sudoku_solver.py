from sudoku_board import *

ans_boards = []


def is_list_invalid(_list_):
    for i in range(1, 10):
        if _list_.count(i) > 1:
            return True
    return False


def is_valid(board1):
    for i in range(9):
        _list_ = []
        for j in range(9):
            _list_.append(board1.figure[i][j].val)
        if is_list_invalid(_list_):
            return False
    for i in range(9):
        _list_ = []
        for j in range(9):
            _list_.append(board1.figure[j][i].val)
        if is_list_invalid(_list_):
            return False
    idx = [1, 4, 7]
    inc = [-1, 0, 1]
    for i in idx:
        for j in idx:
            _list_ = []
            for i_inc in inc:
                for j_inc in inc:
                    _list_.append(board1.figure[i + i_inc][j + j_inc].val)
            if is_list_invalid(_list_):
                return False
    return True


def backtrack(board1: board, depth: int):
    if board1.recent_grid.x == 8 and board1.recent_grid.y == 8:
        global ans_boards
        if board1.recent_grid.edit:
            for i in range(1, 10):
                board1.recent_grid.update_val(i)
                if is_valid(board1):
                    ans_boards.append(board1.copy_board())
                    break
        else:
            if is_valid(board1):
                ans_boards.append(board1.copy_board())
    else:
        for i in range(1, 10):
            board1.recent_grid.update_val(i)
            if is_valid(board1):
                board1.next_board()
                backtrack(board1, depth + 1)
                board1.prev_board()
