import pygame 
#seth window
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test")
#load images 
walkRight = [pygame.image.load('sprite_sheet/r1.png'), pygame.image.load('sprite_sheet/r2.png'), pygame.image.load('sprite_sheet/r3.png'), pygame.image.load(
    'sprite_sheet/r4.png'), pygame.image.load('sprite_sheet/r5.png'), pygame.image.load('sprite_sheet/r5.png'), pygame.image.load('sprite_sheet/r5.png'), pygame.image.load('sprite_sheet/r5.png'), pygame.image.load('sprite_sheet/r5.png')]
walkLeft = [pygame.image.load('sprite_sheet/l1.png'), pygame.image.load('sprite_sheet/l2.png'), pygame.image.load('sprite_sheet/l3.png'), pygame.image.load(
    'sprite_sheet/l4.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png'), pygame.image.load('sprite_sheet/l5.png')]
bg = pygame.image.load('sprite_sheet/bk.png')
char = pygame.image.load('sprite_sheet/stand.png')
#set clock speed
clock = pygame.time.Clock()
#set player attr
x = 50
y = 90
width = 40
height = 40
vel = 5

#Pulos
isJump = False
jumpCount = 10

left = False
right = False
WalkCount = 0

def redrawGameWindow():
    global WalkCount
    win.blit(bg, (0,0))
    #upload player to the screen
    if WalkCount + 1 >= 27:
        WalkCount = 0
    
    if left:
        win.blit(walkLeft[WalkCount//3],(x,y))
        WalkCount += 1 
    elif right:
         win.blit(walkRight[WalkCount//3], (x, y))
         WalkCount += 1 
    else:
        win.blit(char, (x,y))
    pygame.display.update()
#Main-loop
st = True
while st:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          st =  False
    #summom key move 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        WalkCount = 0
    # Se isJump não é usado?
    if not (isJump):   
        # Então se is Jump não for usado (o que sempre vai acontecer nesse ponto)
        if keys[pygame.K_SPACE]:
        # O booleano fica ativado
            isJump = True
            right = False
            left = False
            WalkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10  
    redrawGameWindow()

pygame.quit()
