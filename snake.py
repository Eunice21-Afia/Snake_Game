import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen size
width = 600
height = 400

# Snake settings
snake_block = 10
snake_speed = 15

# Set up the game window
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set the clock for controlling the snake's speed
clock = pygame.time.Clock()

# Fonts for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def show_score(score):
    value = score_font.render("Score: " + str(score), True, BLUE)
    display.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def game_loop():
    # Game over conditions
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Direction change variables
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Generate initial food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0

    # Main game loop
    while not game_over:

        while game_close:
            display.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            show_score(score)
            pygame.display.update()

            # Event handling for game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling user input for snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # If the snake hits the boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Updating the snake's position
        x += x_change
        y += y_change
        display.fill(BLACK)

        # Draw the food
        pygame.draw.rect(display, RED, [food_x, food_y, snake_block, snake_block])

        # Update the snake's body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        snake(snake_block, snake_list)
        show_score(score)

        pygame.display.update()

        # If the snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()

# Start the game
game_loop()
