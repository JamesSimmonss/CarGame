import pygame
import random

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 10
SPEED = 20

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Define the Snake class
class Snake:
    def __init__(self):
        self.segments = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self):
        x, y = self.segments[0]
        if self.direction == 'up':
            y -= BLOCK_SIZE
        elif self.direction == 'down':
            y += BLOCK_SIZE
        elif self.direction == 'left':
            x -= BLOCK_SIZE
        elif self.direction == 'right':
            x += BLOCK_SIZE
        self.segments.insert(0, (x, y))
        self.segments.pop()

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, WHITE, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))


# Define the Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE), random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))


# Create the Snake and Food objects
snake = Snake()
food = Food()

# Game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'

    # Move the snake
    snake.move()

    # Check for collision with the food
    if snake.segments[0][0] == food.position[0] and snake.segments[0][1] == food.position[1]:
        snake.segments.append(snake.segments[-1])
        food = Food()

    # Check for collision with the wall or self
    if snake.segments[0][0] < 0 or snake.segments[0][0] >= SCREEN_WIDTH or snake.segments[0][1] < 0 or \
            snake.segments[0][1] >= SCREEN_HEIGHT:
        game_over = True
    for segment in snake.segments[1:]:
        if snake.segments[0] == segment:
            game_over = True

    # Draw the screen
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Limit the frame rate
    clock.tick(SPEED)

# Clean up
pygame.quit()