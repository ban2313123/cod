import pygame
import random
import sys
import time

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Лови числа!")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont("Arial", 36)

# Параметры игрока
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Параметры числа
number_width = 40
number_height = 40
falling_numbers = []  # Список падающих чисел
number_speed = 5

# Счёт
score = 0

# Число для поимки
target_number = random.randint(1, 9)

# Настройки
show_fps = True
color_change_enabled = True

# Таймер для генерации новых чисел
NEW_NUMBER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(NEW_NUMBER_EVENT, 1000)  # Новое число каждую секунду

# МЕМЫ (добавлены дополнительные мемы)
memes = [
    "Ошибка: Загрузка мозга не удалась.",
    "Невозможно найти логическую ошибку. Ты просто не умеешь играть.",
    "Система перегружена мемами.",
    "У меня не хватает памяти для этого... В смысле для тебя.",
    "О, опять эта ошибка! Почему бы просто не перезагрузить компьютер?",
    "Мемы убивают процессор. Выключите их на 5 минут.",
    "Ошибка 404: Память не найдена.",
    "Кто-то позвонил? Нет, это просто ошибка в системе.",
    "Запрос на обновление не может быть выполнен: слишком много мемов.",
    "Время ожидания истекло, загрузка не произошла.",
    "Мой создатель сломал меня с этим кодом.",
    "Невозможно продолжить игру, слишком много мемов.",
    "Мемы сыпятся, как ошибки компиляции!",
    "Кто не любит мемы? Это же ошибка!",
    "Слишком много веселых картинок — система перегружена!",
    "Ошибка: Определение «жизни» не найдено.",
    "Внимание! Мозг перегружен. МЕМЫ ВЫХОДЯТ ИЗ ПОД КОНТРОЛЯ!",
    "Ошибка времени: ваша реакция слишком медленная для этих мемов.",
    "Превышен лимит мемов в игре. Перезагрузитесь для продолжения.",
    "Мемы заполняют экран. Уберите их, пожалуйста!",
    "Система сообщает: мемы превращают ваш мозг в хаос.",
    "Ошибка! Не удается вычислить количество мемов в системе.",
    "Вы не можете сдать экзамен, если не поймали мемы!",
    "Мемы на сервере перегружены. Запрос на рестарт.",
    "Превышен лимит использования юмора. Ошибка!",
    "Все мемы повреждены, перезагрузите шутку.",
    "Этот мем занял больше места, чем ваша игра.",
    "Ошибка: Приложение не смогло обработать шутку.",
    "Ваше чувство юмора слишком слабое для этого мема.",
    "Превышено количество мемов на одну игру. Попробуйте снова позже.",
    "Перезагрузите игру для очистки всех мемов.",
    "Ошибка: Мозг не может обработать столь много смеха.",
    "Мемы оказались слишком сложными для выполнения этой задачи.",
    "Этот мем не совместим с вашей операционной системой.",
    "Ошибка в алгоритме. Мемы стали чересчур абсурдными.",
    "Не удается загрузить более смешные мемы. Попробуйте позже.",
    "Слишком много мемов для одного экрана. Перезагрузите и попробуйте снова.",
    "Ошибка! Система настолько переполнена мемами, что не может продолжить работу.",
    "Загрузка мемов... Мозг начинает кипеть.",
    "Ошибка: База данных мемов переполнена.",
    "Слишком много данных! Память не вмещает количество мемов.",
    "Мемы слишком мощные для этой игры. Нужно обновление.",
    "Невозможно продолжить игру. Мемы заняли все свободное место.",
    "Ошибка: Невозможно найти связь между мемом и реальностью.",
    "Память переполнена мемами. Нажмите F5 для перезагрузки.",
    "Приложение перегружено мемами. Система не выдержала.",
    "Слишком много мемов! Не могу остановиться!",
    "Система мемов дала сбой. Рестарт требуется для нормальной работы.",
    "Слишком много шума от мемов, система не может больше функционировать.",
    "Ошибка: мемы не совместимы с вашей текущей ситуацией.",
    "Мемы разрушают реальность. Попробуйте выйти и вернуться позже.",
    "Ошибка загрузки! Не удалось синхронизировать мемы с сервером.",
    "Мемы начали поглощать все вычислительные ресурсы.",
    "Ошибка: Доступ к мемам ограничен. Попробуйте позже.",
    "Мемы заставляют всю систему работать медленно.",
    "Ваши мемы израсходовали все системные ресурсы.",
    "Слишком много мемов для этой машины. Требуется перезагрузка.",
    "Где-то здесь есть ошибка... или это просто мемы?",
    "Перезагрузка не решит проблему с мемами.",
    "Мемы уничтожают все старые шутки. Подготовьтесь к новым!",
    "Этот мем настолько велик, что заблокировал систему.",
    "Загрузка не удалась. Память переполнена мемами.",
    "Ошибка: Пытаетесь загрузить слишком много смеха.",
    "Шутки не подходят для этой операционной системы.",
    "Мемы, кажется, превращаются в вирус. Нужно прекратить их распространение.",
    "Перезагрузка системы не поможет в случае мемов.",
    "Мемы сожрали все ваши байты. Вам нужно больше памяти.",
    "Память полностью занята мемами. Время для рестарта.",
    "Мемы поглотили все ресурсы вашего компьютера.",
    "Мемы настолько велики, что они ломают эту игру.",
    "Слишком много мемов! Прекратите запрашивать их.",
    "Ошибка: слишком много комедийных файлов для этой системы.",
    "Система не может обработать столь сложные мемы.",
    "Мемы превзошли все ожидания! Ошибка при загрузке.",
    "Перегрузка мемами. Это слишком смешно для вашей системы.",
    "Процесс мемов завершился с ошибкой: слишком много юмора.",
    "Превышено количество символов в меме. Время для обновлений.",
]


# Время, через которое будет отображаться мем
MEME_TIME = 5000  # 5000 миллисекунд (5 секунд)

# Для управления временем появления мемов
last_meme_time = time.time()
MEME_INTERVAL = random.randint(5, 10)  # Мемы будут появляться случайным интервалом от 5 до 10 секунд
current_meme = None
meme_end_time = 0

def get_color_shift(base_color, shift_amount):
    r = (base_color[0] + shift_amount) % 256
    g = (base_color[1] + shift_amount * 2) % 256
    b = (base_color[2] + shift_amount * 3) % 256
    return (r, g, b)

def main_menu():
    menu_running = True
    while menu_running:
        screen.fill(BLACK)
        title_text = font.render("Лови числа!", True, WHITE)
        start_text = font.render("Нажмите ENTER для начала игры", True, WHITE)
        settings_text = font.render("Нажмите S для настроек", True, WHITE)
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, screen.get_height() // 4))
        screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, screen.get_height() // 2))
        screen.blit(settings_text, (screen.get_width() // 2 - settings_text.get_width() // 2, screen.get_height() // 2 + 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_running = False
                if event.key == pygame.K_s:
                    settings_menu()

def settings_menu():
    global show_fps, color_change_enabled
    settings_running = True
    while settings_running:
        screen.fill(BLACK)
        fps_text = font.render(f"Показывать FPS: {'ВКЛ' if show_fps else 'ВЫКЛ'} (Нажмите F)", True, WHITE)
        color_text = font.render(f"Изменение цвета чисел: {'ВКЛ' if color_change_enabled else 'ВЫКЛ'} (Нажмите C)", True, WHITE)
        back_text = font.render("Нажмите ESC для выхода", True, WHITE)
        screen.blit(fps_text, (10, 10))
        screen.blit(color_text, (10, 60))
        screen.blit(back_text, (10, 110))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_running = False
                if event.key == pygame.K_f:
                    show_fps = not show_fps
                if event.key == pygame.K_c:
                    color_change_enabled = not color_change_enabled

def pause_menu():
    global running
    pause_running = True
    while pause_running:
        screen.fill(BLACK)
        pause_text = font.render("Пауза", True, WHITE)
        resume_text = font.render("Нажмите P для продолжения", True, WHITE)
        quit_text = font.render("Нажмите ESC для выхода в меню", True, WHITE)
        screen.blit(pause_text, (screen.get_width() // 2 - pause_text.get_width() // 2, screen.get_height() // 4))
        screen.blit(resume_text, (screen.get_width() // 2 - resume_text.get_width() // 2, screen.get_height() // 2))
        screen.blit(quit_text, (screen.get_width() // 2 - quit_text.get_width() // 2, screen.get_height() // 2 + 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_running = False  # Возвращаемся в игру
                if event.key == pygame.K_ESCAPE:
                    pause_running = False
                    main_menu()  # Выход в главное меню

# Функция для отображения случайного мема
def show_random_meme():
    global current_meme, meme_end_time
    current_meme = random.choice(memes)
    meme_end_time = time.time() + MEME_TIME / 1000  # Устанавливаем время окончания показа мема

# Время появления мемов
last_meme_time = time.time()

main_menu()

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Проверяем, не настало ли время для отображения нового мема
    if time.time() - last_meme_time > MEME_INTERVAL:
        show_random_meme()
        last_meme_time = time.time()  # Обновляем время для следующего мема

    # Если мем отображается, показываем его на экране
    if current_meme and time.time() < meme_end_time:
        text_surface = font.render(current_meme, True, RED)
        
        # Центрируем мем на экране
        meme_x = (screen.get_width() - text_surface.get_width()) // 2
        meme_y = (screen.get_height() - text_surface.get_height()) // 2
        screen.blit(text_surface, (meme_x, meme_y))
    else:
        current_meme = None  # Если время мема истекло, очищаем

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            player_x = WIDTH // 2 - player_width // 2
            player_y = HEIGHT - player_height - 10
        if event.type == NEW_NUMBER_EVENT:
            number_value = random.randint(1, 9)
            number_x = random.randint(0, WIDTH - number_width)
            falling_numbers.append({
                "x": number_x, 
                "y": 0, 
                "value": number_value, 
                "base_color": (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)), 
                "color_shift": random.randint(1, 5)  
            })
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Обработка паузы
    if keys[pygame.K_p]:
        pause_menu()

    # Рисуем игрока
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Обработка падения чисел
    for number in falling_numbers[:]:
        number["y"] += number_speed
        if color_change_enabled:
            number["base_color"] = get_color_shift(number["base_color"], number["color_shift"])

        # Проверка на перехват числа игроком
        if (number["x"] + number_width > player_x and number["x"] < player_x + player_width and
            number["y"] + number_height > player_y):
            if number["value"] == target_number:
                score += 1
                target_number = random.randint(1, 9)  # Обновляем цель, если число поймано правильно
            else:
                target_number = random.randint(1, 9)  # Обновляем цель, если число поймано неправильно
            falling_numbers.remove(number)

        # Удаляем число, если оно прошло экран
        if number["y"] > HEIGHT:
            falling_numbers.remove(number)

        # Рисуем число
        number_text = font.render(str(number["value"]), True, number["base_color"])
        screen.blit(number_text, (number["x"], number["y"]))

    # Рисуем счёт
    score_text = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Рисуем целевое число
    target_text = font.render(f"Цель: {target_number}", True, WHITE)
    screen.blit(target_text, (WIDTH - target_text.get_width() - 10, 10))

    # Отображение FPS
    if show_fps:
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
        screen.blit(fps_text, (WIDTH - fps_text.get_width() - 10, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
