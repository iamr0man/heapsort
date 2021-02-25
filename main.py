# Python implementation of the
# Sorting visualiser: Heap Sort

# Imports
import re

import pygame
import random
import time
import numpy as np

pygame.font.init()
startTime = time.time()

# Total window
screen = pygame.display.set_mode(
    (1000, 650)
)

# Title and Icon
pygame.display.set_caption(
    "SORTING VISUALISER"
)

# Uncomment below lines for setting
# up the icon for the visuliser
# img = pygame.image.load('sorticon.png')
# pygame.display.set_icon(img)

# Boolean variable to run
# the program in while loop
run = True
main_page = True

# Window size and some initials
width = 1000
length = 600
array = [0] * 151
arr_clr = [(0, 204, 120)] * 151
clr_ind = 0
clr = [(0, 204, 120), (150, 5, 150),
       (0, 0, 153), (255, 120, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)

numbers = [
    pygame.K_SPACE,
    pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
    pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
]

user_text = ''

input_rect = pygame.Rect(20, 80, 950, 22)

program_rect = pygame.Rect(20, 105, 450, 200)
me_rect = pygame.Rect(520, 105, 450, 200)

color = pygame.Color('black')


# Function to generate new Array
def generate_arr():
    for i in range(1, 151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)


# Initially generate a array
generate_arr()


# Function to refill the
# updates on the window
def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(10)


# Sorting Algorithm: Heap Sort
def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        pygame.event.pump()
        heapify(array, i, n)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        arr_clr[i] = clr[1]
        refill()
        heapify(array, 0, i)


def heapify(array, root, size):
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root
    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != root:
        arr_clr[largest] = clr[2]
        arr_clr[root] = clr[2]
        array[largest], \
        array[root] = array[root], \
                      array[largest]
        refill()
        arr_clr[largest] = clr[0]
        arr_clr[root] = clr[0]
        heapify(array, largest, size)
        refill()


# Function to Draw the array values
def draw():
    # Text should be rendered
    txt = fnt.render("Сортування: Нажміть 'ENTER'",
                     1, (0, 0, 0))
    # Position where text is placed
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("Створити новий масив: Нажміть 'R'",
                      1, (0, 0, 0))
    screen.blit(txt1, (20, 40))
    txt4 = fnt.render("Введіть масив вручну через пробіл:",
                      1, (0, 0, 0))
    screen.blit(txt4, (20, 60))
    txt2 = fnt.render("Довідка про розробника: Нажміть 'D'", 1, (0, 0, 0))
    screen.blit(txt2, (20, 110))
    text3 = fnt1.render("Тривалість(секунди): " +
                        str(int(time.time() - startTime)),
                        1, (0, 0, 0))
    screen.blit(text3, (700, 20))
    txt5 = fnt1.render("Алгоритм: HEAP SORT", 1, (0, 0, 0))
    screen.blit(txt5, (700, 40))
    element_width = (width - 150) // 150
    boundry_arr = 1000 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 130),
                     (1000, 130), 6)

    text_surface = fnt.render(user_text, True, (0, 0, 0))
    pygame.draw.rect(screen, color, input_rect, 2)
    screen.blit(text_surface, input_rect)

    # Drawing the array values as lines
    for i in range(1, 151):
        if len(array) > i:
            pygame.draw.line(screen, arr_clr[i],
                             (boundry_arr * i - 3, 137),
                             (boundry_arr * i - 3, array[i] * boundry_grp + 137),
                             element_width)


def draw_info():
    # Text should be rendered
    txt = fnt.render("Про мене", 1, (0, 0, 0))
    # Position where text is placed
    screen.blit(txt, (460, 20))

    txt2 = fnt.render("Головне меню: Нажміть 'S'", 1, (0, 0, 0))
    screen.blit(txt2, (20, 50))

    pygame.draw.line(screen, (0, 0, 0), (0, 95), (1000, 95), 6)

    program_text = 'Програма розроблена в PyCharm на мові \nпрограмування Python за допомогою \nбібліотеки Pygame'
    blit_text(screen,program_text, (30,120), fnt)
    pygame.draw.rect(screen, color, program_rect, 2)

    me_text = 'Розробник: Корнієнко Ромам Сергійович \nСтудент 472 групи \nПроект розроблений для курсової\nроботи'
    blit_text(screen, me_text, (530, 120), fnt)
    pygame.draw.rect(screen, color, me_rect, 2)


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def convert_to_int(n):
    return int(n)


def validate(text):
    # text_after = re.sub(regex_search_term, regex_replacement, text_before
    new_text = text.strip()
    return re.sub(r' +', ' ', new_text).split(' ')


# Program should be run
# continuously to keep the window open
while run:
    # background
    screen.fill((255, 255, 255))

    # Event handler stores all event
    for event in pygame.event.get():

        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                main_page = True
                pygame.display.update()
            if event.key == pygame.K_d:
                main_page = False
                pygame.display.update()
            if event.key == pygame.K_r:
                generate_arr()
            if event.key == pygame.K_RETURN and event.key != pygame.K_r:
                if len(user_text):
                    array = np.fromiter(map(convert_to_int, validate(user_text)), int)
                    draw()
                    pygame.display.update()
                    time.sleep(3)
                heapSort(array)
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            if numbers.count(event.key) == 0:
                break
            else:
                user_text += event.unicode
    draw() if main_page else draw_info()
    pygame.display.update()

pygame.quit()
