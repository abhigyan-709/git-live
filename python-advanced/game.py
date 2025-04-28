import pygame
import math
import sys

try:
    # Initialize Pygame
    pygame.init()
    print("Pygame initialized successfully")

    # Set up the display
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball in Circle")

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Circle properties
    CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
    CIRCLE_RADIUS = 200

    # Ball properties
    ball_radius = 20
    ball_x = CIRCLE_CENTER[0]
    ball_y = CIRCLE_CENTER[1]
    ball_speed = 5

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        new_x = ball_x
        new_y = ball_y
        
        if keys[pygame.K_LEFT]:
            new_x -= ball_speed
        if keys[pygame.K_RIGHT]:
            new_x += ball_speed
        if keys[pygame.K_UP]:
            new_y -= ball_speed
        if keys[pygame.K_DOWN]:
            new_y += ball_speed

        distance = math.sqrt((new_x - CIRCLE_CENTER[0])**2 + (new_y - CIRCLE_CENTER[1])**2)
        
        if distance + ball_radius >= CIRCLE_RADIUS:
            ball_radius *= 2
            if distance > 0:
                scale = (CIRCLE_RADIUS - ball_radius) / distance
                new_x = CIRCLE_CENTER[0] + (new_x - CIRCLE_CENTER[0]) * scale
                new_y = CIRCLE_CENTER[1] + (new_y - CIRCLE_CENTER[1]) * scale
        else:
            ball_x = new_x
            ball_y = new_y

        screen.fill(WHITE)
        pygame.draw.circle(screen, BLACK, CIRCLE_CENTER, CIRCLE_RADIUS, 2)
        pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
        
        pygame.display.flip()
        clock.tick(60)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    pygame.quit()
    sys.exit()