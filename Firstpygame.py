import pygame as pg
from time import sleep
from random import randrange


def mycar(x, y):
    image_layer.blit(mycar_img, (x, y))  # blit means speedpassing of dataset


def movingcar(x, y, type):
    if type == 1: image_layer.blit(cabcar_img, (x, y))
    if type == 2: image_layer.blit(copcar_img, (x, y))


def divider(y):
    while y <= 750:
        pg.draw.line(image_layer, (255, 255, 255), (500, y), (500, y + 50), 15)  # 15 is thickness
        y += 100


def message(text):
    font = pg.font.SysFont(None, 250)
    txt_surface = font.render(text, True, (255, 255, 255))  # This is white & (0,0,0)is black
    txt_box = txt_surface.get_rect()
    txt_box.center = (500, 350)
    image_layer.blit(txt_surface, txt_box)  # renders the image
    display_window.update()  # updates to the screen


def score(count):
    font = pg.font.SysFont(None, 50)
    txt_surface = font.render("SCORE: " + str(count), True, (255, 255, 255))
    image_layer.blit(txt_surface, (5, 5))


def crash(score):
    image_layer.fill((50, 25, 200))  # new screen -> so fill color
    message("CRASHED")
    sleep(0.2)
    image_layer.fill((200, 25, 50))  # new screen -> so fill color
    message("CRASHED")
    sleep(0.4)
    image_layer.fill((50, 25, 200))  # new screen -> so fill color
    message("CRASHED")
    sleep(0.2)
    image_layer.fill((200, 25, 50))  # new screen -> so fill color
    message("CRASHED")
    sleep(1)
    image_layer.fill((25, 200, 75))
    message("SCORE: " + str(score))
    audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\score.mpeg')
    audio.play(1)
    sleep(1)
    game_loop()


def game_loop():
    audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\music.mpeg')
    audio.play(-1)  # (-1) for continuous play or other integer will loop it that number of times
    audio.set_volume(0.25)
    mycar_x = 450
    mycar_y = 475
    type = 1
    movingcar_x = randrange(200, 800)
    movingcar_y = -250
    movingcar_speed = randrange(5, 10)
    divider_y = -800  #
    dx = 0
    count = 0
    while True:  # runs repetitively in accordance with fps
        clock.tick(30)  # fps(slow-15,medium-30,fast-60) not mentioning tick make it infinite
        for event in pg.event.get():  # example -> get_events = pressing 2 keys & moving cursor at a time
            # print(event) prints all the movements
            if event.type == pg.QUIT: pg.quit()  # for system-exit
            if event.type == pg.KEYDOWN:  # detects key-pressing
                if event.key == pg.K_LEFT:
                    dx = -7  # here each number corresponds to number of pixels
                elif event.key == pg.K_RIGHT:
                    dx = 7
            if event.type == pg.KEYUP:  # detects keypress-releasing, so one time pressing button
                if event.key == pg.K_LEFT:
                    dx = -0.5
                elif event.key == pg.K_RIGHT:
                    dx = 0.5
        image_layer.fill((70, 70, 70))  # RGB
        divider(divider_y)
        divider_y += movingcar_speed
        mycar_x += dx
        movingcar_y += movingcar_speed  # this makes the car move in y-axis
        mycar(mycar_x, mycar_y)
        movingcar(movingcar_x, movingcar_y, type)
        score(count)
        if movingcar_y > 750:
            movingcar_y = -200
            movingcar_x = randrange(50, 950)
            movingcar_speed += 1  # difficulty increases
            count += 1  # score increases
            if randrange(0, 10) < 7:
                type = 1
            else:
                type = 2
        if divider_y > 0: divider_y = -800  # it runs from -800 to 0
        if mycar_x > 900 or mycar_x < 0:
            audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\crash.mpeg')
            audio.play(1)
            crash(count)
        if movingcar_y + 240 >= mycar_y:  # collision based on the length or the pixels of the cars
            if movingcar_x + 90 >= mycar_x >= movingcar_x - 110:
                audio.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\crash.mpeg')
                audio.play(1)
                crash(count)
        display_window.update()  # updates


pg.init()  # initiate PYGAME ...
clock = pg.time.Clock()
pg.mixer.init()  # music initiation
audio = pg.mixer.music
'''mixer.music for background music, at a time it loads only one music but by
mixer.Sound('') one can store multiple sound effects in various variables and
by var.play(),var.sleep(req time),var.stop()'''
# getting the background display,other layers of images
display_window = pg.display  # Like pg.time
image_layer = display_window.set_mode((1000, 750))  # (1000,750)is a tuple (width,height)
display_window.set_caption("MY  FIRST  GAME")
mycar_img = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\amblnc.png')
cabcar_img = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\taxi.png')  # type1
copcar_img = pg.image.load(r'C:\Users\USER9\PycharmProjects\pygame\Firstpygame_extras\cops.png')  # type2
game_loop()
