import pygame
Width = 500
Height = 500
Window = pygame.display.set_mode((Width, Height))

def main():
    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False