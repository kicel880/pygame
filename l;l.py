import pygame#импортируем библеотеку pygame

class Food():#создание класса
    def __init__(self, a, c, d):#создание конструктора   в нем создается свойство   он вызывается при создании объекта
        self.image = pygame.image.load(a)#загрузка картинки,это свойство
        self.rect = self.image.get_rect()#получение прямоугольника от картинки,это свойство
        self.rect.x = c #свойство
        self.rect.y = d #свойство

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

fon = Food("кухня.jpg", 0, 0)

pygame.init()# обязательная команда
window_size=(800,800)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
clock = pygame.time.Clock()#фпс

food1 = Food("шашлык.png", 0, 0)#создание объекта класса food
food2 = Food("шашлык.png", 100,0)#создание объекта класса food
food3 = Food("шашлык.png", 200,0)#создание объекта класса food
food4 = Food("шашлык.png", 300,0)#создание объекта класса food
food5 = Food("шашлык.png", 400,0)#создание объекта класса food
food6 = Food("суши.png", 500,0)#создание объекта класса food
food7 = Food("суши.png", 600,0)#создание объекта класса food
food8 = Food("суши.png", 700,0)#создание объекта класса food
food9 = Food("суши.png", 800,0)#создание объекта класса food
food10 = Food("суши.png", 900,0)#создание объекта класса food
food11 = Food("plate.png", 500, 700)#создание объекта класса food
while True:#игровой цикл
    fon.draw_image() #применение метода отрисовки картинки к объекту-картинке
    food1.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food2.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food3.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food4.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food5.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food6.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    food7.draw_image()  # объект класса food,применения метода отрисовки к объекту класса food
    food8.draw_image()  # объект класса food,применения метода отрисовки к объекту класса food
    food9.draw_image()  # объект класса food,применения метода отрисовки к объекту класса food
    food10.draw_image()  # объект класса food,применения метода отрисовки к объекту класса food
    food11.draw_image()# объект класса food,применения метода отрисовки к объекту класса food
    pygame.display.update()  # оюновление содержимого экрана
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
