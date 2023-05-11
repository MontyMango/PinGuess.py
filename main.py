from random import randrange
from time import sleep

class pin():
    def __init__(self):
        # Game Settings
        # Guesses (Safe to change)
        self.counter = 5
        
        # win / loss count (Safe to change, but if you do, you are a cheater!)
        self.win = 0
        self.loss = 0
        
        # Guessing strings
        self.n = 0000
        self.lst = []

        # Input Strings
        self.inp1 = 0
        self.lst1 = []

        # Correct numbers
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0

        # for the Checker
        self.nmbr = 0

        # debug (-1 to activate)
        self.dbg = 0


        # self.ratio = self.win / self.loss

    def toggledebugmode(self):
      if self.dbg == 0:
        self.dbg = 1
        print("Debug mode on")
      elif self.dbg == 1:
        self.dbg = 0
        print("Debug mode off")
      self.guess()

    def switchnums(self):
        self.n = randrange(1000,9999)   # Random number from 1000 - 9999
        
        if self.dbg == 1:
          print(self.n)                   # Shows random number
        self.n = str(self.n)
        
        for l in self.n:                # Coverts number into list
          self.lst.append(l)
          if self.dbg == 1:
            print(self.lst)
        self.counter = 5                # Sets counter back to 5
        print("Ready to play!\n\n")
        self.guess()

    def guess(self):
        self.inp1 = input("\nPut in pin guess: ")  # Asks for a number
        if self.inp1 == "-1":
          self.toggledebugmode()
        for f in self.inp1:         # Coverts guess into list
            self.lst1.append(f)
            if self.dbg == 1:
              print(self.lst1)      # Checks if numbers made it on list
        self.check()

    # Checks the guessed number
    def check(self):
      print("\nResults:")
      try:
        for i in range(0,4):    # Changes number
          if i == 0: self.nmbr = self.n1
          elif i == 1: self.nmbr = self.n2
          elif i == 2: self.nmbr = self.n3
          elif i == 3: self.nmbr = self.n4
          if self.lst[i] == self.lst1[i]:
            print("#",i+1," Correct!")
            self.nmbr = 1
          elif self.lst[i] < self.lst1[i]:
            print("#",i+1," Less")
            self.nmbr = 0
          elif self.lst[i] > self.lst1[i]:
            print("#",i+1," More")
            self.nmbr = 0
          if i == 0: self.n1 = self.nmbr
          elif i == 1: self.n2 = self.nmbr
          elif i == 2: self.n3 = self.nmbr
          elif i == 3: self.n4 = self.nmbr

        del self.lst1[0:]
        self.counter-=1         # Counter minus one


        if self.n1 and self.n2 and self.n3 and self.n4 == 1:  # If you win
          print("\nWow, you're so good at this.")
          sleep(5)
          self.win+=1
          self.score()
          sleep(2)
          print("But lets see if you are good at this one...")
          sleep(1)
          print("Generating new pin...")
          sleep(1)
          del self.lst1[0:4]    # deletes guessing list
          del self.lst[0:4]     # deletes automated list
          self.switchnums()

        if self.counter == 0:   # If you run out of guesses
          print("Game over...")
          sleep(2)
          print("The correct numbers for this is ",self.n)
          sleep(2)
          self.loss+=1
          self.score()
          sleep(3)
          print("Restarting list...")
          del self.lst[0:4]
          self.switchnums()
        else:
          del self.lst1[0:4]      # deletes guessing list
          if self.dbg == 1:
            print(self.lst1)        # prints and checks if list is deleted
          self.guess()          # If not, take another guess
      except IndexError:
        print("\nPlease use a 4 number guess.\n")
        del self.lst1[0:]   # deletes input guessing list to start a new one
        self.guess()
      except:
        print("We don't know what happened...")
        self.guess()

    def score(self):        # Prints scoreboard
        print("\nScoreboard\n","_"*10,"\n Wins:",self.win,"\n Losses:",self.loss,"\n","_"*10)


obj = pin()
obj.switchnums()
