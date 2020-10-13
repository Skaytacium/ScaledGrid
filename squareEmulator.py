import pygame
pygame.init()

gridSize = 20
desiredRad = 10
displaySize = 750

screen = pygame.display.set_mode([displaySize, displaySize])
running = True

distance = (((displaySize / desiredRad) - gridSize) * desiredRad) / (gridSize * 2)
xArray = []
yArray = []

for n in range(gridSize):
    coordinate = int((distance * (n + 1)) + ((desiredRad + distance) * n) + (desiredRad / 2))
    xArray.append(coordinate)
    yArray.append(coordinate)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for a in range(gridSize):
        for b in range(gridSize):
            pygame.draw.circle(screen, (255, 255, 255), (xArray[a], yArray[b]), desiredRad)
    pygame.display.update()

pygame.quit()