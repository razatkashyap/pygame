import pygame
import random
import time
from threading import Thread

pygame.init()
font = pygame.font.SysFont(None, 25)
win = pygame.display.set_mode((600, 630))
pygame.display.set_caption("Snake class")



class Snake():
    count = 0
    def counter(self):
        for x in range(10):
            time.sleep(1)
            self.count += 1
            print(self.count)

    def main(self, snake_x = 400, snake_y = 500, snake_width = 10, snake_height = 10, apple_x = round(random.randrange(0, 600)/10.0)*10.0, apple_y = round(random.randrange(0, 630)/10.0)*10.0, apple_width = 10, apple_height = 10, vel = 10, set_x = 600, set_y = 630, black = (0,0,0), white = (255,255,255), red = (255,0,0), green = (0,255,0), blue = (0, 0, 255), hurdle = (80,50,120), hurdle_x = round(random.randrange(0, 600)/10.0)*10.0, hurdle_y = round(random.randrange(0, 630)/10.0)*10.0, hurdle_width = 10, hurdle_height = 10):
            run = True
            score = 0
            while run and self.count < 10:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP] and snake_y > vel + 10:
                    snake_y -= vel
                if keys[pygame.K_DOWN] and snake_y < set_y - (snake_height - 10) - vel:
                    snake_y += vel
                if keys[pygame.K_RIGHT] and snake_x < set_x - (snake_width - 10) - vel:
                    snake_x += vel
                if keys[pygame.K_LEFT] and snake_x > vel - 10:
                    snake_x -= vel

                if apple_x == snake_x and apple_y == snake_y:
                    apple_x = round(random.randrange(0, (set_x - 10)) / 10.0) * 10.0
                    apple_y = round(random.randrange(30, (set_y - 10)) / 10.0) * 10.0
                    hurdle_x = round(random.randrange(0, set_x) / 10.0) * 10.0
                    hurdle_y = round(random.randrange(30, set_y) / 10.0) * 10.0
                    snake_width += 10
                    score += 1

                if hurdle_x == snake_x and hurdle_y == snake_y:
                    outi = font.render("Game Over", True, red)
                    win.blit(outi, (270, 310))
                    pygame.display.update()
                    time.sleep(5)
                    run = False

                win.fill(white)
                pygame.draw.rect(win, black, (snake_x, snake_y, snake_width, snake_height))
                pygame.draw.rect(win, red, (apple_x, apple_y, apple_width, apple_height))
                pygame.draw.rect(win, hurdle, (hurdle_x, hurdle_y, hurdle_width, hurdle_height))
                screen = font.render("Score : " + str(score), True, green)
                win.blit(screen, (510, 0))
                message = font.render("Press q any time to quit!!", True, blue)
                win.blit(message, (170, 0))
                pygame.display.update()

snake = Snake()
Thread(target=snake.counter()).start()
Thread(target=snake.main()).start()



pygame.quit()
quit()