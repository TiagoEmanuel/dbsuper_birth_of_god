import pygame
from pygame import * 
mixer.init()
mixer.music.load('music/single.ogg')
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(3)
    break
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Test") 
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

def redrawGameWindow():
    ch.WalkCount
    win.blit(bg, (0,0))
    if ch.WalkCount + 1 >= 27:
        ch.WalkCount = 0
    if ch.left:
        win.blit(walkLeft[ch.WalkCount//3],(ch.x,ch.y))
        ch.WalkCount += 1 
    elif ch.right:
         win.blit(walkRight[ch.WalkCount//3], (ch.x,ch.y))
         ch.WalkCount += 1 
    elif ch.up:
         win.blit(jump[ch.WalkCount//2], (ch.x,ch.y))
         ch.WalkCount += 1
    else:
        win.blit(char, (ch.x,ch.y))
    pygame.display.update()

ch = Player(300,610,64,64)

st = True

while st:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          st =  False
    #summom key move 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        ch.x -= ch.vel
        ch.left = True
        ch.right = False
        ch.up = False
    elif keys[pygame.K_RIGHT] and ch.x < 1000 - ch.width - ch.vel:
        ch.x += ch.vel
        ch.left = False
        ch.right = True
        ch.up = False 
    else:
        ch.left = False
        ch.right = False
        ch.WalkCount = 0
    # Se isJump não é usado?
    if not (ch.isJump):   
        # Então se is Jump não for usado (o que sempre vai acontecer nesse ponto)
        if keys[pygame.K_SPACE]:
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
            ch.y -= (ch.jumpCount **2) * 0.5 * neg
            ch.jumpCount -= 1
        else:
            ch.isJump = False
            ch.jumpCount = 10  
    redrawGameWindow()

pygame.quit()
