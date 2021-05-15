import pygame, sys, random

#functions
def collisions():
    global ball_speed_x, ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y


    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= 900:
        ball_restart()


    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (450 - 15, 300 - 15)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def player_animation():
    player.y += player_speed 

    if player.top <= 0:
        player.top = 0

    if player.bottom >= 600:
        player.bottom = 600

def opponent_AI():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= 600:
        opponent.bottom = 600





#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Pong')

ball = pygame.Rect(450-15, 300-15,20,20)
player = pygame.Rect(900 - 20, 300 - 50, 10, 100)
opponent = pygame.Rect(10, 300 - 50, 10, 100)

color = (200,200,200)
bg_color = pygame.Color('white')

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    opponent_AI()
    player_animation()
    collisions()
    

    
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.rect(screen, color, player)
    pygame.draw.rect(screen, color, opponent)
    pygame.draw.aaline(screen, color, (450, 0), (450, 600))


 
    #updating the window
    pygame.display.flip()
    clock.tick(60)