from pygame import *
from random import randint
window = display.set_mode((700, 500))   
display.set_caption("Пинг понг")   
background = transform.scale(image.load("bakcground.jpg"), (700, 500))   
   
class GameSprite(sprite.Sprite):   
    def __init__(self, player_image, player_x, player_y, player_speed):      
        self.player_image = transform.scale(image.load(player_image), (45, 100))   
        self.speed = player_speed   
        self.rect = self.player_image.get_rect()   
        self.rect.x = player_x   
        self.rect.y = player_y  
    def reset(self):   
        window.blit(self.player_image, (self.rect.x,self.rect.y))   
          
class Ball(sprite.Sprite):  
    def __init__(self, ball_image, ball_x, ball_y, ball_speed_y, ball_speed_x):
        self.ball_image = transform.scale(image.load(ball_image), (50, 50))
        self.rect = self. ball_image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y
    def reset(self):
        window.blit(self.ball_image, (self.rect.x,self.rect.y))  
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 450: 
            self.rect.y += self.speed 

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 450: 
            self.rect.y += self.speed 

class Movement(Ball):
    def update(self):
        if finish != True:
            ball.rect.x += self.speed_x
            ball.rect.y += self.speed_y
        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            self.speed_y *= -1


player = Player('hero.png', 0, 0, 10)
player1 = Player1('hero.png', 650, 0, 10)
ball = Movement('ball.png', 350, randint(0, 500), 3, 3)

game = True 
finish = False   
clock = time.Clock()   
while game: 
    for e in event.get():   
        if e.type == QUIT:   
            game = False 
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        player1.update()
        player.reset()
        player1.reset()
        ball.reset()
        ball.update()
    if finish != False:
        
    display.update()   
    clock.tick(60)