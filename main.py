import pygame

class Food():
    def __init__(self, a, c, d):
        self.image = pygame.image.load(a)
        self.rect = self.image.get_rect()
        self.x = c
        self.y = d

    def draw_image(self):
        screen.blit(self.image, (self.x, self.y))

fon = Food("кухня.jpg", 0, 0)

pygame.init()# обезательная программа
window_size=(1000,1000)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
background_color = (80,90,250)
screen.fill(background_color)
clock = pygame.time.Clock()#фпс
r = pygame.Rect(90,90,150,60)
x = 150
y = 150


while True:#игровой цикл
    fon.draw_image()
    r = pygame.Rect(x, y, 60, 60)
    color = (220, 70, 20)
    pygame.draw.rect(screen, color, r)
    clock.tick(40)#40фпс\с
    pygame.display.update()#оюновление содержимого экрана
    for event in pygame.event.get():#события
        if event.type == pygame.KEYDOWN:#если клавиша нажата
            if event.key == pygame.K_a:
                x = x - 100
            if event.key == pygame.K_d:
                x = x + 100
            if event.key == pygame.K_w:
                y = y - 100
            if event.key == pygame.K_s:
                y = y + 100
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()# выход из игры

