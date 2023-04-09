import pygame
import os
import numpy as np
import math

Width = 400
gridWidth = 10
Height = 400
gridHeight = 10
margin = 1
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ai Project")
Hero = pygame.image.load("Hero.png")

grid = []
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)

def DrawGrid():
    for row in range(10):
        for col in range(10):
            color = (255, 255, 255)
            if grid[row][col] == 1:
                color = (0, 0, 0)
            pygame.draw.rect(Window, color, [(margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin, Width // gridWidth - margin, Height // gridHeight - margin])

def main():
    clock = pygame.time.Clock()
    Game = True
    while Game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = round(pos[0] / (Width / gridWidth)) - 1
                row = round(pos[1] // (Height // gridHeight))
                print("Click ", pos, "Grid coordinates: ", row, col)
                grid[row][col] = 1
        DrawGrid()       
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()