import pygame

class Food():
    def __init__(self, a, c, d):
        self.image = pygame.image.load(a)#загрузка картинки
        self.rect = self.image.get_rect()#получение прямоугольника от картинки
        self.x = c
        self.y = d

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.image, (self.x, self.y))

fon = Food("кухня.jpg", 0, 0)

pygame.init()# обязательная программа
window_size=(800,800)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
clock = pygame.time.Clock()#фпс

food1 = Food("шашлык.png", 0, 0)
food2 = Food("шашлык.png", 100,0)
food3 = Food("шашлык.png", 200,0)
food4 = Food("шашлык.png", 300,0)
food5 = Food("шашлык.png", 400,0)
while True:#игровой цикл
    fon.draw_image() #применение метода отрисовки картинки к объекту-картинке
    food1.draw_image()
    food2.draw_image()
    food3.draw_image()
    food4.draw_image()
    food5.draw_image()
    clock.tick(40)#40фпс\с
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()#выход из игры
    pygame.display.update()  #обновление содержимого экрана
