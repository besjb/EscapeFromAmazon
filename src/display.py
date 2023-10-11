#!/usr/bin/env python3
import sys, time, pygame
import random
import math



xDim = 10
yDim = 20
standard_wW = 1700
standard_hW = 900
size_boxe = math.floor(min(standard_hW/yDim, standard_wW/xDim))
wW = xDim * size_boxe
hW = yDim * size_boxe

floor_img = pygame.image.load("img/floor.jpg")
boxe_img = pygame.image.load("img/boxe.jpg")
worker_img = pygame.image.load("img/worker.jpg")

floor_img = pygame.transform.scale(floor_img, (size_boxe, size_boxe))
boxe_img = pygame.transform.scale(boxe_img, (size_boxe, size_boxe))
worker_img = pygame.transform.scale(worker_img, (size_boxe, size_boxe))

img = [floor_img, boxe_img, worker_img]

board = [[0 for x in range(xDim)] for y in range(yDim)]

s = pygame.Surface((wW, hW))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((wW, hW))
clock = pygame.time.Clock()
running = True

def init():
    init_boxes(40)
    init_worker()
    print_board()
    #term_print(board)

def term_print_board():
    for y in range(yDim):
        print(board[y])

def print_board():
    for y in range(yDim):
        for x in range(xDim):
            #r = pygame.Rect(x*size_boxe, y*size_boxe, size_boxe, size_boxe)
            #pygame.draw.rect(s, colors[board[y][x]], r)
            screen.blit(img[board[y][x]], (x*size_boxe, y*size_boxe))


def init_worker():
    board[yDim-1][random.randint(0, xDim-1)] = 2

def init_boxes(nb_boxes):
    n = 0
    while(n<nb_boxes):
      x = random.randint(0, xDim-1)
      y = random.randint(0, yDim-1)
      if(board[y][x] == 0):
          board[y][x] = 1
          n += 1



init()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                #print("Key q has been pressed")
                running = False
            if event.key == pygame.K_ESCAPE:
                #print("Key esc has been pressed")
                running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


