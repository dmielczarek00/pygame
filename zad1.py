import pygame
import math

pygame.init()
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)


def shear(surface, points, shear_factor, offset_x, offset_y):
    transformed_points = []
    for x, y in points:
        new_x = x + y * shear_factor
        transformed_points.append((new_x + offset_x, y + offset_y))
        
    pygame.draw.polygon(surface, BIALY, transformed_points, 0)

def pos_1(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    pygame.draw.polygon(surface, BIALY, points, 0)

def pos_2(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    pos_1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 45)
    scaled = pygame.transform.scale(surface_new, (int(surface_new.get_width() * 1.2), int(surface_new.get_height() * 1.2)))

    offset_x = (surface.get_width() - scaled.get_width()) // 2
    offset_y = (surface.get_height() - scaled.get_height()) // 2

    surface.blit(scaled, (offset_x, offset_y))

def pos_3(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    pos_1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 180)
    scaled = pygame.transform.smoothscale(surface_new, (surface_new.get_width(), int(surface_new.get_height() * 1.2)))

    offset_x = (surface.get_width() - scaled.get_width()) // 2
    offset_y = (surface.get_height() - scaled.get_height()) // 2

    surface.blit(scaled, (offset_x, offset_y))

def pos_4(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    shear(surface, points, 0.5, -150, 0)

def pos_5(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    pos_1(surface, x, y, radius)
    scaled = pygame.transform.smoothscale(surface, (int(surface.get_width() * 1.2), int(surface.get_height() * 0.2)))
    surface.fill(ZOLTY)

    offset_x = (surface.get_width() - scaled.get_width()) // 2
    offset_y = (surface.get_height() - scaled.get_height()) // 2

    surface.blit(scaled, (offset_x, offset_y - 200))

def pos_6(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    shear(surface, points, 0.2, -150, 0)
    rotated = pygame.transform.rotate(surface, 90)
    surface.fill(ZOLTY)

    offset_x = (surface.get_width() - rotated.get_width()) // 2
    offset_y = (surface.get_height() - rotated.get_height()) // 2

    surface.blit(rotated, (offset_x, offset_y))

def pos_7(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    pos_1(surface, x, y, radius)
    surface_new = pygame.transform.rotate(surface, 180)
    scaled = pygame.transform.smoothscale(surface_new, (surface_new.get_width(), int(surface_new.get_height() * 1.2)))
    flipped = pygame.transform.flip(scaled, False, True)

    offset_x = (surface.get_width() - flipped.get_width()) // 2
    offset_y = (surface.get_height() - flipped.get_height()) // 2

    surface.blit(flipped, (offset_x, offset_y))

def pos_8(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    pos_1(surface, x, y, radius)
    scaled = pygame.transform.smoothscale(surface, (int(surface.get_width() * 1.2), int(surface.get_height() * 0.2)))
    surface_new = pygame.transform.rotate(scaled, -30)
    surface.fill(ZOLTY)

    offset_x = (surface.get_width() - surface_new.get_width()) // 2
    offset_y = (surface.get_height() - surface_new.get_height()) // 2

    surface.blit(surface_new, (offset_x - 50, offset_y + 100))

def pos_9(surface, x, y, radius):
    window.fill(ZOLTY)
    n = 11
    points = []
    for i in range(n):
        angle = math.radians(360 / n * i)
        point = (x + radius * math.cos(angle), y + radius * math.sin(angle))
        points.append(point)
    shear(surface, points, 0.5, -150, 0)
    rotated = pygame.transform.rotate(surface, 180)
    surface.fill(ZOLTY)

    offset_x = (surface.get_width() - rotated.get_width()) // 2
    offset_y = (surface.get_height() - rotated.get_height()) // 2

    surface.blit(rotated, (offset_x + 100, offset_y))


# Współrzędne środka i promień
center_x, center_y = width // 2, height // 2
radius = 150

pos_1(window, center_x, center_y, radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        pos_1(window, center_x, center_y, radius)
    if keys[pygame.K_2]:
        pos_2(window, center_x, center_y, radius)
    if keys[pygame.K_3]:
        pos_3(window, center_x, center_y, radius)
    if keys[pygame.K_4]:
        pos_4(window, center_x, center_y, radius)
    if keys[pygame.K_5]:
        pos_5(window, center_x, center_y, radius)
    if keys[pygame.K_6]:
        pos_6(window, center_x, center_y, radius)
    if keys[pygame.K_7]:
        pos_7(window, center_x, center_y, radius)
    if keys[pygame.K_8]:
        pos_8(window, center_x, center_y, radius)
    if keys[pygame.K_9]:
        pos_9(window, center_x, center_y, radius)

    pygame.display.update()

pygame.quit()
