#!/usr/bin/env python3

#agent = 1
#sortie = 2
#carton = 3
import random
import os
"""
Move :      push :      pull :      move_box N:     S:      O:      E:
    N 1         N 5         N 9             S 13    N 16    E 19    O 22
    S 2         S 6         S 10            O 14    O 17    N 20    N 23
    O 3         O 7         O 11            E 15    E 18    S 21    S 24    
    E 4         E 8         E 12            

"""
dimX = 3
dimY = 3
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
    def action_possible(self,map):
        actions = []
        self.move(map, actions)
        self.push(map, actions)
        self.pull(map, actions)
        return actions
        #self.move_box(map)

    def move(self,map, actions):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
            actions.append(1)
        if self.x+1 < dimX and map[self.x+1][self.y] == 0:
            actions.append(2)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 0:
            actions.append(3)
        if self.y+1 < dimY and map[self.x][self.y+1] == 0:
            print("MOVE")
            print("move info", map[self.x][self.y+1])
            print("self.yx = ", self.x, self.y)
            affiche(map)
            print()
            actions.append(4)

    def push(self,map, actions):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
            if self.x-2 >= 0 and map[self.x-2][self.y] == 0 :
                actions.append(5)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
            if self.x+2 < dimX and map[self.x+2][self.y] == 0 :
                actions.append(6)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
            if self.y-2 >= 0 and map[self.x][self.y-2] == 0 :
                actions.append(7)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
            if self.y+2 < dimY and map[self.x][self.y+2] == 0 :
                actions.append(8)
                
    def pull(self,map, actions):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
            if self.x+1 <dimX and map[self.x+1][self.y] == 0 :
                actions.append(9)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                actions.append(10)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
            if self.y+1 <dimY and map[self.x][self.y+1] == 0 :
                actions.append(11)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                actions.append(12)

    def move_box(self,map, actions):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                actions.append(13)
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                actions.append(14)
                    #E
            if self.y+1 < dimY and map[self.x][self.y+1] == 0 :
                actions.append(15)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                actions.append(16)
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                actions.append(17)
                    #E
            if self.y+1 < dimY and map[self.x][self.y+1] == 0 :
                actions.append(18)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
                    #E
            if self.y+1 < dimY and map[self.x+1][self.y] == 0 :
                actions.append(19)
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                actions.append(20)
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                actions.append(21)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                actions.append(22)
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                actions.append(23)
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                actions.append(24)

    #fonctions do
    def do_move(self,map,direction):
        map[self.x][self.y]=0
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
        map[self.x][self.y]=1
    
    def do_push(self,map,direction): 
        match direction:
            case 5:
                map[self.x-1][self.y]=0
                map[self.x-2][self.y]=3
            case 6:
                map[self.x+1][self.y]=0
                map[self.x+2][self.y]=3
            case 7:
                map[self.x][self.y-1]=0
                map[self.x][self.y-2]=3
            case 8:
                map[self.x][self.y+1]=0
                map[self.x][self.y+2]=3
            case _:
                return False

    def do_pull(self,map,direction):
        match direction:
            case 9:
                map[self.x-1][self.y]=0
                map[self.x][self.y]=3
                map[self.x+1][self.y]=1
                self.x+=1                        
            case 10:
                map[self.x+1][self.y]=0
                map[self.x][self.y]=3
                map[self.x-1][self.y]=1
                self.x-=1
            case 11:
                map[self.x][self.y-1]=0
                map[self.x][self.y]=3
                map[self.x][self.y+1]=1
                self.y+=1
            case 12:
                map[self.x][self.y+1]=0
                map[self.x][self.y]=3
                map[self.x][self.y-1]=1
                self.y-=1
            case _:
                return False

    def do_move_box(self,map,direction):
        
        match direction:
            case 13:
                map[self.x-1][self.y]=0
                map[self.x+1][self.y]=3
            case 14:
                map[self.x-1][self.y]=0
                map[self.x][self.y-1]=3
            case 15:
                map[self.x-1][self.y]=0
                map[self.x][self.y+1]=3
        
            case 16:
                map[self.x+1][self.y]=0
                map[self.x-1][self.y]=3
            case 17:
                map[self.x+1][self.y]=0
                map[self.x][self.y-1]=3
            case 18:
                map[self.x+1][self.y]=0
                map[self.x][self.y+1]=3
                    
            case 19:
                map[self.x][self.y-1]=0
                map[self.x][self.y+1]=3
            case 20:
                map[self.x][self.y-1]=0
                map[self.x-1][self.y]=3
            case 21:
                map[self.x][self.y-1]=0
                map[self.x+1][self.y]=3
                    
            case 22:
                map[self.x][self.y+1]=0
                map[self.x][self.y-1]=3
            case 23:
                map[self.x][self.y+1]=0
                map[self.x-1][self.y]=3
            case 24:
                map[self.x][self.y+1]=0
                map[self.x+1][self.y]=3
            
            case _:
                return False

    def do(self, map, direction):
        if(direction < 5):
            self.do_move(map, direction)
        elif(direction < 9):
            self.do_move(map, direction)
        elif(direction < 13):
            self.do_move(map, direction)
        else:
            self.do_move(map, direction)
    #fonctions undo
    def undo_move(self,map,direction):
        match direction:
            case 1:
                    self.do_move(map,'S')
            case 2:
                    self.do_move(map,'N')
            case 3:
                    self.do_move(map,'E')
            case 4:
                    self.do_move(map,'O')
            case _:
                return False
        
    def undo_push(self,map,direction):
        match direction:
            case 5:
                map[self.x-1][self.y]=3
                map[self.x-2][self.y]=0
            case 6:
                map[self.x+1][self.y]=3
                map[self.x+2][self.y]=0
            case 7:
                map[self.x][self.y-1]=3
                map[self.x][self.y-2]=0
            case 8:
                map[self.x][self.y+1]=3
                map[self.x][self.y+2]=0
            case _:
                return False

    def undo_pull(self,map,direction):
        match direction:
            case 9:
                map[self.x-2][self.y]=3
                map[self.x-1][self.y]=1
                map[self.x][self.y]=0
                self.x-=1                        
            case 10:
                map[self.x+2][self.y]=3
                map[self.x+1][self.y]=1
                map[self.x][self.y]=0
                self.x+=1
            case 11:
                map[self.x][self.y-2]=3
                map[self.x][self.y-1]=1
                map[self.x][self.y]=0
                self.y-=1
            case 12:
                map[self.x][self.y+2]=3
                map[self.x][self.y+1]=1
                map[self.x][self.y]=0
                self.y+=1
            case _:
                return False

    def undo_move_box(self,map,direction):
        match direction:
            case 13:
                map[self.x-1][self.y]=3
                map[self.x+1][self.y]=0
            case 14:
                map[self.x-1][self.y]=3
                map[self.x][self.y-1]=0
            case 15:
                map[self.x-1][self.y]=3
                map[self.x][self.y+1]=0
        
            case 16:
                map[self.x+1][self.y]=3
                map[self.x-1][self.y]=0
            case 17:
                map[self.x+1][self.y]=3
                map[self.x][self.y-1]=0
            case 18:
                map[self.x+1][self.y]=3
                map[self.x][self.y+1]=0
                    
            case 19:
                map[self.x][self.y-1]=3
                map[self.x][self.y+1]=0
            case 20:
                map[self.x][self.y-1]=3
                map[self.x-1][self.y]=0
            case 21:
                map[self.x][self.y-1]=3
                map[self.x+1][self.y]=0
                    
            case 22:
                map[self.x][self.y+1]=3
                map[self.x][self.y-1]=0
            case 23:
                map[self.x][self.y+1]=3
                map[self.x-1][self.y]=0
            case 24:
                map[self.x][self.y+1]=3
                map[self.x+1][self.y]=0
            
            case _:
                return False

    def undo(self, map, direction):
        if(direction < 5):
            self.undo_move(map, direction)
        elif(direction < 9):
            self.undo_move(map, direction)
        elif(direction < 13):
            self.undo_move(map, direction)
        else:
            self.undo_move(map, direction)

def remplissage(map,nbCarton,agent):
    map[0][0] = 1
    agent.update(0,0)

    #ajout des cartons sur la map et dans la liste
    '''
    for i in range(nbCarton) :
        a = random.randrange(dimX)
        b = random.randrange(dimY)
        
        while map[a][b] != 0:
            a = random.randrange(dimX)
            b = random.randrange(dimY)
        map[a][b] = 3
    '''
    map[1][1] = 3
    
def affiche(map):
    for i in map:
        print(i,"\n")
    print("\n")

def eval_goal(agent):
    if(agent.goal >= agent.nb_goal):
        return 1
    return 0

def check_box(map, agent):
    if(map[agent.outX][agent.outY] == 3):
        agent.goal += 1
        map[agent.outX][agent.outY] = 0

def search_tree(map, agent, solve_actions, save_maps):
    if(map in save_maps):#si on a déjà croisé cette map on stop la recherche
           return 0
    save_maps.append(map)#si on n'a pas croisé la map on l'ajoute à save_maps
    if(eval_goal(agent) == 1):#le but est remplis
        return 1
    actions = agent.action_possible(map)#on récupère la liste des action possibles
    print("Actions : ")
    print(actions, "\n")
    for action in actions:
       agent.do(map, action)#on effectue une action
       print("SEARCH TREE")
       print(" agent x = ", agent.x)
       print(" agent y = ", agent.y)
       print("action = ", action)
       affiche(map)
       print()
       check_box(map, agent)
       solve_actions.append(action)#on ajoute cette action à la liste de la solution
       ret = search_tree(map, agent, solve_actions, save_maps)#appel récursif prochain fils
       if(ret == 1):#on a trouvé une solution (on sort)
           return 1
       agent.undo(map, action)#on défait l'action
       del(solve_actions[-1])
    return 0

def do_solution(map, agent, solve_actions):
    for action in solve_actions:
        do(action)
        affiche(map)

def main():
    solve_actions = []
    save_maps = []
    map = [[0 for x in range(dimX)] for y in range(dimY)]
    agent=Agent()
    remplissage(map,1,agent)
    affiche(map)
    search_tree(map, agent, solve_actions, save_maps)
    do_solution(map, agent, solve_actions)

main()
