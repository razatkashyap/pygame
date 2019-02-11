import pygame

pygame.init()

pygame.display.set_caption("Move Circle")
win = pygame.display.set_mode((500, 500))


x = 50
y = 50
width = 50
height = 50
run = True
isJump = False
jumpCount = 10

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        isJump = True

    if isJump:
        if jumpCount >= 10:
            neg = 1
            if jumpCount < 0:
                neg = -1
        y -= (jumpCount ** 2) * 0.5 * neg
        jumpCount -= 1
    else:
        isJump = False
        jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,255), (x,y,width,height))
    pygame.display.update()
pygame.quit()