#################################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Final Game: Minesweeper Classes
#################################################
import pygame
from Minesweeper_Cell_AlonMezhibovsky import *

BLOCKSIZE = 24
greyCellImg = pygame.image.load("block.png")
greyCellImg = pygame.transform.scale(greyCellImg,(BLOCKSIZE,BLOCKSIZE))
blownMineImg = pygame.image.load("blownblock.jpg")
blownMineImg = pygame.transform.scale(blownMineImg,(BLOCKSIZE,BLOCKSIZE))

class Mine(Cell):
    def __init__(self,x,y,screen, hiddenImage = greyCellImg, visibleImage = blownMineImg):
        Cell.__init__(self, x,y,screen, hiddenImage, visibleImage, True)
        Cell.mineCount = -1
        
