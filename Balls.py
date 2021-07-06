import pygame as pg
from random import randint

RED = [255, 0, 20]
GREEN = [0, 225, 50]
BLUE = [0, 50, 255]
YELLOW = [255, 225, 0]
WHITE = [200, 200, 200]
num = 30


def message(gravity, damping):
    if gravity:
        font = pg.font.SysFont(None, 60)
        txt_surface = font.render('GRAVITY', True, (100, 100, 100))
        txt_box = txt_surface.get_rect()
        txt_box.center = (300, 25)
        image_layer.blit(txt_surface, txt_box)  # renders the image
    if damping:
        font = pg.font.SysFont(None, 60)
        txt_surface = font.render('DAMPING', True, (100, 100, 100))
        txt_box = txt_surface.get_rect()
        txt_box.center = (550, 25)
        image_layer.blit(txt_surface, txt_box)  # renders the image


class ball(object):
    def __init__(self, color, x, y, x_change, y_change):
        self.color = color
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change

    def display(self):
        rad = 10
        pg.draw.circle(image_layer, self.color, (self.x, self.y), rad)  # pg.draw.arc() for hollow ones

    def move(self, gravity, damping):
        if gravity and 50 < self.y < 530:
            self.y_change += 1
        if self.x < 65:
            if damping:
                if self.x_change != 0:
                    self.x_change = int(abs(self.x_change) / 1.2)
                if -3 <= self.x_change <= 3:
                    self.x_change = int(abs(self.x_change) / 2.5)
                if -1 <= self.x_change <= 1:
                    self.x_change = 0
            else:
                self.x_change = abs(self.x_change)
            self.color = YELLOW
        elif self.x > 735:
            if damping:
                if self.x_change != 0:
                    self.x_change = -int(abs(self.x_change) / 1.2)
                if -3 <= self.x_change <= 3:
                    self.x_change = -int(abs(self.x_change) / 2.5)
                if -1 <= self.x_change <= 1:
                    self.x_change = 0
            else:
                self.x_change = -abs(self.x_change)
            self.color = GREEN
        if self.y < 65:
            if gravity and 50 < self.y < 530:
                self.y_change += 10
            elif damping:
                if self.y_change != 0:
                    self.y_change = int(abs(self.y_change) / 1.2)
                if -3 <= self.y_change <= 3:
                    self.y_change = int(abs(self.y_change) / 2.5)
                if -1 <= self.y_change <= 1:
                    self.y_change = 0
            else:
                self.y_change = abs(self.y_change)
            self.color = RED
        elif self.y > 535:
            if damping:
                if self.y_change != 0:
                    self.y_change = -int(abs(self.y_change) / 1.2)
                if -3 <= self.y_change <= 3:
                    self.y_change = -int(abs(self.y_change) / 2.5)
                if -1 <= self.y_change <= 1:
                    self.y_change = 0
            else:
                self.y_change = -abs(self.y_change)
            self.color = BLUE
        self.x += self.x_change
        self.y += self.y_change

    def is_collided(self, ball_set, i, gravity, damping):
        xi = self.x
        yi = self.y
        vxi = self.x_change
        vyi = self.y_change
        for j in range(num):
            if i == j:
                continue
            xj = ball_set[j].x
            yj = ball_set[j].y
            vxj = ball_set[j].x_change
            vyj = ball_set[j].y_change
            D = (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj)
            if D <= 150:
                if D < 100:
                    D = 100
                # self.color = WHITE
                # ball_set[j].color = WHITE
                factor = randint(5, 15) / 10
                self.y_change = vyj * ((yi - yj) * (yi - yj) / D) + vyi * ((xi - xj) * (xi - xj) / D) + (vxi - vxj) * (
                        abs((yi - yj) * (xi - xj)) / D)
                self.x_change = vxi * ((yi - yj) * (yi - yj) / D) + vxj * ((xi - xj) * (xi - xj) / D) + (vyj - vyi) * (
                        abs((yi - yj) * (xi - xj)) / D)
                if gravity:
                    if abs(vyi) > 5:
                        self.y_change = vyi
                    elif yi < 530:
                        self.y_change = 5
                    else:
                        self.y_change = -5
                    self.x_change = int(self.x_change)
                elif damping:
                    self.y_change = int(self.y_change / 1.1)
                    self.x_change = int(self.x_change / 1.1)
                else:
                    if 0 <= self.y_change < 3:
                        self.y_change = randint(3, 5)
                    elif -3 < self.y_change <= 0:
                        self.y_change = -randint(3, 5)
                    else:
                        self.y_change = int(self.y_change * factor)
                    if 0 <= self.x_change < 3:
                        self.x_change = randint(3, 5)
                    elif -3 < self.x_change <= 0:
                        self.x_change = -randint(3, 5)
                    else:
                        self.x_change = int(self.x_change * factor)


def game_loop():
    gravity = False
    damping = False
    ball_set = []
    for i in range(num):
        ball_set.append(ball(WHITE, randint(60, 740), randint(60, 540), randint(-10, 10), randint(-10, 10)))
    while True:
        for event in pg.event.get():  # section for movements
            if event.type == pg.QUIT:
                pg.quit()  # for system-exit
            if event.type == pg.KEYDOWN:  # detects key-pressing
                if event.key == pg.K_g:
                    if gravity:
                        gravity = False
                    else:
                        gravity = True
                if event.key == pg.K_d:
                    if damping:
                        damping = False
                    else:
                        damping = True
        image_layer.fill((50, 50, 50))
        pg.draw.line(image_layer, RED, (50, 50), (750, 50), 2)
        pg.draw.line(image_layer, GREEN, (750, 50), (750, 550), 2)
        pg.draw.line(image_layer, BLUE, (750, 550), (50, 550), 2)
        pg.draw.line(image_layer, YELLOW, (50, 550), (50, 50), 2)
        message(gravity, damping)
        for i in range(num):
            ball_set[i].move(gravity, damping)
            ball_set[i].is_collided(ball_set, i, gravity, damping)
            ball_set[i].display()
        clock.tick(60)
        display_window.update()  # updates to the screen


pg.init()  # initiate PYGAME ...
clock = pg.time.Clock()
display_window = pg.display  # getting the background display,other layers of images
image_layer = display_window.set_mode((800, 600))
display_window.set_caption("OOP EXAMPLE")
game_loop()
