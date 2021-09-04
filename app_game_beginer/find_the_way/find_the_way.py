import pygame
import time

# khoi tao matran 
board = '01000-00000-00000-00000-00000'
board = [[int(i) for i in row] for row in board.split('-')]


x_amount, y_amount = len(board[0]), len(board)
width, height = 600, 600
x_delta, y_delta = width/x_amount, height/y_amount
x_offset, y_offset = x_delta/2, y_delta/2

radius = 80

visited = [[True if i == 1 else False for i in row] for row in board]

def wait_for_keypress(key):
    global done
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return 
        fps.tick(10)

def draw_board():
    surface.fill((255,255,255))
    pygame.display.set_caption('Be_cong-VN')
    for j in range(y_amount):
        for i in range(x_amount):
            node = board[j][i]
            color = (0,0,0) if node == 1 else (0,0,0)
            x = (i*x_delta)+x_offset-40
            y = (j*y_delta)+y_offset-40
            if node==1:
                pygame.draw.rect(surface, color, pygame.Rect(x,y,radius,radius))
            else:
                pygame.draw.rect(surface, color, pygame.Rect(x,y,radius,radius),2)
            print(x,y)

def reset_visited():
    global board, visited, solved
    visited = [[True if i == 1 else False for i in row] for row in board]
    solved = False
    path = []

def is_solved():
    global visited
    for row in visited:
        if not all(row):
            return False
    return True

def draw_path():
    global path, line_surface
    line_surface.fill((0,0,0,0))
    first = True
    for idx in range(len(path)-1):
        (i, j), (nx, ny) = path[idx], path[idx+1]
        color = (50,50,50,255)
        if first:
            color = (0,0,0,255)
            first = False
        start = ((i*x_delta)+x_offset, (j*y_delta)+y_offset)
        end = ((nx*x_delta)+x_offset, (ny*y_delta)+y_offset)
        pygame.draw.line(line_surface, color, start, end, width = 20)

solved = False
path = []
def solve(i, j):
    global visited, solved, path
    visited[j][i] = True
    path.append((i, j))
    draw_board()
    draw_path()
    surface.blit(line_surface, (0,0))
    pygame.display.flip()

    if is_solved():
        wait_for_keypress(pygame.K_SPACE)

    directions = ((0,1),(0,-1),(1,0),(-1,0))
    for y, x in directions:
        nx, ny = i+x, j+y
        if 0 <= nx < x_amount and 0 <= ny < y_amount:
            if visited[ny][nx] == False:
                solve(nx, ny)
                visited[ny][nx] = False
    visited[j][i] = False
    path.pop()

def solve_all():
    global board, visited
    for j in range(y_amount):
        for i in range(x_amount):
            if board[j][i] == 0:
                solve(i, j)
                reset_visited()

surface = pygame.display.set_mode((width, height))
line_surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
line_surface = line_surface.convert_alpha(line_surface)

done = False
fps = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
            done = True

    solve_all()
    pygame.display.flip()

    done = True
    fps.tick(5)

pygame.quit()