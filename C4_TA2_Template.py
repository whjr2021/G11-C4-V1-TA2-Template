# Import pygame library
import pygame
pygame.init() 
# Create a game screen and set its title
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Breakout Game")
# Define the RGB color combinations of rectangle objects
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
# Create a variable "RED" and assign RGB color combination of orange color to it.
# (255,0,0) represents red color.


# Create a paddle and a ball rectangle objects
paddle = pygame.Rect(300,500,60,10)
ball = pygame.Rect(200,250,10,10)
# Define variables to track ball and paddle movement
ballx = -1
bally = -1
paddlex = 2
# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False  
    screen.fill(DARKBLUE)
    # Check for user input to move the paddle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=paddlex
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=paddlex
           
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    # Update x and y position of the ball on screen 
    ball.x = ball.x + ballx
    ball.y = ball.y + bally
    # Limiting ball movement on screen along x-axis
    if ball.x >= 590:
      ballx = -ballx
    if ball.x <= 10:
      ballx = -ballx
    # Limiting ball movement on screen along y-axis
    if ball.y >= 590:
      bally = -bally
    if ball.y <= 10:
      bally = -bally
    pygame.draw.rect(screen,WHITE ,ball)
    # Check for paddle and ball collision and change the ball direction if they collided
    if paddle.collidepoint(ball.x, ball.y):
        bally = -bally
    # Create and draw 6 red bricks on screen 
    
    
    
    pygame.time.wait(8)
    # Update the contents of entire display
    pygame.display.flip()
# Quit the game  
pygame.quit()