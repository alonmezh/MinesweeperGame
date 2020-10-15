#################################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Final Game: Minesweeper Classes
#################################################
import pygame
import time
from random import randint
from Minesweeper_Cell_AlonMezhibovsky import Cell
from Minesweeper_Mine_AlonMezhibovsky import Mine
BLOCKSIZE = 24
IMG_BLOCKSIZE = 22
SHIFT = 50
BLACK = (0,0,0)
DARK_GREY = (169,169,169)
RED = (255,0,0)

greyCellImg = pygame.image.load("block.png")
greyCellImg = pygame.transform.scale(greyCellImg,(BLOCKSIZE,BLOCKSIZE))

hiddenImg = pygame.image.load("block.png")
hiddenImg = pygame.transform.scale(hiddenImg,(BLOCKSIZE,BLOCKSIZE)) 

clickblockImg = pygame.image.load("clickblock.png")
clickblockImg = pygame.transform.scale(clickblockImg,(BLOCKSIZE,BLOCKSIZE))


blownMineImg = pygame.image.load("blownblock.jpg")
blownMineImg = pygame.transform.scale(blownMineImg,(BLOCKSIZE,BLOCKSIZE))

notBlownMineImg = pygame.image.load("mineblock.jpg")
notBlownMineImg = pygame.transform.scale(notBlownMineImg,(BLOCKSIZE,BLOCKSIZE))

oneblockImg = pygame.image.load("oneblock.png")
oneblockImg = pygame.transform.scale(oneblockImg,(BLOCKSIZE,BLOCKSIZE))

twoblockImg = pygame.image.load("twoblock.jpg")
twoblockImg = pygame.transform.scale(twoblockImg,(BLOCKSIZE,BLOCKSIZE))

threeblockImg = pygame.image.load("threeblock.jpg")
threeblockImg = pygame.transform.scale(threeblockImg,(BLOCKSIZE,BLOCKSIZE))

fourblockImg = pygame.image.load("fourblock.jpg")
fourblockImg = pygame.transform.scale(fourblockImg,(BLOCKSIZE,BLOCKSIZE))

fiveblockImg = pygame.image.load("fiveblock.jpg")
fiveblockImg = pygame.transform.scale(fiveblockImg,(BLOCKSIZE,BLOCKSIZE))

sixblockImg = pygame.image.load("sixblock.jpg")
sixblockImg = pygame.transform.scale(sixblockImg,(BLOCKSIZE,BLOCKSIZE))

sevenblockImg = pygame.image.load("sevenblock.jpg")
sevenblockImg = pygame.transform.scale(sevenblockImg,(BLOCKSIZE,BLOCKSIZE))

eightblockImg = pygame.image.load("eightblock.jpg")
eightblockImg = pygame.transform.scale(eightblockImg,(BLOCKSIZE,BLOCKSIZE))

         
class Board(object):

    def __init__(self, columns, rows, numberOfMines, screen):
        self.columns = columns
        self.rows = rows
        self.numberOfMines = numberOfMines
        self.numberOfFlagged = 0;
        self.screen = screen
        print("Mines: " + str(numberOfMines))
        ## initialize empty board
        #self.cells = [[Cell(i,j) for j in range(columns)] for i in range(rows)]
        self.initialize()

    def numberOfMinesLeft(self):
        if self.isWin():
            return int(0)
        else:
            return self.numberOfMines - self.numberOfFlagged
    
    def initialize(self):
        self.cells = [[Cell(i,j, self.screen) for j in range(self.columns)] for i in range(self.rows)]
        ##add mines
        for i in range(self.numberOfMines):
            isMine = False
            while not isMine:
                x = randint(0,self.rows-1)
                y = randint(0,self.columns-1)
                isMine = self.cells[x][y].isMine
                if not isMine:
                    self.cells[x][y] = Mine(x,y,self.screen)
                    isMine = True
        ##add mine counter
        self.setMineCounters()
    def isWin(self):
        revealedCount = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j].isRevealed():
                    revealedCount += 1
        return revealedCount == (self.rows*self.columns - self.numberOfMines)

    def isFlaged(self, x,y):
        return self.cells[x][y].isFlaged()
        
    def flag(self, x,y):
        if(self.cells[x][y].isRevealed()):
            return
        self.cells[x][y].flag()
        if self.cells[x][y].isFlaged():
            self.numberOfFlagged += 1
        else:
            self.numberOfFlagged -= 1
        
        
    def reveal(self, x,y, force = False):
        if not force:
            if self.cells[x][y].revealed:
                return
        self.cells[x][y].reveal()
        
        ## now lets reveal surrounding
        if self.cells[x][y].mineCount != 0:
            return
        
        if x > 0:
            #check the above row
            self.reveal(x-1,y)
                            
            if y > 0 :
                self.reveal(x-1,y-1)
                

            if y < self.columns-1 :
                self.reveal(x-1,y+1)

        if x < self.rows-1:
            
            #check the below row
            self.reveal(x+1,y)
            if y > 0 :
                self.reveal(x+1,y-1)
                
            if y < self.columns-1:
                self.reveal(x+1,y+1)

        if y > 0:
            self.reveal(x,y-1)

        if y < self.columns-1:
            self.reveal(x,y+1)

    def isMine(self, x,y):
        return self.cells[x][y].isMine
    
    def draw(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.cells[i][j].draw()

    def revealBoard(self, win = False):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j].isMine and not self.cells[i][j].isFlaged() and win:
                    self.cells[i][j].flag()
                self.cells[i][j].reveal()
                

    def setMineCounters(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j].isMine :
                    mineCount = -1
                else:    
                    self.cells[i][j].mineCount = self.countMines(i,j)
                   ## print("Cell " + str(i) + ":" + str(j) + " - " + str(self.cells[i][j].mineCount))
                    if self.cells[i][j].mineCount == 1:
                        self.cells[i][j].visibleImage = oneblockImg
                    elif self.cells[i][j].mineCount == 2:
                        self.cells[i][j].visibleImage = twoblockImg
                    elif self.cells[i][j].mineCount == 3:
                        self.cells[i][j].visibleImage = threeblockImg
                    elif self.cells[i][j].mineCount == 4:
                        self.cells[i][j].visibleImage = fourblockImg
                    elif self.cells[i][j].mineCount == 5:
                        self.cells[i][j].visibleImage = fiveblockImg
                    elif self.cells[i][j].mineCount == 6:
                        self.cells[i][j].visibleImage = sixblockImg
                    elif self.cells[i][j].mineCount == 7:
                        self.cells[i][j].visibleImage = sevenblockImg
                    elif self.cells[i][j].mineCount == 8:
                        self.cells[i][j].visibleImage = eightblockImg

    def countMines(self, x, y):
        count = 0
        ##count mines
        if x > 0:
            #check the above row
            if self.cells[x-1][y].isMine:
                count += 1
            if y > 0 and self.cells[x-1][y-1].isMine:
                count += 1
            if y < self.columns-1 and self.cells[x-1][y+1].isMine:
                count += 1
        if x < self.rows-1:
            #check the below row
            if self.cells[x+1][y].isMine:
                count += 1
            if y > 0 and self.cells[x+1][y-1].isMine:
                count += 1
            if y < self.columns-1 and self.cells[x+1][y+1].isMine:
                count += 1

        if y > 0 and self.cells[x][y-1].isMine:
           count += 1

        if y < self.columns-1 and self.cells[x][y+1].isMine:
            count += 1
      ##  print(count)   
        return count
                
