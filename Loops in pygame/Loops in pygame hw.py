import pygame



# screen = pygame.display.set_mode((640,480))
# g = 0
# g_dir = 1
# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#
#     pygame.draw.circle(screen, (0, g, 0), (320, 240), 50)
#     pygame.display.update()
#
#     g += g_dir
#     if g >= 255 or g < 1:
#         g_dir = g_dir * -1
#     clock.tick(60)
#
#
# pygame.quit()


# screen = pygame.display.set_mode((640,480))
# r = 49
# r_dir= 1
# r2 = 3
# r2_dir = 2
# r3 = 27
# r3_dir= 1
# r4 = 1
# r4_dir = 17
# r5= 15
# r5_dir= 2
#
# g = 210
# g_dir = 1
# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#
#     pygame.draw.circle(screen, (0, 250, 0), (320, 240), r)
#     pygame.draw.circle(screen, (200, 150, 0), (220, 240), r2)
#     pygame.draw.circle(screen, (0, 250, 0), (420, 240), r3)
#     pygame.draw.circle(screen, (200, 150, 0), (120, 240), r4)
#     pygame.draw.circle(screen, (200, 150, 0), (520, 240), r5)
#
#     pygame.display.update()
#
#     r += r_dir
#     if r <= 1 or r >=50:
#         r_dir = r_dir * -1
#     clock.tick(60)
#
#     r2 += r2_dir
#     if r2 <= 1 or r2 >= 50:
#         r2_dir = r2_dir * -1
#     clock.tick(60)
#
#     r3 += r3_dir
#     if r3 <= 1 or r3 >= 50:
#         r3_dir = r3_dir * -1
#     clock.tick(60)
#
#     r4 += r4_dir
#     if r4 <= 1 or r4 >= 50:
#         r4_dir = r4_dir * -1
#     clock.tick(60)
#     r5 += r5_dir
#     if r5 <= 1 or r5 >= 50:
#         r5_dir = r5_dir * -1
#     clock.tick(60)
#
#
# pygame.quit()




screen = pygame.display.set_mode((640,480))

r = 50
g = 210
g_dir = 1
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    r=r+2
    g= g+1
    for i in range(30):
        pygame.draw.circle(screen, ((r-i*5)%180, (g-i*5)%255,0 ), (320, 240), 300-i*10)




    pygame.display.update()


pygame.quit()


