import pygame
import datetime

pygame.init()

width = 400
height = 400 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Часы с руками Микки")

# Загружаем изображения
right_hand = pygame.image.load('mickeyclock.jpeg') 
left_hand = pygame.image.load('mickeyclock.jpeg')  

# Функция для вычисления угла поворота руки
def getrotationangle(time, max):
    return -360 * (time / max)

# Главный цикл
running = True
while running:
    #текущее время
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    #углы для вращения рук
    right_angle = getrotationangle(minutes, 60)
    left_angle = getrotationangle(seconds, 60)

    # Вращаем руки
    right_hand_rotate = pygame.transform.rotate(right_hand, right_angle)
    left_hand_rotate = pygame.transform.rotate(left_hand, left_angle)

    #новые размеры после вращения
    right_rect = right_hand_rotate.get_rect(center=(width//2,height//2))
    left_rect = left_hand_rotate.get_rect(center=(width//2, height//2))

    # Заполняем экран белым цветом
    screen.fill((255, 255, 255))

    # Отображаем руки
    screen.blit(right_hand_rotate, right_rect)
    screen.blit(left_hand_rotate, left_rect)

    pygame.display.update()

    # Проверяем, не закрыто ли окно
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
