import pygame as pg
from time import sleep
from random import randrange


class snake(object):
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def show(self):
        block = pg.image.load(self.type + '.png')
        image_layer.blit(block, (self.x, self.y))


def food(x, y, type):
    if type == 1:
        image_layer.blit(food_small, (x, y))
    elif type == 2:
        image_layer.blit(food_big, (x, y))


def highscore(count):
    record = open(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\record.txt', 'r')
    highscore = int(record.read())
    if count <= highscore:
        record.close()
        return highscore
    record = open(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\record.txt', 'w')
    record.write(str(count))
    record.close()
    return count


def crash(count):
    image_layer.blit(end_score, (50, 20))
    message("SCORE: " + str(count), 550, 150, 120)
    message("HIGHscore: " + str(highscore(count)), 550, 250, 80)
    audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\score.mpeg')
    audio.play(1)
    sleep(2)
    game_loop()


def message(text, x, y, size):
    font = pg.font.SysFont(None, size)
    txt_surface = font.render(text, True, (150, 255, 150))
    txt_box = txt_surface.get_rect()
    txt_box.center = ((x, y))
    image_layer.blit(txt_surface, txt_box)  # renders the image
    display_window.update()  # updates to the screen


def score(count):
    font = pg.font.SysFont(None, 30)
    txt_surface = font.render("SCORE: " + str(count), True, (255, 255, 255))
    image_layer.blit(txt_surface, (5, 5))


def game_loop():
    audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\music.mpeg')
    audio.play(-1)
    audio.set_volume(0.25)
    snake_blocks = [100, 100, 90, 100]
    x = snake_blocks[0]
    y = snake_blocks[1]
    dx = 8
    dy = 0
    direction = 'right'
    blocks_num = 0
    food_x = 103
    food_y = 103
    type = 1
    while True:  # runs repetitively in accordance with fps
        clock.tick(15)
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
            if event.type == pg.KEYDOWN:  # detects key-pressing
                if event.key == pg.K_LEFT:
                    dx = -15
                    dy = 0
                    direction = 'left'
                elif event.key == pg.K_RIGHT:
                    dx = 15
                    dy = 0
                    direction = 'right'
                elif event.key == pg.K_UP:
                    dx = 0
                    dy = -15
                    direction = 'up'
                elif event.key == pg.K_DOWN:
                    dx = 0
                    dy = 15
                    direction = 'down'
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    dx = -8
                    dy = 0
                    direction = 'left'
                elif event.key == pg.K_RIGHT:
                    dx = 8
                    dy = 0
                    direction = 'right'
                elif event.key == pg.K_UP:
                    dx = 0
                    dy = -8
                    direction = 'up'
                elif event.key == pg.K_DOWN:
                    dx = 0
                    dy = 8
                    direction = 'down'
        x += dx
        y += dy
        snake_blocks.insert(0, x)
        snake_blocks.insert(1, y)
        image_layer.fill((200, 50, 50))
        image_layer.blit(sand_bg, (5, 5))
        if (type == 1) and (y - 9 <= food_y <= y + 9) and (x - 9 <= food_x <= x + 9):
            food_x = randrange(6, 794)
            food_y = randrange(6, 560)
            if randrange(0, 10) < 6:
                type = 1
            else:
                type = 2
            blocks_num += 1
        elif (type == 2) and (y - 17 <= food_y <= y + 17) and (x - 17 <= food_x <= x + 17):
            food_x = randrange(6, 794)
            food_y = randrange(6, 560)
            if randrange(0, 10) < 9:
                type = 1
            else:
                type = 2
            blocks_num += 2
        score(blocks_num - 1)
        food(food_x, food_y, type)
        snake('C:/Users/USER9/PycharmProjects/pygame/Secondpygame_extras/tail' + direction,
              snake_blocks[2 * blocks_num + 2], snake_blocks[2 * blocks_num + 3]).show()
        for i in range(1, blocks_num + 1):
            snake('C:/Users/USER9/PycharmProjects/pygame/Secondpygame_extras/body', snake_blocks[2 * i],
                  snake_blocks[2 * i + 1]).show()
        snake('C:/Users/USER9/PycharmProjects/pygame/Secondpygame_extras/head' + direction, snake_blocks[0],
              snake_blocks[1]).show()
        if (x >= 805) or (x <= 5) or (y >= 576) or (y <= 5): crash(blocks_num - 1)
        for i in range(blocks_num + 1, 0, -1):  # runs from blocks+1(which means tail) to 0+1(so head's excluded)
            if (y - 8 < snake_blocks[2 * i + 1] < y + 8) and (x - 8 < snake_blocks[2 * i] < x + 8): crash(
                blocks_num - 1)
        display_window.update()  # updates


pg.init()  # initiate PYGAME ...
clock = pg.time.Clock()
pg.mixer.init()  # music initiation
audio = pg.mixer.music
display_window = pg.display  # getting the background display,other layers of images
image_layer = display_window.set_mode((810, 581))
display_window.set_caption("MY  SECOND  GAME")
sand_bg = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\ground.jpg')
end_score = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\endscore.png')
food_small = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\food.png')
food_big = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Secondpygame_extras\bigfood.png')
game_loop()
