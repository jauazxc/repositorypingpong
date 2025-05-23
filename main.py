from pygame import *
from random import randint
from time import sleep

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 485:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y <= 485:
            self.rect.y += self.speed

a = randint(1, 2)

mixer.init()
mixer.music.load('dotamusic.ogg')
mixer.music.play

speed_x = 7
speed_y = 7

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y, score1, score2
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y >= 480 or self.rect.y <= 20:
            speed_y *= -1
        if self.rect.x <= 0:
            score2 += 1
            self.rect.y = 218
            self.rect.x = 318
            sleep(1)
        if self.rect.x >= 660:
            score1 +=1
            self.rect.y = 218
            self.rect.x = 318 
            sleep(1)

score1 = 0
score2 = 0

def draw_pause():
    zxcpausss = font2.render('GAME PAUSED', True, (255, 0, 0))
    window.blit(zxcpausss,(100, 250))

pause_time = 0

def game_over():
    if score1 >= 11 and score1 - score2 >= 2:
        window.blit(lose2, (200, 200))
        window.blit(win1, (200, 350))
    if score2 >= 11 and score2 - score1 >= 2:
        window.blit(lose1, (200, 200))
        window.blit(win2, (200, 350))

window = display.set_mode((700, 500))
display.set_caption('qeqoqeq')
background = transform.scale(image.load('oboi CR.jpg'), (700, 500))

cooldown = 0

player = Player('doom.png', 15, 218, 15, 50, 100)
player2 = Player2('lion.png', 635, 217, 15, 50, 100)
ball = Ball('ball.png', 318, 218, 200, 40, 40)

font.init()
font1 = font.Font(None, 35)
font2 = font.Font(None, 96)
win1 = font1.render('Player 1 win!', True, (255, 255, 255))
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
win2 = font1.render('Player 2 win!', True, (255, 255, 255))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))
n1 = font1.render('UP - W, DOWN - S', True, (255, 0, 255))
n2 = font1.render('UP - O, DOWN - L', True, (255, 255, 255))
zxcpause = font1.render('PAUSE - ESC (5s)', True, (255, 255, 255))

game = True
finish = False
pause = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0)) 
    score_1 = font1.render('Player 1 score:'+str(score1), 1, (255, 0, 255))
    score_2 = font1.render('Player 2 score:'+str(score2), 1, (255, 255, 255))
    window.blit(score_1, (15, 15))
    window.blit(score_2,(480, 15))
    window.blit(n1,(15, 40))
    window.blit(n2,(480, 40))
    window.blit(zxcpause,(250, 20))
    player.reset()
    player2.reset()
    ball.reset()

    keys_pressed = key.get_pressed()
    if keys_pressed[K_ESCAPE]:
        pause = True
        
    if finish == False and pause == False:
        player.update_l()
        player2.update_r()
        ball.update()
        if sprite.collide_rect(ball, player) and cooldown > 9:
            speed_x *= -1
            cooldown = 0
        if sprite.collide_rect(ball, player2) and cooldown > 9:
            speed_x *= -1
            cooldown = 0
        game_over()
        cooldown += 1
    if pause == True and pause_time > 300:
        pause = False
        pause_time = 0
    if pause == True and pause <= 300:
        draw_pause()
        pause_time += 1
    display.update()
    clock.tick(60)
