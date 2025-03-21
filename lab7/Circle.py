import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Круг")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
BALL_SPEED = 15

x, y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - BALL_RADIUS - BALL_SPEED >= 0:
        x -= BALL_SPEED
    if keys[pygame.K_RIGHT] and x + BALL_RADIUS + BALL_SPEED <= WIDTH:
        x += BALL_SPEED
    if keys[pygame.K_UP] and y - BALL_RADIUS - BALL_SPEED >= 0:
        y -= BALL_SPEED
    if keys[pygame.K_DOWN] and y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
        y += BALL_SPEED

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
