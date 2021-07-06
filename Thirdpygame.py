import pygame as pg
from time import sleep
from random import randint


def pro_turn(list, moveidx, start, end, cpu, max):  # AI USING MINIMAX ALGORITHM
    if (start == end - 1) or (start == end):
        val = -1
        if check_result(list, False) == cpu:
            val = 1
        elif check_result(list, False) == 2:
            val = 0.1
        return val * list[moveidx]
    elif max:
        best_val = -10
        for i in range(start, end):
            list[start], list[i] = list[i], list[start]  # future turns
            val_multiplied = pro_turn(list, moveidx, start + 1, end, cpu, False)  # fixing previous turn
            if val_multiplied > best_val:
                best_val = val_multiplied  # maximizing best value
            list[start], list[i] = list[i], list[start]  # backtracking
        return best_val  # loop ends here & so it's a parent node
    else:
        best_val = 10
        for i in range(start, end):
            list[start], list[i] = list[i], list[start]  # future turns
            val_multiplied = pro_turn(list, moveidx, start + 1, end, cpu, True)  # fixing previous turn
            if val_multiplied < best_val:
                best_val = val_multiplied  # minimizing best value
            list[start], list[i] = list[i], list[start]  # backtracking
        return best_val  # loop ends here & so it's a parent node


def next_turn(x, y):
    if (150 <= x < 257) and (120 <= y < 223): return 6
    if (257 <= x < 364) and (120 <= y < 223): return 1
    if (364 <= x < 471) and (120 <= y < 223): return 8
    if (150 <= x < 257) and (223 <= y < 326): return 7
    if (257 <= x < 364) and (223 <= y < 326): return 5
    if (364 <= x < 471) and (223 <= y < 326): return 3
    if (150 <= x < 257) and (326 <= y < 429): return 2
    if (257 <= x < 364) and (326 <= y < 429): return 9
    if (364 <= x < 471) and (326 <= y < 429): return 4


def show(sign, grid):
    img = pg.image.load('C:/Users/USER9/PycharmProjects/pygame/Thirdpygame_extras/' + sign + '.png')
    if grid == 6:
        image_layer.blit(img, (151, 121))
    elif grid == 1:
        image_layer.blit(img, (258, 121))
    elif grid == 8:
        image_layer.blit(img, (365, 121))
    elif grid == 7:
        image_layer.blit(img, (151, 224))
    elif grid == 5:
        image_layer.blit(img, (258, 224))
    elif grid == 3:
        image_layer.blit(img, (365, 224))
    elif grid == 2:
        image_layer.blit(img, (151, 327))
    elif grid == 9:
        image_layer.blit(img, (258, 327))
    elif grid == 4:
        image_layer.blit(img, (365, 327))
    display_window.update()  # updates to the screen


def win(sign):
    while True:
        clock.tick(15)
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
        if sign == 'NONE':
            image_layer.fill((18, 20, 22))
            message("GAME TIED", 350, 170, 110, 250, 220, 80)
            button('RESTART', 250, 300, 200, 120)
        else:
            img = pg.image.load('C:/Users/USER9/PycharmProjects/pygame/Thirdpygame_extras/' + sign + '.png')
            image_layer.fill((18, 20, 22))
            image_layer.blit(img, (180, 120))
            message(" WON", 380, 170, 110, 250, 220, 80)
            button('RESTART', 250, 300, 200, 120)
        display_window.update()  # updates to the screen


def check_result(turns, value):
    if value:
        sleep(0.5)
        if len(turns) < 5:
            return
        elif turns[0] + turns[2] + turns[4] == 15:
            win('X')
        if len(turns) < 6:
            return
        elif turns[1] + turns[3] + turns[5] == 15:
            win('O')
        if len(turns) < 7:
            return
        elif turns[6] + turns[2] + turns[4] == 15:
            win('X')
        elif turns[0] + turns[6] + turns[4] == 15:
            win('X')
        elif turns[0] + turns[2] + turns[6] == 15:
            win('X')
        if len(turns) < 8:
            return
        elif turns[7] + turns[3] + turns[5] == 15:
            win('O')
        elif turns[1] + turns[7] + turns[5] == 15:
            win('O')
        elif turns[1] + turns[3] + turns[7] == 15:
            win('O')
        if len(turns) < 9:
            return
        elif turns[8] + turns[2] + turns[4] == 15:
            win('X')
        elif turns[6] + turns[8] + turns[4] == 15:
            win('X')
        elif turns[0] + turns[6] + turns[8] == 15:
            win('X')
        elif turns[0] + turns[2] + turns[8] == 15:
            win('X')
        elif turns[0] + turns[8] + turns[4] == 15:
            win('X')
        elif turns[8] + turns[2] + turns[6] == 15:
            win('X')
        else:
            win('NONE')
    elif not value:
        if turns[0] + turns[2] + turns[4] == 15:
            return 1  # for 'X'
        elif turns[1] + turns[3] + turns[5] == 15:
            return 0  # for 'O'
        elif turns[6] + turns[2] + turns[4] == 15:
            return 1
        elif turns[0] + turns[6] + turns[4] == 15:
            return 1
        elif turns[0] + turns[2] + turns[6] == 15:
            return 1
        elif turns[7] + turns[3] + turns[5] == 15:
            return 0
        elif turns[1] + turns[7] + turns[5] == 15:
            return 0
        elif turns[1] + turns[3] + turns[7] == 15:
            return 0
        elif turns[8] + turns[2] + turns[4] == 15:
            return 1
        elif turns[6] + turns[8] + turns[4] == 15:
            return 1
        elif turns[0] + turns[6] + turns[8] == 15:
            return 1
        elif turns[0] + turns[2] + turns[8] == 15:
            return 1
        elif turns[0] + turns[8] + turns[4] == 15:
            return 1
        elif turns[8] + turns[2] + turns[6] == 15:
            return 1
        else:
            return 2  # for TIE


def message(text, x, y, size, a, b, c):  # last three are R-G-B
    font = pg.font.SysFont(None, size)
    txt_surface = font.render(text, True, (a, b, c))
    txt_box = txt_surface.get_rect()
    txt_box.center = ((x, y))
    image_layer.blit(txt_surface, txt_box)  # renders the image


def button(text, x, y, wd, hg):
    mouseptr = pg.mouse.get_pos()  # returns the coordinate as tuples like (300,469)
    mouseclk = pg.mouse.get_pressed()  # returns clicked or not in binary like (1,0,0)
    if (x + wd > mouseptr[0] > x) and (y + hg > mouseptr[1] > y):
        pg.draw.rect(image_layer, [40, 40, 60], (x, y, wd, hg))
        if mouseclk == (1, 0, 0):
            if text == 'BEGINNER':
                gameloop_bgn()
            elif text == 'PROFESSIONAL':
                gameloop_pro()
            elif text == 'RESTART':
                introloop()
    else:
        pg.draw.rect(image_layer, [30, 30, 40], (x, y, wd, hg))
    message(text, x + wd / 2, y + hg / 2, 40, 50, 250, 250)


def introloop():
    image_layer.fill((20, 22, 24))
    image_layer.blit(board, (0, 0))
    image_layer.blit(board, (400, 0))
    image_layer.blit(board, (0, 200))
    image_layer.blit(board, (400, 200))
    image_layer.blit(board, (150, 0))
    image_layer.blit(board, (150, 200))
    while True:
        clock.tick(15)
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
        message('T I C', 150, 150, 115, 255, 80, 100)
        message('T A C', 350, 150, 100, 80, 255, 100)
        message('T O E', 550, 150, 115, 100, 80, 255)
        button('BEGINNER', 50, 300, 175, 100)
        button('PROFESSIONAL', 425, 300, 250, 100)
        display_window.update()  # updates to the screen


def gameloop_bgn():
    if randint(0, 10) <= 6:
        turns = []
    else:
        turns = [randint(1, 9)]
    cpu_turn = False
    while True:
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
            mouseptr = pg.mouse.get_pos()
            if (150 <= mouseptr[0] < 471) and (120 <= mouseptr[1] < 429):
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    grid_num = next_turn(mouseptr[0], mouseptr[1])
                    for i in turns:
                        if i == grid_num: grid_num = 0
                    if grid_num != 0:
                        turns.append(grid_num)
                        cpu_turn = True
        image_layer.fill((18, 20, 22))
        image_layer.blit(board, (150, 120))
        for i in range(0, len(turns), 2):
            show('X', turns[i])
            if len(turns) > i + 1: show('O', turns[i + 1])
        check_result(turns, True)
        if len(turns) != 9:
            while cpu_turn:
                next = randint(1, 9)
                if next not in turns:
                    turns.append(next)
                    cpu_turn = False
        image_layer.fill((18, 20, 22))
        image_layer.blit(board, (150, 120))
        for i in range(0, len(turns), 2):
            show('X', turns[i])
            if len(turns) > i + 1: show('O', turns[i + 1])
        check_result(turns, True)
        clock.tick(30)
        display_window.update()  # updates to the screen


def gameloop_pro():
    cpu_sign = 0  # for 'O'
    if randint(0, 10) <= 6:
        turns = []
    elif randint(0, 10) <= 8:
        turns = [2 * randint(1, 4)]
        cpu_sign = 1  # for 'X'
    else:
        turns = [5]
        cpu_sign = 1  # for 'X'
    cpu_turn = False
    while True:
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
            mouseptr = pg.mouse.get_pos()
            if (150 <= mouseptr[0] < 471) and (120 <= mouseptr[1] < 429):
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    grid_num = next_turn(mouseptr[0], mouseptr[1])
                    for i in turns:
                        if i == grid_num: grid_num = 0
                    if grid_num != 0:
                        turns.append(grid_num)
                        cpu_turn = True
        image_layer.fill((18, 20, 22))
        image_layer.blit(board, (150, 120))
        for i in range(0, len(turns), 2):
            show('X', turns[i])
            if len(turns) > i + 1: show('O', turns[i + 1])
        check_result(turns, True)
        if len(turns) != 9:
            while cpu_turn:
                if 5 not in turns:
                    turns.append(5)
                    cpu_turn = False
                else:
                    start = len(turns)
                    for i in range(1, 10):
                        if i not in turns: turns.append(i)
                    end = len(turns)
                    grid_num = abs(pro_turn(turns, start, start, end, cpu_sign, True))
                    turns = turns[:start]
                    if grid_num < 1:
                        turns.append(int(grid_num * 10))
                    else:
                        turns.append(int(grid_num))
                    cpu_turn = False
        image_layer.fill((18, 20, 22))
        image_layer.blit(board, (150, 120))
        for i in range(0, len(turns), 2):
            show('X', turns[i])
            if len(turns) > i + 1: show('O', turns[i + 1])
        check_result(turns, True)
        clock.tick(30)
        display_window.update()  # updates to the screen


pg.init()  # initiate PYGAME ...
clock = pg.time.Clock()
pg.mixer.init()  # music initiation
audio = pg.mixer.music
audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Thirdpygame_extras\music.mp3')
audio.play(-1)
audio.set_volume(0.5)
display_window = pg.display  # getting the background display,other layers of images
image_layer = display_window.set_mode((700, 500))
display_window.set_caption("MY  THIRD  GAME")
board = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Thirdpygame_extras\board.png')
introloop()
# To create icon make a batch file -> python "C:\Users\USER9\PycharmProjects\pygame\Thirdpygame.py"
