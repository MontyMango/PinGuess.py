from random import randrange, choice
from time import sleep


class pin_game:
    def __init__(self):
        # Game Settings
        # Difficulty (0 = easy (5 guesses), 1 = medium (4 guesses), 2 = hard (3 gueses))
        # TODO: Implement a difficulty changer in-game
        self.difficulty = 0

        # Guesses (Will not be saved, change in switchnums() function)
        self.counter = 0

        # win / loss count (Safe to change, but if you do, you are a cheater!)
        self.win = 0
        self.loss = 0
        self.ratio = 0      # win / loss | Don't change to it! You will get divide by 0 error!

        # Guessing strings
        self.n = 0000
        self.correct_num_list = []

        # Input Strings
        self.input_list = []

        # debug (input -1 to activate)
        self.debug_mode_on = False

        # Used for functions
        self.positive_messages = [
            "Wow, you're so good at this!",
            "Yay! Nice job!",
            "Congrats you won! :)"
        ]

        self.loss_messages = [
            "Ah! Darn. You'll get it next time!",
            "Rats!!! That was a hard one. Don't give up! You got the next one!"
        ]

    # DEBUG: Mainly used to tests and input tests on screen while playing
    def toggledebugmode(self):
        if self.debug_mode_on:
            self.debug_mode_on = False
            print("Debug mode off")
        else:
            self.debug_mode_on = True
            print("Debug mode on")


    # Pick a brand new number
    def switchnums(self):
        self.n = randrange(1000, 9999)   # Random number from 1000 - 9999

        if self.debug_mode_on:
            print(self.n)                 # Shows answer- uh I mean shows a random number that has nothing to do with the program :)
        self.n = str(self.n)

        for l in self.n:                # Coverts the number into list
            self.correct_num_list.append(l)
            if self.debug_mode_on:
                print(self.correct_num_list)

        # Difficulty meter (Adjust as needed) 
        if self.difficulty == 0: self.counter = 5
        elif self.difficulty == 1: self.counter = 4
        elif self.difficulty == 2: self.counter = 3
        
        print("Ready to play! If you want to quit, Ctrl + C to exit the game\n\n")


    # This is where the game mainly takes place in this loop.
    def guess(self):
        while (self.counter != 0):
            print("\n\nGuesses Left: " + str(self.counter))
            try:
                inputString = input("Put in pin guess: ")  # Asks for a number

                # Inputs for debugging
                if inputString == "-1":     self.toggledebugmode()
                elif inputString == "-2":   self.show_answer()
                
                # Game functions
                if inputString == "0":      self.changeDifficulty()

                # If the input length is 4
                elif len(inputString) == 4:
                    self.put_into_input_list(inputString)
                    # Check if the list is all integers and then check the guess
                    if(self.check_if_valid_list()):
                        self.check()
                else:
                    print("You need to input a 4 pin number")

            except KeyboardInterrupt:
                print("Thanks for playing!")
                quit()                          # This helped me out with quitting the program: https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script#73673


    # Converts the input into a list
    def put_into_input_list(self, inputList):
        for f in inputList:         # Coverts guess into list
            self.input_list.append(f)
            if self.debug_mode_on:
                print("Input List:", self.input_list)      # Checks if numbers made it on list


    # DEBUG FEATURE: Shows the answer- uh I mean a number that is DEFINITELY NOT the answer
    def show_answer(self):
        if self.debug_mode_on:  print(self.n)
        else:                   print("You cheater! You are not going to get the answer!")


    # Returns win / loss ratio
    def calculate_ratio(self):
        # Prevents divde by 0 error (or the sky from falling) from happening 
        if self.loss == 0:  return self.win / 1
        else:               return self.win / self.loss


    # Chooses a positive message to print out onto the console when the user wins
    def printPositiveMessage(self): print(choice(self.positive_messages) + "\n")


    # Chooses a loss message to print out when the user losses
    def printLossMessage(self):     print(choice(self.loss_messages) + "\n")


    #region Checks if the list is an integer list
    def check_if_valid_list(self):
        for num_in_list in range(0,4):

            if(self.debug_mode_on):
                print("is element " + str(self.input_list[num_in_list]) + " a character?: " + str(self.input_list[num_in_list].isalpha()))

            # Check if the element is a character
            # This helped me out here: https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python
            if (self.input_list[num_in_list].isalpha()):
                if(self.debug_mode_on):
                    print("! - check_if_valid_list breaking out! See ya later!")
                print("You inputted a letter! You must input a number!")
                del self.input_list[0:]     # Clear list
                return False
        return True
    #endregionn


    #region Checks guessed number
    def check(self):
        print("\nResults:")
        try:
            # Check each number to see if the guess is correct!
            total_correct = 0
            for i in range(1, 5):       # Changes number
                number_on_list = i - 1  # TODO: Implement this into the for loop instead of implementing this as a variable.
                                        #       For the life of me, I tried to implement this into the range function and it cannot work.

                if self.correct_num_list[number_on_list] == self.input_list[number_on_list]:
                    print("#", i, " Correct!")
                    total_correct += 1
                elif self.correct_num_list[number_on_list] < self.input_list[number_on_list]:
                    print("#", i, " Less")
                elif self.correct_num_list[number_on_list] > self.input_list[number_on_list]:
                    print("#", i, " More")

                if self.debug_mode_on:
                    print("Total correct so far: " + str(total_correct))

            self.input_list = []        # Erase the entire input list 
            self.counter -= 1           # Counter minus one

            if total_correct == 4:      # If you win
                self.printPositiveMessage()
                sleep(5)
                self.win += 1
                self.score()
                sleep(2)
                print("But lets see if you are good at this one...")
                sleep(1)
                print("Generating new pin...")
                sleep(1)
                self.input_list = [ ]           # deletes guessing list
                self.correct_num_list = [ ]     # deletes automated list
                self.switchnums()

            # If there are no more guesses
            elif self.counter == 0:
                print("Game over...")
                self.printLossMessage()
                sleep(2)
                print("The correct numbers for this is ", self.n)
                sleep(2)
                self.loss += 1
                self.score()
                sleep(3)
                print("Restarting list...")
                self.correct_num_list = [ ]
                self.switchnums()

            # If there are still guesses left, clear the guessing list
            else:
                self.input_list = [ ]      # cleans guessing list
                if self.debug_mode_on:
                    # prints and checks if list is deleted
                    print("List should be empty:", self.input_list)

        # When the user exits during the announcements
        except KeyboardInterrupt:
            print(" ---oh, so you\'re just going to leave while I'm talking? Okay, bye then >:(")
            exit()

        except:
            print("Umm... we don't know what exactly happened...")
            del self.input_list[0:]
    #endregion

    #region Print score
    def score(self):        # Prints scoreboard
        print("\nScoreboard\n", "_"*10, "\n Wins:", self.win,
              "\n Losses:", self.loss, "\n",
               "Ratio:", self.calculate_ratio(), "\n", "_"*10)
    #endregion



while __name__ == '__main__':
  obj = pin_game()
  obj.switchnums()
  obj.guess()
