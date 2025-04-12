#создай игру "Лабиринт"!
from pygame import*
class GameSprite(sprite.Sprite):
    #iwehfei
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win__width-80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heigt -80:
            self. rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <=470:
            self.direction = 'right'
        if self.rect.x >=win__width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win__width = 700 #ширина окна
win_heigt = 500 #высота
#созание окна
window = display.set_mode((win__width, win_heigt))
display.set_caption('Maze')
#Фон
background = transform.scale(image.load('background.jpg'), (win__width, win_heigt))
#Персонажи игр
player =Player('hero.png', 5, win_heigt - 80, 4)
monster = Enemy('cyborg.png', win__width - 80, 200, 2)
final = GameSprite('treasure.png', win__width - 120, win_heigt-80, 0)
#создание стен
w1 = Wall(200, 200, 200, 100, 20, 450, 10)
w2 = Wall(200, 200, 200, 100, 50, 350, 10)
w3 = Wall(200, 200, 200, 100, 10, 10, 380)
#Игровой цикл
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (0, 255, 0))
lose = font.render('YOU LOSE!', True, (255, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

#Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
    #проигрыш
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    #победа
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)
