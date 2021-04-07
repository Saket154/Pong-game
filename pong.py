import pygame, sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Pong')

ball = pygame.Rect(450-15, 300-15,30,30)

color = (200,200,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.ellipse(screen, color, ball)

    #updating the window
    pygame.display.flip()
    clock.tick(60)