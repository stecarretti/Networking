import pygame
from network import Network
from player import Player


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0


def redraw_window(win, p1, p2):
    win.fill((255, 255, 255))
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(win, p1, p2)


main()