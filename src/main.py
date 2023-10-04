#!/usr/bin/env python3

#agent = 1
#sortie = 2
#carton = 3
import random
import os

dimX = 10
dimY = 10
class Agent:
    def __init__(self):
        self.x=0
        self.y=0

    def update(self,x,y):
        self.x=x 
        self.y=y 

    def move(self,map,direction):
        map[self.x][self.y]=0
        match direction:
            case 'N':
                if self.x-1 >= 0 and map[self.x-1][self.y] == 0 :
                    self.x-=1
            case 'S':
                if self.x+1 < dimX and map[self.x+1][self.y] == 0:
                    self.x+=1
            case 'O':
                if self.y-1 >= 0 and map[self.x][self.y-1] == 0:
                    self.y-=1
            case 'E':
                if self.y+1 < dimY and map[self.x][self.y+1] == 0:
                    self.y+=1
            case _:
                return false
        map[self.x][self.y]=1

    def push(self,map,direction):
        match direction:
            case 'N':
                if self.x-1 >= 0 and map[self.x-1][self.y] == 3 :
                    if self.x-2 >= 0 and map[self.x-2][self.y] == 0 :
                        map[self.x-1][self.y]==0
                        map[self.x-2][self.y]==3
            case 'S':
                if self.x+1 < dimX and map[self.x+1][self.y] == 3:
                    if self.x+2 >= 0 and map[self.x+2][self.y] == 0 :
                        map[self.x+1][self.y]==0
                        map[self.x+2][self.y]==3
            case 'O':
                if self.y-1 >= 0 and map[self.x][self.y-1] == 3:
                    if self.y-2 >= 0 and map[self.x][self.y-2] == 0 :
                        map[self.x][self.y-1]==0
                        map[self.x][self.y-2]==3
            case 'E':
                if self.y+1 < dimY and map[self.x][self.y+1] == 3:
                    if self.y+2 >= 0 and map[self.x][self.y+2] == 0 :
                        map[self.x][self.y+1]==0
                        map[self.x][self.y+2]==3
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
    remplissage(map,1,agent)
    affiche(map)
    agent.move(map,'N')
    agent.move(map,'E')
    affiche(map)

    


main()