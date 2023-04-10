import pygame
import os
import numpy as np
import math
import time

Width = 600
gridWidth = 10
Height = 600
gridHeight = 10
margin = 1.2
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ai Project")
Hero = pygame.image.load("Hero.png")
Goal = pygame.image.load("1.png")
Goal = pygame.transform.scale(Goal, (Width // gridWidth, Height // gridHeight))
Hero = pygame.transform.scale(Hero, (Width // gridWidth, Height // gridHeight))
actions = []
grid = []
global actionState, heroCount, goalCount
actionState = 'B'
heroCount = 0
goalCount = 0
buildState = 0
secondScreen = False
pygame.font.init()

for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)
for row in range(10):
    for col in range(10):
        grid[row][col] = 1
def createGraph(grid):
    #Create a graph representation of the grid with path cost and heuristic cost
    graph = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
            else:
                if grid[row][col] == 1:
                    graph[(row, col)] = {}
                elif grid[row][col] == 2:
                    graph[(row, col)] = {}
                    heroPos = (row, col)
                elif grid[row][col] == 3:
                    graph[(row, col)] = {}
                    goalPos = (row, col)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
            else:
                if row - 1 >= 0:
                    if grid[row - 1][col] != 0:
                        graph[(row, col)][(row - 1, col)] = 1
                if row + 1 < len(grid):
                    if grid[row + 1][col] != 0:
                        graph[(row, col)][(row + 1, col)] = 1
                if col - 1 >= 0:
                    if grid[row][col - 1] != 0:
                        graph[(row, col)][(row, col - 1)] = 1
                if col + 1 < len(grid[0]):
                    if grid[row][col + 1] != 0:
                        graph[(row, col)][(row, col + 1)] = 1
    return graph, heroPos, goalPos
    
def uniformCostSearch(graph, heroPos, goalPos):
    explored = []
    queue = [[heroPos]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goalPos:
                    return new_path
            explored.append(node)
    return None
        
def DrawGrid():
    for row in range(10):
        for col in range(10):
            if grid[row][col] == 1:
                color = (255, 255, 255)
                pygame.draw.rect(Window, color, [(margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin, Width // gridWidth, Height // gridHeight])
            elif grid[row][col] == 0:
                color = (0, 0, 0)
                pygame.draw.rect(Window, color, [(margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin, Width // gridWidth, Height // gridHeight])
            elif grid[row][col] == 2:
                Window.blit(Hero, ((margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin))
            elif grid[row][col] == 3:
                Window.blit(Goal, ((margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin))
            elif grid[row][col] == 4:
                color = (0, 255, 0)
                pygame.draw.rect(Window, color, [(margin + Width // gridWidth) * col + margin, (margin + Height // gridHeight) * row + margin, Width // gridWidth, Height // gridHeight])
            pygame.display.update()

def DrawSecondScreen():
    global Width, Height, Window
    Window.fill((255, 255, 255))
    pygame.draw.rect(Window, (255, 255, 255), (0, 0, Width // 2, 100))
    pygame.draw.rect(Window, (255, 255, 255), (Width // 2, 0, Width // 2, 100))
    pygame.draw.rect(Window, (255, 255, 255), (0, 100, Width // 2, 100))
    pygame.draw.rect(Window, (255, 255, 255), (Width // 2, 100, Width // 2, 100))
    pygame.draw.rect(Window, (255, 255, 255), (0, 200, Width , 100))
    pygame.draw.rect(Window, (0, 0, 0), (0, 0, Width // 2, 100), 2)
    pygame.draw.rect(Window, (0, 0, 0), (Width // 2, 0, Width // 2, 100), 2)
    pygame.draw.rect(Window, (0, 0, 0), (0, 100, Width // 2, 100), 2)
    pygame.draw.rect(Window, (0, 0, 0), (Width // 2, 100, Width // 2, 100), 2)
    font = pygame.font.SysFont(None,30)
    text = font.render("Uniform Cost Search", 1, (0, 0, 0))
    Window.blit(text, ((Width // 4) - (text.get_width() // 2), (50) - (text.get_height() // 2)))
    text = font.render("Breadth-first Search", 1, (0, 0, 0))
    Window.blit(text, ((Width // 4) * 3 - (text.get_width() // 2), (50) - (text.get_height() // 2)))
    text = font.render("Depth-first Search", 1, (0, 0, 0))
    Window.blit(text, ((Width // 4) - (text.get_width() // 2), (50) + 100 - (text.get_height() // 2)))
    text = font.render("Depth-limited Search", 1, (0, 0, 0))
    Window.blit(text, ((Width // 4) * 3 - (text.get_width() // 2), (50) + 100 - (text.get_height() // 2)))
    text = font.render("Iterative deepening depth-first search", 1, (0, 0, 0))
    Window.blit(text, ((Width // 2)  - (text.get_width() // 2), (50) + 200 - (text.get_height() // 2)))
    pygame.display.update()           

def DrawPath(path):
    if path == None:
        print("No path found")
    else:
        for i in range(len(path)):
            grid[path[i][0]][path[i][1]] = 4
            DrawGrid()
            time.sleep(0.5)

def getAnswer(mousePos):
    if mousePos[0] < Width // 2 and mousePos[1] < 100:
        return "UCS"
    elif mousePos[0] > Width // 2 and mousePos[1] < 100:
        return "BFS"
    elif mousePos[0] < Width // 2 and mousePos[1] > 100 and mousePos[1] < 200:
        return "DFS"
    elif mousePos[0] > Width // 2 and mousePos[1] > 100 and mousePos[1] < 200:
        return "DLS"
    elif mousePos[1] > 200:
        return "IDDFS"
    else:
        return None
    

def main():
    global actionState, heroCount, goalCount, buildState, secondScreen
    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if actionState[0] == 'B' and buildState == 0:
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    if grid[row][col] == 2 or grid[row][col]  == 3:
                        continue
                    else:
                        grid[row][col] = 0
                        print(grid)
                elif actionState == 'H' and heroCount < 1 and buildState == 0:
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    if grid[row][col] == 0 or grid[row][col]  == 3:
                        continue
                    else:
                        grid[row][col] = 2
                        heroCount = 1
                        print(grid)
                elif actionState == 'G' and goalCount < 1 and buildState == 0:
                    pos = pygame.mouse.get_pos()
                    col = (pos[0] // (Width // gridWidth))
                    row = (pos[1] // (Height // gridHeight))
                    actions.append((row, col))
                    if grid[row][col] == 0 or grid[row][col]  == 2:
                        continue
                    else:
                        grid[row][col] = 3
                        goalCount = 1
                elif secondScreen:
                    pos = pygame.mouse.get_pos()
                    if getAnswer(pos) == "UCS":
                        Window.fill((0, 0, 0))
                        DrawPath(uniformCostSearch(graph, heroPos, goalPos))
                        secondScreen = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for row in range(10):
                        for col in range(10):
                            grid[row][col] = 1
                    actions.clear()
                    buildState = 0
                    heroCount = 0
                    goalCount = 0
                elif event.key == pygame.K_d:
                    grid[actions[-1][0]][actions[-1][1]] = 1
                    actions.remove(actions[-1])
                elif event.key == pygame.K_h:
                    actionState = 'H'
                elif event.key == pygame.K_b:
                    actionState = 'B'
                elif event.key == pygame.K_g:
                    actionState = 'G'
                elif event.key == pygame.K_s:
                    buildState = 1
                    graph , heroPos, goalPos = createGraph(grid)
                    secondScreen = True
                    DrawSecondScreen()
        if secondScreen == False:            
           DrawGrid()       
    pygame.quit()
if __name__ == "__main__":
    main()