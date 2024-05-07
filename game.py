import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_size = 10
snake_speed = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
food_pos = [random.randrange(1, WIDTH // snake_size) * snake_size, random.randrange(1, HEIGHT // snake_size) * snake_size]
food_spawn = True
enemy_size = 10
enemy_speed = 5
enemies = [[random.randrange(1, WIDTH // enemy_size) * enemy_size, random.randrange(1, HEIGHT // enemy_size) * enemy_size]]
clock = pygame.time.Clock()
game_over = False
font = pygame.font.SysFont(None, 35)
score = 0
target_score = 5
def show_message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH // 6, HEIGHT // 3])
def show_score():
    score_text = font.render(f"PONTUAÇÃO: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], snake_size, snake_size))
def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, RED, pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size))
def move_enemies(enemies, snake_pos):
    for enemy in enemies:
        if enemy[0] < snake_pos[0]:
            enemy[0] += enemy_speed
        elif enemy[0] > snake_pos[0]:
            enemy[0] -= enemy_speed
        
        if enemy[1] < snake_pos[1]:
            enemy[1] += enemy_speed
        elif enemy[1] > snake_pos[1]:
            enemy[1] -= enemy_speed
def generate_food_position():
    pos = [random.randrange(1, WIDTH // snake_size) * snake_size, random.randrange(1, HEIGHT // snake_size) * snake_size]
    while pos in snake_body or pos in enemies:
        pos = [random.randrange(1, WIDTH // snake_size) * snake_size, random.randrange(1, HEIGHT // snake_size) * snake_size]
    return pos
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
    if snake_direction == 'UP':
        snake_pos[1] -= snake_speed
    elif snake_direction == 'DOWN':
        snake_pos[1] += snake_speed
    elif snake_direction == 'LEFT':
        snake_pos[0] -= snake_speed
    elif snake_direction == 'RIGHT':
        snake_pos[0] += snake_speed
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
        score += 1
    else:
        snake_body.pop()
    if not food_spawn:
        food_pos = generate_food_position()
        food_spawn = True
    move_enemies(enemies, snake_pos)
    for enemy in enemies:
        if snake_pos == enemy:
            game_over = True
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        game_over = True
    if snake_pos in snake_body[1:]:
        game_over = True
    screen.fill(BLACK)
    draw_snake(snake_body)
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))
    draw_enemies(enemies)
    show_score()
    if score >= target_score:
        game_over = True
        show_message("VOCÊ VENCEU!", GREEN)
        pygame.display.update()
        pygame.time.wait(2000)
        break
    pygame.display.update()
    clock.tick(15)
if game_over:
    screen.fill(BLACK)
    show_message("GAME OVER!", RED)
    pygame.display.update()
    pygame.time.wait(2000)
pygame.quit()