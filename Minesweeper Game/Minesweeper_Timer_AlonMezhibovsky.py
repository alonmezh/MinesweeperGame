#################################################
#Programmer: Alon Mezhibovsky
#Date: I dunno
#File Name: Final Game: Minesweeper Classes
#################################################

import time

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        self.start = 0
        self.running = False
            
    def start_timer(self):
        """Starts the timer"""
        self.start = self.now()
        self.running = True
        return str(self.start)
    
    def stop_timer(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = self.now()
        self.running = False
        return message + str(self.stop - self.start)
    
    def now(self, message="Now: "):
        """Returns the current time with a message"""
        return int(time.time())

    def isRunning(self):
        return self.running 
    
    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        if self.start == 0:
            return ""

        if not self.running:
            return str(self.stop - self.start)
        
        return str(self.now() - self.start)
