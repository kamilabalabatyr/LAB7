import pygame

pygame.init()

# Размер окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры мяча
BALL_RADIUS = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
BALL_SPEED = 20

# Основной цикл
running = True
while running:
    screen.fill(WHITE) 

    # Рисуем мяч
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip() 

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
                ball_x -= BALL_SPEED
            elif i.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
                ball_x += BALL_SPEED
            elif i.key == pygame.K_UP and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
                ball_y -= BALL_SPEED
            elif i.key == pygame.K_DOWN and ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
                ball_y += BALL_SPEED

pygame.quit()
