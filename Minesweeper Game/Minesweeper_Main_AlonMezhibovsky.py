###############################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Minesweeper Template
###############################################
from Minesweeper_Board_AlonMezhibovsky import *
from Minesweeper_Timer_AlonMezhibovsky import Timer
from Minesweeper_Smiley_AlonMezhibovsky import Smiley
from random import randint
import pygame
pygame.init()

class Main(object):
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    BLOCKSIZE = 24
    IMG_BLOCKSIZE = 22
    SHIFT = 50
    BOARD_HEIGHT = 20
    BOARD_WIDTH = 20
    SMILEY_SIZE = 30
    smiley_x = BOARD_WIDTH*BLOCKSIZE/2 - SMILEY_SIZE/2
    smiley_y = SHIFT/2 - SMILEY_SIZE/2
    DARK_GREY = (169,169,169)
    RED = (255,0,0)
    BLACK = (0,0,0)
    def __init__(self):
        pygame.display.set_caption ("Minesweeper")
        self.font = pygame.font.SysFont("Arial",15)
        self.screen = pygame.display.set_mode((self.BOARD_WIDTH*self.BLOCKSIZE,self.BOARD_HEIGHT*self.BLOCKSIZE + self.SHIFT))
        self.board = Board(self.BOARD_HEIGHT, self.BOARD_WIDTH, self.getNumberOfMinesBySize(), self.screen)
        self.smileyMiddle = Smiley(self.smiley_x, self.smiley_y, self.SMILEY_SIZE, self.screen)
        self.smileyBig = Smiley(self.smiley_x + self.SMILEY_SIZE+6, self.smiley_y-3, int(self.SMILEY_SIZE*1.2), self.screen)
        self.smileySmall = Smiley(self.smiley_x-self.SMILEY_SIZE , self.smiley_y+3, int(self.SMILEY_SIZE*0.8), self.screen)
        self.timeClass = Timer()
        
    def getNumberOfMinesBySize(self):
        return self.BOARD_HEIGHT*self.BOARD_WIDTH//8

    def getSmileyPosition(self):
        return [self.BOARD_WIDTH*self.BLOCKSIZE/2 - self.SMILEY_SIZE/2, self.SHIFT/2 - self.SMILEY_SIZE/2]
    
    def run(self):
        inPlay = True
        allowedToClick = True

        while inPlay:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inPlay = False
                if allowedToClick and event.type == pygame.MOUSEBUTTONUP and event.button==self.RIGHT_BUTTON:
                    coordiantes = self.getBoardCoordinates()
                    if y >= 0 and x >= 0 : 
                        self.board.flag(coordiantes[0], coordiantes[1])
                    print("Mines left: " + str(self.board.numberOfMinesLeft()))
                if allowedToClick and event.type == pygame.MOUSEBUTTONUP and event.button==self.LEFT_BUTTON:
                    coordiantes = self.getBoardCoordinates()
                    x = coordiantes[0]
                    y = coordiantes[1]
            
                    if y >= 0 and x >= 0 : 
                        if not self.timeClass.isRunning():
                            self.timeClass.start_timer()
                        
                        if self.board.isMine(x,y):
                            if not self.board.isFlaged(x,y):
                                self.board.revealBoard()
                                print("Game over. You loose.")                    
                                allowedToClick = False
                                self.timeClass.stop_timer()
                        else:
                            self.board.reveal(x, y, True)
                            if self.board.isWin():
                                print("You WON!")   
                                self.board.revealBoard(True)
                                allowedToClick = False
                                self.timeClass.stop_timer()

                if event.type == pygame.MOUSEBUTTONUP and event.button == self.LEFT_BUTTON and allowedToClick == False:
                    print("New Game")
                    coordinates = pygame.mouse.get_pos()
                    if self.smileyMiddle.smileyClicked(coordinates[0], coordinates[1]):
                        self.initDisplay(20, 20)
                        allowedToClick = True
                    if self.smileyBig.smileyClicked(coordinates[0], coordinates[1]):
                        self.initDisplay(30, 25)
                        allowedToClick = True
                    if self.smileySmall.smileyClicked(coordinates[0], coordinates[1]):
                        self.initDisplay(10,10)
                        allowedToClick = True
                        
            self.redraw_screen()
            pygame.time.delay(200)
        pygame.quit()

    def initDisplay(self, width, height):
        self.BOARD_HEIGHT = height
        self.BOARD_WIDTH = width
        pos = self.getSmileyPosition()
        self.smileyMiddle.x = pos[0]
        self.smileyMiddle.y = pos[1]
        self.smileySmall.x = pos[0]-self.SMILEY_SIZE
        self.smileySmall.y = pos[1]+3
        self.smileyBig.x = pos[0]+self.SMILEY_SIZE+6
        self.smileyBig.y = pos[1]-3
        self.screen = pygame.display.set_mode((self.BOARD_WIDTH*self.BLOCKSIZE,self.BOARD_HEIGHT*self.BLOCKSIZE + self.SHIFT))
        self.board = Board(height, width, self.getNumberOfMinesBySize(), self.screen)
 
    def redraw_screen(self):
        self.screen.fill(self.DARK_GREY)
        self.smileySmall.draw()
        self.smileyMiddle.draw()
        self.smileyBig.draw()
        self.board.draw()    
        mineText = self.font.render("Mines Left:",1,self.BLACK)
        mineText2 = self.font.render(str(self.board.numberOfMinesLeft()),1,self.RED)
        self.screen.blit(mineText, (10,10))
        self.screen.blit(mineText2, (25,25))
        timeText = self.font.render("Time: "+ self.timeClass.elapsed(),1,self.BLACK)
        self.screen.blit(timeText,(self.BOARD_WIDTH*self.BLOCKSIZE-60,10))
        pygame.display.update()

    def getBoardCoordinates(self):
        (x,y)=pygame.mouse.get_pos()
        x = x//self.BLOCKSIZE
        if y >= self.SHIFT:
            y = (y-self.SHIFT)//self.BLOCKSIZE
        else:
            y = -1
        return [x,y]

if __name__ == '__main__':
    Main().run()
