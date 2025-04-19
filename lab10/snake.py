import pygame
import random
import time
import psycopg2

# Подключение к базе
conn = psycopg2.connect(database="postgres", user="postgres", password="8888")
cur = conn.cursor()

# Создание таблицы user_score
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL,
    level INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# Pygame настройки
pygame.init()
WIDTH, HEIGHT = 600, 400
BLOCK = 20
FPS = 10

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(win, GREEN, (x, y, BLOCK, BLOCK))


def draw_score(score):
    text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(text, [10, 10])


def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    speed = FPS
    level = 1

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
    food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

    # Получение имени пользователя
    username = input("Enter your username: ").strip()

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT: dx, dy = BLOCK, 0
                elif event.key == pygame.K_UP: dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN: dx, dy = 0, BLOCK

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break

        snake.append((x, y))
        if len(snake) > length:
            del snake[0]

        if (x, y) in snake[:-1]:
            break

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
            food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)
            length += 1
            if length % 5 == 0:
                speed += 2
                level += 1

        win.fill(BLACK)
        pygame.draw.rect(win, RED, (food_x, food_y, BLOCK, BLOCK))
        draw_snake(snake)
        draw_score(length - 1)
        pygame.display.update()

        clock.tick(speed)

    # Сохраняем результат
    cur.execute("""
        INSERT INTO user_score (username, score, level) 
        VALUES (%s, %s, %s)
    """, (username, length - 1, level))
    conn.commit()

    print(f"Game over. Score saved for {username}.")

    time.sleep(2)
    pygame.quit()


game_loop()
cur.close()
conn.close()
