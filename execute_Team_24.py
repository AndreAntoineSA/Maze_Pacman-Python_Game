#Maze game code

"""
Created on Tue Apr  28 11:20:05 2020
@authors:
TEAM 24
Amrita Tiwari
André Antoine Saint Ange Gounassegarane Saint Ange
Simpy Surbhi
"""


# Reading from the text file and creating maze
import pygame
import time
import os

WINDOW_NAME = "Maze Game 1.0 [Team 24]"
BLOCKWIDTH = 40
BLOCKHEIGHT = 40
PATH = 'sprites/'
PATH_IMGS = {
    '0': 'path.png',
    '1': 'block.png',
    's': 'pacman.png',
    'p': 'pacman.png',
    'e': 'reward.png',
    'a': 'yellow_key.png',
    'b': 'yellow_door.png',
    'd': 'green_key.png',
    'c': 'green_door.png',
    'f': 'red_key.png',
    'g': 'red_door.png',
    'h': 'blue_key.png',
    'i': 'blue_door.png',
    'V': 'path.png',
    '99': 'path.png',
}
IMGS_OBJS = {}
running_path = []
keys = []
lock_sets = {'a': 'b', 'd': 'c', 'f': 'g', 'h': 'i'}
delay = 0.05

#reading from the file and creating maze list
def create_maze():
    maze = []
    f = open('Maze3.txt', "r")
    dataset = f.readlines()

    for lines in dataset:
        line = lines.split()
        maze.append(line)
        # array =np.array(maze)
    return maze

#creating pygame window
def create_window():
    HEIGHT = len(maze) * BLOCKHEIGHT
    WIDTH = len(maze[0]) * BLOCKWIDTH

    global IMGS_OBJS, screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #window title
    pygame.display.set_caption(WINDOW_NAME)

#    setting logo in the window
#    icon = pygame.image.load('sprites/maze_icon.png')
#    pygame.display.set_icon(icon)

    for code, filename in PATH_IMGS.items():
        img = pygame.image.load(PATH + filename)
        IMGS_OBJS[code] = pygame.transform.scale(img, (BLOCKWIDTH, BLOCKHEIGHT))
    screen.fill((128, 128, 128))
    draw_maze()
    pygame.display.update()

#drawing the maze in co-ordinates
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            x_coord = x * BLOCKWIDTH
            y_coord = y * BLOCKHEIGHT
            screen.blit(IMGS_OBJS[maze[y][x]], (x_coord, y_coord))

def eventListener():
    # Program loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def right(x, y):
    return x < len(maze) - 1 and search(x + 1, y)

def up(x, y):
    return y > 0 and search(x, y - 1)

def left(x, y):
    return x > 0 and search(x - 1, y)

def down(x, y):
    return y < len(maze) - 1 and search(x, y + 1)

#searching for each elements in the grid, start, end and other objects
def search(x, y):
    if maze[y][x] == 'e':
        running_path.append((y, x))
        print('found at %d,%d' % (y, x))
        maze[running_path[-1][0]][running_path[-1][1]] = 'p'
        if len(running_path) > 1:
            maze[running_path[-2][0]][running_path[-2][1]] = 'V'
        draw_maze()
        pygame.display.update()
        time.sleep(delay)
        print(running_path)
        #os._exit(1)
        return True
    elif maze[y][x] in lock_sets.values() and maze[y][x] not in keys:
        return False
    elif maze[y][x] == '1':
        return False
    elif maze[y][x] == 'V':
        return False
    elif maze[y][x] in lock_sets:
        keys.append(lock_sets[maze[y][x]])
        for i in range(0, len(maze) - 1):
            for j in range(0, len(maze[i]) - 1):
                if maze[j][i] == 'V':
                    maze[j][i] = '0'
                    draw_maze()
                    pygame.display.update()
                    time.sleep(delay)
        check_blank_cell(maze)
    #        for l in maze:

    # add the visiting path co-ordinates to the running_path
    running_path.append((y, x))

    # mark those points as visited

    maze[running_path[-1][0]][running_path[-1][1]] = 'p'
    if len(running_path)>1:
        maze[running_path[-2][0]][running_path[-2][1]] = 'V'
    draw_maze()
    pygame.display.update()
    time.sleep(delay)

    # exploring neighbors clockwise from right - up - left - down
    success = down(x, y)
    if success == '':
        running_path.append((y, x))
        maze[running_path[-1][0]][running_path[-1][1]] = 'p'
        if len(running_path) > 1:
            maze[running_path[-2][0]][running_path[-2][1]] = 'V'
        draw_maze()
        pygame.display.update()
        time.sleep(delay)
    if not success:
        success = right(x, y)
        if success == '':
            running_path.append((y, x))
            maze[running_path[-1][0]][running_path[-1][1]] = 'p'
            if len(running_path) > 1:
                maze[running_path[-2][0]][running_path[-2][1]] = 'V'
            draw_maze()
            pygame.display.update()
            time.sleep(delay)
    if not success:
        success = up(x, y)
        if success == '':
            running_path.append((y, x))
            maze[running_path[-1][0]][running_path[-1][1]] = 'p'
            if len(running_path) > 1:
                maze[running_path[-2][0]][running_path[-2][1]] = 'V'
            draw_maze()
            pygame.display.update()
            time.sleep(delay)
    if not success:
        success = left(x, y)
        if success == '':
            running_path.append((y, x))
            maze[running_path[-1][0]][running_path[-1][1]] = 'p'
            if len(running_path) > 1:
                maze[running_path[-2][0]][running_path[-2][1]] = 'V'
            draw_maze()
            pygame.display.update()
            time.sleep(delay)
    if success:
        return True

    # adding the returning path to the running_path
    running_path.append((y, x))
    maze[running_path[-1][0]][running_path[-1][1]] = 'p'
    if len(running_path)>1:
        maze[running_path[-2][0]][running_path[-2][1]] = 'V'
    draw_maze()
    pygame.display.update()
    time.sleep(delay)
    return ''

#checking if its the corner cell
def check_blank_cell(maze):
    while found_blank_cell(maze):
        for y_index in range(0, len(maze)):
            for x_index in range(0, len(maze[y_index])):
                if is_blank_cell(y_index, x_index, maze):
                    block_blank_cell(y_index, x_index, maze)

def found_blank_cell(maze):
    for y_index in range(0, len(maze)):
        for x_index in range(0, len(maze[y_index])):
            if is_blank_cell(y_index, x_index, maze):
                return True
    return False

def block_blank_cell(x, y, maze):
    maze[x][y] = '99'
    draw_maze()
    pygame.display.update()
    time.sleep(delay)

def is_blank_cell(x, y, maze):
    # count_cells is the number of the surrounding cells if they are walls.
    count_cells = 0
    if maze[x][y] == '1' or maze[x][y] == 's' or maze[x][y] == 'e' or maze[x][y] in lock_sets  or maze[x][y] == '99':
        return False
    if 0 < x < len(maze) - 1:
        if 0 < y < len(maze[x]) - 1:
            if maze[x - 1][y] == '1':
                count_cells += 1
            if maze[x + 1][y] == '1':
                count_cells += 1
            if maze[x][y - 1] == '1':
                count_cells += 1
            if maze[x][y + 1] == '1':
                count_cells += 1
    if count_cells > 2:
        return True
    else:
        return False


#calling all the functions inside main
def main():
    global maze
    maze = create_maze()
    create_window()
    check_blank_cell(maze)
    search(1, 1)
    eventListener()

if __name__ == '__main__':
    main()
