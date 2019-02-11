import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Yolo")

x = 250
y = 250
width = 10
height = 10
run = True
vel = 5

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 500:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel:
        x += vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
quit()