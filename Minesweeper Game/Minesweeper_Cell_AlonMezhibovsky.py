###############################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Minesweeper Template
###############################################

import pygame

class Cell(object):
    BLOCKSIZE = 24
    SHIFT = 50
    flagblockImg = pygame.image.load("flagblock.png")
    flagblockImg = pygame.transform.scale(flagblockImg,(BLOCKSIZE,BLOCKSIZE))
    greyCellImg = pygame.image.load("block.png")
    greyCellImg = pygame.transform.scale(greyCellImg,(BLOCKSIZE,BLOCKSIZE))
    clickblockImg = pygame.image.load("clickblock.png")
    clickblockImg = pygame.transform.scale(clickblockImg,(BLOCKSIZE,BLOCKSIZE))


    def __init__(self,x,y,screen, hiddenImage = None, visibleImage=None, isMine = False):

        self.hiddenImage = hiddenImage
        if self.hiddenImage == None:
            self.hiddenImage = self.greyCellImg
            
        self.visibleImage = visibleImage
        if self.visibleImage == None:
            self.visibleImage = self.clickblockImg
        
        
        self.x = x * self.BLOCKSIZE
        self.y = y * self.BLOCKSIZE + self.SHIFT
        self.isMine = isMine
        self.mineCount = 0
        self.revealed = False
        self.flaged = False
        self.screen = screen

    def draw(self):
        if self.flaged:
            self.screen.blit(self.flagblockImg,(self.x,self.y)) 
        elif self.revealed:
            self.screen.blit(self.visibleImage,(self.x,self.y))
        else:
            self.screen.blit(self.hiddenImage,(self.x,self.y))

    def isRevealed(self):
        return self.revealed

    def isFlaged(self):
        return self.flaged
        
    def reveal(self):
        if not self.flaged:
            self.revealed = True
            self.flaged = False

    def flag(self):
        if not self.revealed:
            self.flaged = not self.flaged
    
    def isSafe(self):
        return self.mineCount > -1
