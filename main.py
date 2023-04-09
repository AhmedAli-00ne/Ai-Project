import pygame
Width = 500
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ai Project")

def main():
    clock = pygame.time.Clock()
    Game = True
    while Game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()