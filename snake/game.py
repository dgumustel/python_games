# Imports
import pygame
import time
import random
import sys

snake_speed = 15
score = 0

# Window size
window_x = 720
window_y = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
# What's the purpose of this?

# Initializing pygame:
pygame.init()

# And game window
pygame.display.set_caption('Tutorial snake')
# This line displays the window: 
game_window = pygame.display.set_mode((window_x, window_y))

# Control the FPS:
fps = pygame.time.Clock()

# print('hello friend!')

# Set snake default pos
snake_position = [100, 50]

# Create snake body
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Default snake direction:
direction = 'RIGHT'
change_to = direction

# Starting fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True


def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)

    # Create text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # Create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # Set position of text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 2 seconds, quit the program
    time.sleep(2)

    pygame.quit()
    quit()

# Function for displaying score
def show_score(choice, color, font, size):
    # Font
    score_font = pygame.font.SysFont(font, size)

    # Create display surface object:
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # Displaying text
    game_window.blit(score_surface, score_rect)

# Main game loop
while True:
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         

        # Handling key events
        # for event in pygame.event.get():
        #     print(event)
        if event.type == pygame.KEYDOWN:
            # Uncomment for debugging
            # print(event.key)
            if event.key == pygame.K_UP:
                change_to = 'UP'
                # print('up arrow pressed')
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
                # print('down arrow pressed')
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
                # print('left arrow pressed')
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                # print('right arrow pressed')


    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Uncomment for debugging
    # print(direction)


    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Uncomment for debugging
    # print(snake_position)

    # Add snake head to body
    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        print('nom nom nom')
        score += 10
        fruit_spawn = False
    else:
        # Remove last block from snake with each frame to simulate movement
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10
        ]

    fruit_spawn = True
    game_window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10
        ))
        # print(pos)

    # Draw fruit
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10
    ))

    # Game over conditions
    # Touching screen edge
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Running into snake's body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # FPS / refresh rate
    fps.tick(snake_speed)

