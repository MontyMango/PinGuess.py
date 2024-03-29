from random import randrange
from time import sleep


class pin_game:
    def __init__(self):
        # Game Settings
        # Guesses (Safe to change)
        self.counter = 5

        # win / loss count (Safe to change, but if you do, you are a cheater!)
        self.win = 0
        self.loss = 0
        self.ratio = 0      # win / loss | Don't change to it! You will get divide by 0 error!

        # Guessing strings
        self.n = 0000
        self.correct_num_list = []

        # Input Strings
        self.inp1 = 0
        self.input_list = []

        # debug (-1 to activate)
        self.debug_mode_on = False


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
            print(self.n)                 # Shows answer
        self.n = str(self.n)

        for l in self.n:                # Coverts number into list
            self.correct_num_list.append(l)
            if self.debug_mode_on:
                print(self.correct_num_list)

        self.counter = 5                # Sets counter back to 5
        print("Ready to play! If you want to quit, hold Ctrl + C to exit the game\n\n")


    # This is where the game mainly takes place in this loop.
    def guess(self):
        while (self.counter != 0):
            print("\n\nGuesses Left: " + str(self.counter))
            try:
                self.inp1 = input("Put in pin guess: ")  # Asks for a number
            except KeyboardInterrupt:
                print("Thanks for playing!")

            if self.inp1 == "-1":
                self.toggledebugmode()
            elif self.inp1 == "-2":
                self.show_answer()
            elif len(self.inp1) == 4:
                self.put_into_input_list()
                if(self.check_if_valid_list()):
                    self.check()
            else:
                print("You need to input a 4 pin number")


    # Converts the input into a list
    def put_into_input_list(self):
        for f in self.inp1:         # Coverts guess into list
            self.input_list.append(f)
            if self.debug_mode_on:
                print("Input List:", self.input_list)      # Checks if numbers made it on list


    # DEBUG FEATURE: Shows the answer
    def show_answer(self):
        if self.debug_mode_on:
            print(self.n)
        else:
            print("You cheater! You are not going to get the answer!")


    # Returns win / loss ratio
    def calculate_ratio(self):
        if self.loss == 0:
            return self.win / 1
        else:
            return self.win / self.loss


    # Checks if the list is an integer list
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
            


    # Checks the guessed number
    def check(self):
        print("\nResults:")
        try:
            total_correct = 0
            for i in range(1, 5):    # Changes number
                number_on_list = i - 1

                if self.correct_num_list[number_on_list] == self.input_list[number_on_list]:
                    print("#", i, " Correct!")
                    total_correct += 1
                elif self.correct_num_list[number_on_list] < self.input_list[number_on_list]:
                    print("#", i, " Less")
                elif self.correct_num_list[number_on_list] > self.input_list[number_on_list]:
                    print("#", i, " More")

                if self.debug_mode_on:
                    print("Correct so far... " + str(total_correct))

            self.input_list = []        # Erase the entire input list 
            self.counter -= 1           # Counter minus one

            if total_correct == 4:      # If you win
                print("\nWow, you're so good at this.")
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

            elif self.counter == 0:   # If the guesses run out
                print("Game over...")
                sleep(2)
                print("The correct numbers for this is ", self.n)
                sleep(2)
                self.loss += 1
                self.score()
                sleep(3)
                print("Restarting list...")
                self.correct_num_list = [ ]
                self.switchnums()

            else:
                self.input_list = [ ]      # cleans guessing list
                if self.debug_mode_on:
                    # prints and checks if list is deleted
                    print("List should be empty:", self.input_list)

        # User didn't put enough numbers for the pin
        # guess() should now handle this error
        # This is left in here just in case if some error were to happen internally
        except IndexError:
            print("\nPlease use a 4 number guess.\n")
            # deletes input guessing list to start a new one
            del self.input_list[0:]

        # User wants to quit
        except KeyboardInterrupt:
            print("\nThanks for playing!")

        except:
            print("We don't know what happened...")
            del self.input_list[0:]



    def score(self):        # Prints scoreboard
        print("\nScoreboard\n", "_"*10, "\n Wins:", self.win,
              "\n Losses:", self.loss, "\n",
               "Ratio:", self.calculate_ratio(), "\n", "_"*10)



while __name__ == '__main__':
  obj = pin_game()
  obj.switchnums()
  obj.guess()
