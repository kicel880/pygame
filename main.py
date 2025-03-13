import pygame
pygame.init()# обезательная программа
window_size=(300,300)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
background_color = (0,0,255)
screen.fill(background_color)
clock = pygame.time.Clock()#фпс
r = pygame.Rect(90,90,150,60)
x = 150
y = 150
while True:#игровой цикл
    screen.fill(background_color)
    r = pygame.Rect(x, y, 60, 60) #создание прямоугольника
    color = (50, 70, 40)
    pygame.draw.rect(screen, color, r) #отрисовка прямоугольника
    clock.tick(40)#40фпс\с
    pygame.display.update()#оюновление содержимого экрана
    for event in pygame.event.get():#события
        if event.type == pygame.KEYDOWN:#если клавиша нажата
            if event.key == pygame.K_a:
                x = x - 50
            if event.key == pygame.K_d:
                x = x + 50
            if event.key == pygame.K_w:
                y = y - 50
            if event.key == pygame.K_s:
                y = y + 50
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()# выход из игры






