from pygame import *
from random import randint

class GameSprite(sprite.Sprite): #Основной класс спрайта
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

class Ball(GameSprite):
    def update(self):
        if a == 1:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        if a == 2:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.rect.x <= 30:
            self.rect.x += self.speed
        if self.rect.x >= 30:
            self.rect.x -= self.speed
        if self.rect.y <= 15:
            self.rect.y += self.speed
        if self.rect.y >= 15:
            self.rect.y -= self.speed
    
    
window = display.set_mode((500, 700))
display.set_caption('qeqoqeq')
background = transform.scale(image.load('background.jpg'), (500, 700))

player = Player('square.png', 15, 218, 15, 15, 65)
player2 = Player2('square.png', 620, 217, 15, 15, 65)
ball = GameSprite('treasure.png', 318, 218, 20, 40, 40)

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish = false:
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
    
