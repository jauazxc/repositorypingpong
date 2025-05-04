from pygame import *
from random import randint

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
        if keys_pressed[K_UP] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 485:
            self.rect.y += self.speed

a = randint(1, 2)

mixer.init()
mixer.music.load('dotamusic.mp3')
mixer.music.play


speed_x = 5
speed_y = 5

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
        if self.rect.x >= 700:
            score1 +=1
            self.rect.y = 218
            self.rect.x = 318 

score1 = 0
score2 = 0
    
def game_over():
    if score1 >= 11 and score1 - score2 == 2:
        window.blit(lose1, (200, 200))
        window.blit(win2, (200, 350))
    if score2 >= 11 and score2 - score1 == 2:
        window.blit(lose2, (200, 200))
        window.blit(win1, (200, 350))

window = display.set_mode((700, 500))
display.set_caption('qeqoqeq')
background = transform.scale(image.load('map.png'), (700, 500))

player = Player('doom.png', 15, 218, 15, 50, 100)
player2 = Player2('lion.png', 635, 217, 15, 50, 100)
ball = Ball('ball.png', 318, 218, 200, 40, 40)

font.init()
font1 = font.Font(None, 35)
win1 = font1.render('Player 1 win!', True, (255, 255, 255))
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
win2 = font1.render('Player 2 win!', True, (255, 255, 255))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))


game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0)) 
        score_1 = font1.render('Player 1 score:'+str(score1), 1, (255, 255, 255))
        score_2 = font1.render('Player 2 score:'+str(score2), 1, (255, 255, 255))
        window.blit(score_1, (15, 15))
        window.blit(score_2,(500, 15))
        player.update_l()
        player.reset()
        player2.update_r()
        player2.reset()
        ball.update()
        ball.reset()
        if sprite.collide_rect(ball, player):
            speed_x *= -1
        if sprite.collide_rect(ball, player2):
            speed_x *= -1
        game_over()

    display.update()
    clock.tick(60)
