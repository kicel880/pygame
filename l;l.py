import pygame#импортируем библеотеку pygame
from random import *

class Food():#создание класса
    def __init__(self, a, c, d):#создание конструктора   в нем создается свойство   он вызывается при создании объекта
        self.image = pygame.image.load(a)#загрузка картинки,это свойство
        self.rect = self.image.get_rect()#получение прямоугольника от картинки,это свойство
        self.rect.x = c #свойство
        self.rect.y = d #свойство,


    def move_plate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def move_food(self):
        self.rect.y += 5

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

fon = Food("кухня.jpg", 0, 0)

pygame.init()# обязательная команда
window_size=(800,700)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
clock = pygame.time.Clock()#фпс

food1 = Food("шашлык.png", 0,randint(-400, 0)) #создание объекта класса food
food2 = Food("шашлык.png",100,randint(-400, 0))#создание объекта класса food
food3 = Food("шашлык.png",200,randint(-400, 0))#создание объекта класса food
food4 = Food("шашлык.png",300,randint(-400, 0)) #создание объекта класса food
food5 = Food("шашлык.png",400,randint(-400, 0)) #создание объекта класса food
food6 = Food("суши.png",500,randint(-400, 0)) #создание объекта класса food
food7 = Food("суши.png",600,randint(-400, 0))#создание объекта класса food
food8 = Food("суши.png",650,randint(-400, 0))#создание объекта класса food
food9 = Food("суши.png",700,randint(-400, 0))#создание объекта класса food
food10 = Food("суши.png",750,randint(-400, 0))#создание объекта класса food
plate = Food("plate.png",350,600 )#создание объекта класса food
food_list = [food1, food2, food3, food4, food5, food6, food7, food8, food9, food10]
while True:#игровой цикл
    fon.draw_image() #применение метода отрисовки картинки к объекту-картинке
    for i in food_list:
        if plate.rect.colliderect(i.rect):
            food_list.remove(i)
        if i.rect.y > 800:
            i.rect.y = 0
        if food_list == []:
            pygame.QUIT()
        i.draw_image()
        i.move_food()
    plate.draw_image()
    plate.move_plate()#применение к методу объекта

    pygame.display.update()  # обновление содержимого экрана
    clock.tick(40)#40фпс\с
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()#выход из игры
    pygame.display.update()  #обновление содержимого экрана
'''
if event.type == pygame.KEYDOWN:  # если клавиша нажата
    if event.key == pygame.K_a:
        x = x - 50
    if event.key == pygame.K_d:
        x = x + 50'''
