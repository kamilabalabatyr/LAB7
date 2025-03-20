import pygame
import os

pygame.init()

# Создаем окно
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Инициализация микшера для воспроизведения музыки
pygame.mixer.init()

MUSIC_FOLDER = "music/"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]

# Проверка наличия музыки
if not songs:
    print("Нет MP3 файлов в папке 'music'!")
    pygame.quit()
    exit()

current_song = 0

# Функция загрузки и воспроизведения песни
def play_song():
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song]))
    pygame.mixer.music.play()
    print(f"Играет: {songs[current_song]}")

# Запускаем первую песню
play_song()

# Основной цикл
running = True
paused = False

while running:
    screen.fill((135, 206, 235))  # Фон небесно голубой
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза/Воспроизведение
                if paused:
                    pygame.mixer.music.unpause()
                    print("Продолжение воспроизведения")
                else:
                    pygame.mixer.music.pause()
                    print("Пауза")
                paused = not paused

            elif event.key == pygame.K_s:  # Остановка музыки
                pygame.mixer.music.stop()
                print("Музыка остановлена")
                paused = False

            elif event.key == pygame.K_RIGHT:  # Следующая песня
                current_song = (current_song + 1) % len(songs)
                play_song()

            elif event.key == pygame.K_LEFT:  # Предыдущая песня
                current_song = (current_song - 1) % len(songs)
                play_song()

pygame.quit()
