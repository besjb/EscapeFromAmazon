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
                self.do_move(room,'2')
            case 2:
                self.do_move(room,'1')
            case 3:
                self.do_move(room,'4')
            case 4:
                self.do_move(room,'3')
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
        print("Undo affiche")
        affiche(room)
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
        affiche(room)
        agent.goal += 1
        room[agent.outX][agent.outY] = 0

def print_info_st(agent, room, action):
    print("\nSEARCH TREE")
    print("=============")
    print("agent.xy : [", agent.x, "]", "[", agent.y, "]")
    print("action = ", action)
    affiche(room)

def search_tree(room, agent, solve_actions, save_rooms, depth):
    if(depth > 2):
        return 0
    if room in save_rooms:#si on a déjà croisé cette room on stop la recherche
        affiche(room)
        return 0
    room_copy = [row[:] for row in room]
    save_rooms.append(room_copy)#si on n'a pas croisé la room on l'ajoute à save_rooms
    if(eval_goal(agent) == 1):#le but est remplis
        return 1
    actions = agent.action_possible(room)#on récupère la liste des action possibles
    for action in actions:
        agent.do(room, action)#on effectue une action
        print_info_st(agent, room, action)
        check_box(room, agent)
        solve_actions.append(action)#on ajoute cette action à la liste de la solution
        ret = search_tree(room, agent, solve_actions, save_rooms, depth+1)#appel récursif prochain fils
        print("Action = ", action)
        print("Liste des action : ", actions);
        agent.undo(room, action)#on défait l'action
        del(solve_actions[-1])
        if(ret == 1):#on a trouvé une solution (on sort)
           return 1
    return 0

def do_solution(room, agent, solve_actions):
    print("SOLUTION :")
    print(solve_actions)
    for action in solve_actions:
        agent.do_move(room, action)
        affiche(room)

def main():
    solve_actions = []
    save_rooms = []
    room = [[0 for x in range(dimX)] for y in range(dimY)]
    agent=Agent()
    remplissage(room,1,agent)
    #affiche(room)
    search_tree(room, agent, solve_actions, save_rooms, 0)
    do_solution(room, agent, solve_actions)

main()
