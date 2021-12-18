import pygame
import keyboard

pygame.init()

W, H = 800, 800
WIN = pygame.display.set_mode((W, H))
BG_COLOR = (0, 0, 0)


class WASD:
    def __init__(self, button):
        self.button = button
        self.value = 0

    def pressed(self):
        if keyboard.is_pressed(self.button):
            self.value = 1
        else:
            self.value = 0

up = WASD("w")
down = WASD("s")
left = WASD("a")
right = WASD("d")

def keyboardDetection():
    up.pressed(), down.pressed(), left.pressed(), right.pressed()


class Player:
    speed = 500
    x = 10
    y = 10
    W = 100
    H = 100

    @classmethod
    def Move(cls, y, x, delta_time):
        cls.y += y * cls.speed * delta_time
        cls.x += x * cls.speed * delta_time


def render():
    WIN.fill(BG_COLOR)
    pygame.draw.rect(WIN, (255, 0, 0), (int(Player.x), int(Player.y), Player.W, Player.H))
    pygame.display.update()

    
ticks_last_frame = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t = pygame.time.get_ticks()
    delta_time = (t - ticks_last_frame) / 1000
    ticks_last_frame = t

    keyboardDetection()
    yvalue = down.value - up.value
    xvalue = right.value - left.value
    if xvalue != 0 and yvalue != 0:
        xvalue = xvalue / 1.414
        yvalue = yvalue / 1.414
    Player.Move(yvalue, xvalue, delta_time)

    render()
