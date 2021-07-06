from sudoku_generator import *


def set_new_sample():

    #########################################
    # ... ... ... ... ...
    # ... ... ... ... ...
    # WRITE YOUR SAMPLE GRID ARRANGEMENT HERE AS new_board.figure[0][0].set_val(1)
    # ... ... ... ... ...
    # ... ... ... ... ...
    #########################################
    pass


def sample_test():
    sample_sudoku = board()
    sample_sudoku.set_sample()  # you may also use new_board.set_new_sample() instead
    sample_sudoku.calibrate()
    print(sample_sudoku)
    backtrack(sample_sudoku, 1)
    print(ans_boards[0])


def random_board():
    random_sudoku = generate_sudoku()
    print(random_sudoku)
    random_sudoku.calibrate()
    backtrack(random_sudoku, 1)
    while True:
        if input("Enter 'SHOW' to see the answer >> ") == 'SHOW':
            print(ans_boards[0])
            break


sample_test()
# random_board()
