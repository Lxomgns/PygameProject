import pygame
import random
import math

import pygame.camera

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 8
COLS = 8
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("comicsans", 60, bold = True)
MOVE_VEL = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
        (237, 197, 63),
        (233, 185, 40),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col*RECT_WIDTH
        self.y = row*RECT_HEIGHT

    def get_color(self):
        a = -1
        b = self.value
        while True:
            if b%2 == 0:
                b = b/2
                a+=1
            else:
                break
        return self.COLORS[a]
    
    def draw(self, window):
        pygame.draw.rect(window, self.get_color(), (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(str(self.value), True, FONT_COLOR)
        window.blit(text, (self.x+RECT_WIDTH/2-text.get_width()/2, self.y+RECT_HEIGHT/2-text.get_height()/2))
    
    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0,0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    for tile in tiles.values():
        tile.draw(window)

    pygame.display.update()

def move_tiles(window, tiles, clock, direction):
    #와 슈발 이거 어케 만들지 에반데? 하..
    updated = True
    if direction == "left":
        delta = [-MOVE_VEL, 0]
    elif direction == "right":
        delta = [MOVE_VEL, 0]
    elif direction == "up":
        delta = [0, -MOVE_VEL]
    elif direction == "down":
        delta = [0, MOVE_VEL]

    while updated:
        clock.tick(FPS)
        updated = False
        

def generate_tiles(tiles):
    birth = [2,4]
    for i in range(2):
        while (True):
            row = random.randrange(0, ROWS)
            col = random.randrange(0, COLS)
            if (str(row)+str(col) in tiles):
                pass
            else:
                break
        tiles[f"{row}{col}"] = Tile(random.choice(birth),row,col)
    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True
    tiles = {}
    tiles = generate_tiles(tiles)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, tiles)
    
    pygame.quit()

if __name__=="__main__":
    main(WINDOW)