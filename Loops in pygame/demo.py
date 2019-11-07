import pygame

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
w = 1
w_dir = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(0, 128, 128), ((80, 80), (w, 150)))
    pygame.display.update()

    w += w_dir
    if w == 200:
        w_dir =w_dir * -1
    clock.tick(60)

pygame.quit()






