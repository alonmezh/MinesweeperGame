#################################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Final Game: Minesweeper Classes
#################################################
import pygame

class Smiley(object):

    def __init__(self, x, y, size, screen):
        self.smileyImg = pygame.image.load("smiley.png")
        self.smileyImg = pygame.transform.scale(self.smileyImg,(size,size))
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen

    def draw(self):    
        self.screen.blit(self.smileyImg,(self.x,self.y))
        
    def smileyClicked(self, x, y):
        return x > self.x and x < self.x + self.size and y > self.y and y < self.y + self.size
