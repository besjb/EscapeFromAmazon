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
dimX = 10
dimY = 10
class Agent:
    def __init__(self):
        self.x=0
        self.y=0
        self.actions = []

    def update(self,x,y):
        self.x=x 
        self.y=y 
    

    #fonctions remplissage de la liste des actions possible
    def action_possible(self,map):
        self.actions = []
        self.move(map)
        self.push(map)
        self.pull(map)
        #self.move_box(map)

    def move(self,map):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
            self.actions.append(1)
        if self.x+1 < dimX and map[self.x+1][self.y] == 0:
            self.actions.append(2)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 0:
            self.actions.append(3)
        if self.y+1 < dimY and map[self.x][self.y+1] == 0:
            self.actions.append(4)

    def push(self,map):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
            if self.x-2 >= 0 and map[self.x-2][self.y] == 0 :
                self.actions.append(5)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
            if self.x+2 < dimX and map[self.x+2][self.y] == 0 :
                self.actions.append(6)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
            if self.y-2 >= 0 and map[self.x][self.y-2] == 0 :
                self.actions.append(7)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
            if self.y+2 < dimY and map[self.x][self.y+2] == 0 :
                self.actions.append(8)
                
    def pull(self,map):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
            if self.x+1 <dimX and map[self.x+1][self.y] == 0 :
                self.actions.append(9)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                self.actions.append(10)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
            if self.y+1 <dimY and map[self.x][self.y+1] == 0 :
                self.actions.append(11)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                self.actions.append(12)

    def move_box(self,map):
        if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                self.actions.append(13)
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                self.actions.append(14)
                    #E
            if self.y+1 < dimY and map[self.x][self.y+1] == 0 :
                self.actions.append(15)
        if self.x+1 < dimX and map[self.x+1][self.y] == 3:
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                self.actions.append(16)
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                self.actions.append(17)
                    #E
            if self.y+1 < dimY and map[self.x][self.y+1] == 0 :
                self.actions.append(18)
        if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
                    #E
            if self.y+1 < dimY and map[self.x+1][self.y] == 0 :
                self.actions.append(19)
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                self.actions.append(20)
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                self.actions.append(21)
        if self.y+1 < dimY and map[self.x][self.y+1] == 3:
                    #O
            if self.y-1 >= 0 and map[self.x][self.y-1] == 0 :
                self.actions.append(22)
                    #N
            if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                self.actions.append(23)
                    #S
            if self.x+1 < dimX and map[self.x+1][self.y] == 0 :
                self.actions.append(24)

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
                return false
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
                return false       

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
                return false

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
                return false

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
                return false
        
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
                return false        

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
                return false

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
                return false










def remplissage(map,nbCarton,agent):
    entree = random.randrange(dimX)
    sortie = random.randrange(dimX)

    map[entree][0] = 1
    agent.update(entree,0)
    map[sortie][dimY-1] = 2
    
    #ajout des cartons sur la map et dans la liste
    for i in range(nbCarton) :
        a = random.randrange(dimX)
        b = random.randrange(dimY)
        
        while map[a][b] != 0:
            a = random.randrange(dimX)
            b = random.randrange(dimY)
        map[a][b] = 3
    
def affiche(map):
    for i in map:
        print(i,"\n")
    print("\n")

def main():
    map = [[0 for x in range(dimX)] for y in range(dimY)]
    agent=Agent()
    #remplissage(map,1,agent)
    map[5][5] = 1
    agent.update(5,5)
    map[6][5] = 3

    #murs pour tester move_box
    #map[6][5] = 4
    #map[5][6] = 4
    map[5][4] = 4
    agent.action_possible(map)
    print(agent.actions,"\n")
    affiche(map)
    agent.do_move_box(map,18)
    affiche(map)
    agent.undo_move_box(map,18)
    affiche(map)
    


main()