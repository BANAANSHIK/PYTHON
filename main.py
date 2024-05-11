import pygame


screen = pygame.display.set_mode((500,400))

screen.fill((194,250,220))
pygame.display.update()

Time_clock=pygame.time.Clock()

r = 0
g = 0
b = 0
while True:
    r = r + 1
    screen.fill((r,g,b))
    pygame.display.update()
    if r==255:
        r=0
    print(r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    Time_clock.tick(60)