import pygame
from pygame import *

mixer.init()
mixer.music.load('music/single.ogg')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(3)
    break

win = pygame.display.set_mode((1000,800))

pygame.display.set_caption("DRAGON BALL SUPER: BIRTH OF GOD ALPHA 0.0.2")

walkRight = [pygame.image.load('sprite_sheet/r1.png'), pygame.image.load('sprite_sheet/r2.png'), pygame.image.load('sprite_sheet/r3.png'), pygame.image.load(
    'sprite_sheet/r4.png'), pygame.image.load('sprite_sheet/r4.png'), pygame.image.load('sprite_sheet/r4.png'), pygame.image.load('sprite_sheet/r4.png'), pygame.image.load('sprite_sheet/r5.png'), pygame.image.load('sprite_sheet/r5.png')]

walkLeft = [pygame.image.load('sprite_sheet/l1.png'), pygame.image.load('sprite_sheet/l2.png'), pygame.image.load('sprite_sheet/l3.png'), pygame.image.load(
    'sprite_sheet/l4.png'), pygame.image.load('sprite_sheet/l4.png'), pygame.image.load('sprite_sheet/l4.png'), pygame.image.load('sprite_sheet/l4.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png')]

jump = [pygame.image.load('sprite_sheet/j1.png'), pygame.image.load(
    'sprite_sheet/j2.png'), pygame.image.load('sprite_sheet/j3.png'), pygame.image.load('sprite_sheet/j4.png'), pygame.image.load('sprite_sheet/j5.png'), pygame.image.load('sprite_sheet/j6.png'),]

bg = pygame.image.load('sprite_sheet/bk.png')

char = pygame.image.load('sprite_sheet/stand.png')

clock = pygame.time.Clock()

class Player(object):

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.up = False
        self.WalkCount = 0
        self.standing = True
        self.hitbox = (self.x, self.y, 28, 60)
    def draw(self,win):

        if self.WalkCount + 1 >= 27:
            self.WalkCount = 0
        if not (self.standing):

            if self.left:
                win.blit(walkLeft[self.WalkCount//3], (self.x,self.y))
                self.WalkCount += 1

            elif self.right:
                win.blit(walkRight[self.WalkCount//3], (self.x, self.y))
                self.WalkCount += 1

        elif self.up:
            win.blit(jump[self.WalkCount//2], (self.x, self.y))
            self.WalkCount += 1

        else:
           # win.blit(char, (self.x, self.y))
           if self.right:
                win.blit(walkRight[0], (self.x, self.y))
           else:
                win.blit(walkLeft[0], (self.x, self.y))
           self.hitbox = (self.x, self.y, 28, 60)
           pygame.draw.rect(win, (255,0,0), self.hitbox,2)

class Special():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class Enemies(object):
    walkLeft = [pygame.image.load('enemies/r1.png'), pygame.image.load('enemies/r2.png'), pygame.image.load('enemies/r3.png'), pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png')]
    walkRight =  [pygame.image.load('enemies/l1.png'), pygame.image.load('enemies/l2.png'), pygame.image.load('enemies/l3.png'), pygame.image.load('enemies/l4.png'), pygame.image.load('enemies/l4.png'), pygame.image.load('enemies/l4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png'),pygame.image.load('enemies/r4.png')]

    def __init__(self,x,y,width,height,end):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, 28, 60)

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkLeft[self.walkCount //9], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //9], (self.x,self.y))
                self.walkCount += 1
            self.hitbox = (self.x, self.y, 28, 60)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        pass

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        pass

def redrawGameWindow():
    #global WalkCount
    win.blit(bg, (0, 0))
    ch.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

ch = Player(300,610,64,64)
enemy = Enemies(100,410,64,64,450)
st = True
bullets = []
while st:
        clock.tick(27)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                st = False
        for bullet in bullets:
            if bullet.x < 1000 and bullet.x > 0:
                bullet.x += ch.vel
            else:
                bullets.pop(bullets.index(bullet))
        #summom key move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if ch.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append( Special( (ch.x+ch.width // 2),round(ch.y+ch.height//2),6, (0,0,0),facing ) )
        if keys[pygame.K_LEFT] and ch.x > ch.vel:
            ch.x -= ch.vel
            ch.left = True
            ch.right = False
            ch.up = False
            ch.standing = False
        elif keys[pygame.K_RIGHT] and ch.x < 1000 - ch.width - ch.vel:
            ch.x += ch.vel
            ch.left = False
            ch.right = True
            ch.up = False
            ch.standing = False
        else:
            ch.standing = True
            ch.left = False
            ch.right = False
            ch.WalkCount = 0

        # Se isJump não é usado?
        if not (ch.isJump):
            # Então se is Jump não for usado (o que sempre vai acontecer nesse ponto)

            if keys[pygame.K_UP]:
                # O booleano fica ativado
                ch.isJump = True
                ch.up = True
                ch.right = False
                ch.left = False
                ch.WalkCount = 0

        else:
            if ch.jumpCount >= -10:
                neg = 1

                if ch.jumpCount < 0:
                    neg = -1
                ch.y -= (ch.jumpCount ** 2) * 0.5 * neg
                ch.jumpCount -= 1

            else:
                ch.isJump = False
                ch.jumpCount = 10


        redrawGameWindow()

pygame.quit()
