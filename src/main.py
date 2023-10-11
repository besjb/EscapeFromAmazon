#!/usr/bin/env python3

#agent = 1
#sortie = 2
#carton = 3
import random
import os
import sys, time, pygame
import random
import math

"""
Move :      push :      pull :      move_box N:     S:      O:      E:
    N 1         N 5         N 9             S 13    N 16    E 19    O 22
    S 2         S 6         S 10            O 14    O 17    N 20    N 23
    O 3         O 7         O 11            E 15    E 18    S 21    S 24    
    E 4         E 8         E 12            

"""
dimX = 5
dimY = 5

standard_wW = 1700
standard_hW = 900
size_boxe = math.floor(min(standard_hW/dimY, standard_wW/dimX))
wW = dimX * size_boxe
hW = dimY * size_boxe

floor_img = pygame.image.load("img/floor.jpg")
boxe_img = pygame.image.load("img/boxe.jpg")
worker_img = pygame.image.load("img/worker.jpg")

floor_img = pygame.transform.scale(floor_img, (size_boxe, size_boxe))
boxe_img = pygame.transform.scale(boxe_img, (size_boxe, size_boxe))
worker_img = pygame.transform.scale(worker_img, (size_boxe, size_boxe))

img = [floor_img,worker_img ,2,boxe_img, ]

room = [[0 for x in range(dimX)] for y in range(dimY)]

s = pygame.Surface((wW, hW))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((wW, hW))
clock = pygame.time.Clock()
running = True

def init():
    init_boxes(40)
    init_worker()
    print_room(room)
    #term_print(room)

def term_print_room():
    for y in range(dimY):
        print(room[y])

def print_room():
    for x in range(dimX):
        for y in range(dimY):
            #r = pygame.Rect(x*size_boxe, y*size_boxe, size_boxe, size_boxe)
            #pygame.draw.rect(s, colors[room[y][x]], r)
            screen.blit(img[room[y][x]], (x*size_boxe, y*size_boxe))


def init_worker():
    room[dimY-1][random.randint(0, dimX-1)] = 2

def init_boxes(nb_boxes):
    n = 0
    while(n<nb_boxes):
      x = random.randint(0, dimX-1)
      y = random.randint(0, dimY-1)
      if(room[y][x] == 0):
          room[y][x] = 1
          n += 1

class Agent:
    def __init__(self):
        self.x=0
        self.y=0
        self.actions = []
        self.outX = dimX - 1
        self.outY = dimY - 1
        self.nb_cartons = 10
        self.goal = 0
        self.nb_goal = 1

    def update(self,x,y):
        self.x=x 
        self.y=y 


    #fonctions remplissage de la liste des actions possible
    def action_possible(self,room):
        actions = []
        self.move(room, actions)
        self.push(room, actions)
        #self.pull(room, actions)
        return actions
    #self.move_box(room)

    def move(self,room, actions):
        if self.x-1 >= 0 and room[self.x-1][self.y] == 0 :
            actions.append(1)
        if self.x+1 < dimX and room[self.x+1][self.y] == 0:
            actions.append(2)
        if self.y-1 >= 0 and room[self.x][self.y-1] == 0:
            actions.append(3)
        if self.y+1 < dimY and room[self.x][self.y+1] == 0:
            actions.append(4)

    #fonctions do
    def do_move(self,room,direction):
        room[self.x][self.y]=0
        match direction:
            case 1:
                self.x-=1
            case 2:
                self.x+=1
            case 3:
                self.y-=1
            case 4:
                self.y+=1
            case _:
                return False
        room[self.x][self.y]=1

            #fonctions undo
    def undo_move(self,room,direction):
        match direction:
            case 1:
                self.do_move(room,2)
            case 2:
                self.do_move(room,1)
            case 3:
                self.do_move(room,4)
            case 4:
                self.do_move(room,3)
            case _:
                return False

    def push(self,room, actions):
        if self.x-1 >= 0 and room[self.x-1][self.y] == 3 :
            if self.x-2 >= 0 and room[self.x-2][self.y] == 0 :
                actions.append(5)
        if self.x+1 < dimX and room[self.x+1][self.y] == 3:
            if self.x+2 < dimX and room[self.x+2][self.y] == 0 :
                actions.append(6)
        if self.y-1 >= 0 and room[self.x][self.y-1] == 3:
            if self.y-2 >= 0 and room[self.x][self.y-2] == 0 :
                actions.append(7)
        if self.y+1 < dimY and room[self.x][self.y+1] == 3:
            if self.y+2 < dimY and room[self.x][self.y+2] == 0 :
                actions.append(8)

    def do_push(self,room,direction):
        match direction:
            case 5:
                room[self.x-1][self.y]=0
                room[self.x-2][self.y]=3
            case 6:
                room[self.x+1][self.y]=0
                room[self.x+2][self.y]=3
            case 7:
                room[self.x][self.y-1]=0
                room[self.x][self.y-2]=3
            case 8:
                room[self.x][self.y+1]=0
                room[self.x][self.y+2]=3
            case _:
                return False

    def undo_push(self,room,direction):
        match direction:
            case 5:
                room[self.x-1][self.y]=3
                room[self.x-2][self.y]=0
            case 6:
                room[self.x+1][self.y]=3
                room[self.x+2][self.y]=0
            case 7:
                room[self.x][self.y-1]=3
                room[self.x][self.y-2]=0
            case 8:
                room[self.x][self.y+1]=3
                room[self.x][self.y+2]=0
            case _:
                return False
                
    def pull(self,room, actions):
        if self.x-1 >= 0 and room[self.x-1][self.y] == 3 :
            if self.x+1 <dimX and room[self.x+1][self.y] == 0 :
                actions.append(9)
        if self.x+1 < dimX and room[self.x+1][self.y] == 3:
            if self.x-1 >= 0 and room[self.x-1][self.y] == 0 :
                actions.append(10)
        if self.y-1 >= 0 and room[self.x][self.y-1] == 3:
            if self.y+1 <dimY and room[self.x][self.y+1] == 0 :
                actions.append(11)
        if self.y+1 < dimY and room[self.x][self.y+1] == 3:
            if self.y-1 >= 0 and room[self.x][self.y-1] == 0 :
                actions.append(12)

    def undo_pull(self,room,direction):
        match direction:
            case 9:
                room[self.x-2][self.y]=3
                room[self.x-1][self.y]=1
                room[self.x][self.y]=0
                self.x-=1
            case 10:
                room[self.x+2][self.y]=3
                room[self.x+1][self.y]=1
                room[self.x][self.y]=0
                self.x+=1
            case 11:
                room[self.x][self.y-2]=3
                room[self.x][self.y-1]=1
                room[self.x][self.y]=0
                self.y-=1
            case 12:
                room[self.x][self.y+2]=3
                room[self.x][self.y+1]=1
                room[self.x][self.y]=0
                self.y+=1
            case _:
                return False

    def move_box(self,room, actions):
        if self.x-1 >= 0 and room[self.x-1][self.y] == 3 :
            #S
            if self.x+1 < dimX and room[self.x+1][self.y] == 0 :
                actions.append(13)
                #O
            if self.y-1 >= 0 and room[self.x][self.y-1] == 0 :
                actions.append(14)
                #E
            if self.y+1 < dimY and room[self.x][self.y+1] == 0 :
                actions.append(15)
        if self.x+1 < dimX and room[self.x+1][self.y] == 3:
            #N
            if self.x-1 >= 0 and room[self.x-1][self.y] == 0 :
                actions.append(16)
                #O
            if self.y-1 >= 0 and room[self.x][self.y-1] == 0 :
                actions.append(17)
                #E
            if self.y+1 < dimY and room[self.x][self.y+1] == 0 :
                actions.append(18)
        if self.y-1 >= 0 and room[self.x][self.y-1] == 3:
            #E
            if self.y+1 < dimY and room[self.x+1][self.y] == 0 :
                actions.append(19)
                #N
            if self.x-1 >= 0 and room[self.x-1][self.y] == 0 :
                actions.append(20)
                #S
            if self.x+1 < dimX and room[self.x+1][self.y] == 0 :
                actions.append(21)
        if self.y+1 < dimY and room[self.x][self.y+1] == 3:
            #O
            if self.y-1 >= 0 and room[self.x][self.y-1] == 0 :
                actions.append(22)
                #N
            if self.x-1 >= 0 and room[self.x-1][self.y] == 0 :
                actions.append(23)
                #S
            if self.x+1 < dimX and room[self.x+1][self.y] == 0 :
                actions.append(24)



    def do_pull(self,room,direction):
        match direction:
            case 9:
                room[self.x-1][self.y]=0
                room[self.x][self.y]=3
                room[self.x+1][self.y]=1
                self.x+=1
            case 10:
                room[self.x+1][self.y]=0
                room[self.x][self.y]=3
                room[self.x-1][self.y]=1
                self.x-=1
            case 11:
                room[self.x][self.y-1]=0
                room[self.x][self.y]=3
                room[self.x][self.y+1]=1
                self.y+=1
            case 12:
                room[self.x][self.y+1]=0
                room[self.x][self.y]=3
                room[self.x][self.y-1]=1
                self.y-=1
            case _:
                    return False

    def do_move_box(self,room,direction):
        
        match direction:
            case 13:
                room[self.x-1][self.y]=0
                room[self.x+1][self.y]=3
            case 14:
                room[self.x-1][self.y]=0
                room[self.x][self.y-1]=3
            case 15:
                room[self.x-1][self.y]=0
                room[self.x][self.y+1]=3
        
            case 16:
                room[self.x+1][self.y]=0
                room[self.x-1][self.y]=3
            case 17:
                room[self.x+1][self.y]=0
                room[self.x][self.y-1]=3
            case 18:
                room[self.x+1][self.y]=0
                room[self.x][self.y+1]=3
            
            case 19:
                room[self.x][self.y-1]=0
                room[self.x][self.y+1]=3
            case 20:
                room[self.x][self.y-1]=0
                room[self.x-1][self.y]=3
            case 21:
                room[self.x][self.y-1]=0
                room[self.x+1][self.y]=3
            
            case 22:
                room[self.x][self.y+1]=0
                room[self.x][self.y-1]=3
            case 23:
                room[self.x][self.y+1]=0
                room[self.x-1][self.y]=3
            case 24:
                room[self.x][self.y+1]=0
                room[self.x+1][self.y]=3
            
            case _:
                return False

    def do(self, room, direction):
        if(direction < 5):
            self.do_move(room, direction)
        elif(direction < 9):
            self.do_push(room, direction)
        elif(direction < 13):
            self.do_pull(room, direction)
        else:
            self.do_move_box(room, direction)



    def undo_move_box(self,room,direction):
        match direction:
            case 13:
                room[self.x-1][self.y]=3
                room[self.x+1][self.y]=0
            case 14:
                room[self.x-1][self.y]=3
                room[self.x][self.y-1]=0
            case 15:
                room[self.x-1][self.y]=3
                room[self.x][self.y+1]=0
        
            case 16:
                room[self.x+1][self.y]=3
                room[self.x-1][self.y]=0
            case 17:
                room[self.x+1][self.y]=3
                room[self.x][self.y-1]=0
            case 18:
                room[self.x+1][self.y]=3
                room[self.x][self.y+1]=0
            
            case 19:
                room[self.x][self.y-1]=3
                room[self.x][self.y+1]=0
            case 20:
                room[self.x][self.y-1]=3
                room[self.x-1][self.y]=0
            case 21:
                room[self.x][self.y-1]=3
                room[self.x+1][self.y]=0
            
            case 22:
                room[self.x][self.y+1]=3
                room[self.x][self.y-1]=0
            case 23:
                room[self.x][self.y+1]=3
                room[self.x-1][self.y]=0
            case 24:
                room[self.x][self.y+1]=3
                room[self.x+1][self.y]=0
            
            case _:
                return False

    def undo(self, room, direction):
        if(direction < 5):
            self.undo_move(room, direction)
            return;
        elif(direction < 9):
            self.undo_push(room, direction)
            return;
        elif(direction < 13):
            self.undo_pull(room, direction)
            return;
        else:
            self.undo_move_box(room, direction)

def remplissage(room,nbCarton,agent):
    room[0][0] = 1
    agent.update(0,0)

    #ajout des cartons sur la room et dans la liste
    '''
    for i in range(nbCarton) :
        a = random.randrange(dimX)
        b = random.randrange(dimY)
        
        while room[a][b] != 0:
            a = random.randrange(dimX)
            b = random.randrange(dimY)
        room[a][b] = 3
    '''
    room[1][1] = 3
    
def affiche(room):
    for i in room:
        print(i)
    print()

def eval_goal(agent):
    if(agent.goal >= agent.nb_goal):
        return 1
    return 0

def check_box(room, agent):
    if(room[agent.outX][agent.outY] == 3):
        agent.goal += 1
        room[agent.outX][agent.outY] = 0

def print_info_st(agent, room, action):
    print("\nSEARCH TREE")
    print("=============")
    print("agent.xy : [", agent.x, "]", "[", agent.y, "]")
    print("action = ", action)
    affiche(room)

def search_tree(room, agent, solve_actions, save_rooms, depth):

    if room in save_rooms:#si on a déjà croisé cette room on stop la recherche
        #affiche(room)
        print("deja croisée")
        return 0
    room_copy = [row[:] for row in room]
    save_rooms.append(room_copy)#si on n'a pas croisé la room on l'ajoute à save_rooms
    if(eval_goal(agent) == 1):#le but est remplis
        return 1
    actions = agent.action_possible(room)#on récupère la liste des action possibles
    for action in actions:
        agent.do(room, action)#on effectue une action
        #print_info_st(agent, room, action)
        check_box(room, agent)
        solve_actions.append(action)#on ajoute cette action à la liste de la solution
        ret = search_tree(room, agent, solve_actions, save_rooms, depth+1)#appel récursif prochain fils
        agent.undo(room, action)#on défait l'action
        if(ret == 1):#on a trouvé une solution (on sort)
           return 1
        del(solve_actions[-1])
    return 0

def do_solution(room, agent, solve_actions):
    print("SOLUTION :")
    print(solve_actions)
    affiche(room)
    print_room()
    for action in solve_actions:
        agent.do(room, action)
        affiche(room)
        print_room()

solve_actions = []
save_rooms = []
#room = [[0 for x in range(dimX)] for y in range(dimY)]
agent=Agent()
remplissage(room,1,agent)
affiche(room)
search_tree(room, agent, solve_actions, save_rooms, 0)
#do_solution(room, agent, solve_actions)
indice_action=0
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
    print("SOLUTION :")
    print(solve_actions)
    affiche(room)
    print_room()
    
    time.sleep(0.1)
    agent.do(room, solve_actions[indice_action])
    affiche(room)
    print_room()
    if(indice_action<len(solve_actions)):
        indice_action+=1
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()