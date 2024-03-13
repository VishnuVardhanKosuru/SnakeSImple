import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display width and height
display_width = 800
display_height = 600

# Set size of snake blocks and speed
block_size = 20
snake_speed = 15

# Create the display
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # Set initial position of snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Set initial movement direction
    x1_change = 0
    y1_change = 0

    # Define initial length of snake
    snake_list = []
    length_of_snake = 1

    # Randomly place food on screen
    foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])

        # Draw the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        for segment in snake_list:
            pygame.draw.rect(dis, black, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # If snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
