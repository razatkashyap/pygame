import pygame

pygame.init()

win = pygame.display.set_mode((507, 340))
pygame.display.set_caption("woo woo")
font = pygame.font.SysFont(None, 25)
image = pygame.image.load("pic.png")

run = True
win.blit(image, (0,0))
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            screen = font.render("You lose cannibal", True, (255,0,0))
            win.blit(screen, (200,200))


    pygame.display.update()
pygame.quit()
quit()