import pygame
import os
import numpy as np
import math

Width = 600
gridWidth = 10
Height = 600
gridHeight = 10
margin = 1.2
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ai Project")
Hero = pygame.image.load("Hero.png")
actions = []
grid = []
global actionState, heroCount, goalCount
actionState = 'B'
heroCount = 0
goalCount = 0
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
            elif grid[row][col] == 2:
                Window.blit(Hero, ((margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin))
            elif grid[row][col] == 3:
                Window.blit(Goal, ((margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin))
            pygame.draw.rect(Window, color, [(margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin, Width // gridWidth, Height // gridHeight])

def main():
    global actionState, heroCount, goalCount
    clock = pygame.time.Clock()
    Game = True
    while Game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if actionState[0] == 'B':
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    grid[row][col] = 1
                elif actionState == 'H' and heroCount < 1:
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    grid[row][col] = 2
                    print(grid[row][col])
                    heroCount = 1
                elif actionState == 'G' and goalCount < 1:
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    grid[row][col] = 3
                    goalCount = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for row in range(10):
                        for col in range(10):
                            grid[row][col] = 0
                elif event.key == pygame.K_d:
                    grid[actions[-1][0]][actions[-1][1]] = 0
                    actions.remove(actions[-1])
                elif event.key == pygame.K_h:
                    actionState = 'H'
                elif event.key == pygame.K_b:
                    actionState = 'B'
                elif event.key == pygame.K_g:
                    actionState = 'G'                    
        DrawGrid()       
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()