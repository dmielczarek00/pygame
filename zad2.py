import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    pygame.draw.circle(win, "black", (200, 200), 100)
    pygame.draw.rect(win, "yellow", pygame.Rect(150, 150, 100, 100))

    pygame.display.update()