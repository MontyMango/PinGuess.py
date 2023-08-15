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

        # Guessing strings
        self.n = 0000
        self.lst = []

        # Input Strings
        self.inp1 = 0
        self.lst1 = []

        # debug (-1 to activate)
        self.debug_mode_on = False

        # self.ratio = self.win / self.loss

    def toggledebugmode(self):
        if self.debug_mode_on:
            self.debug_mode_on = False
            print("Debug mode off")
        else:
            self.debug_mode_on = True
            print("Debug mode on")

    def switchnums(self):
        self.n = randrange(1000, 9999)   # Random number from 1000 - 9999

        if self.debug_mode_on:
            print(self.n)                 # Shows answer
        self.n = str(self.n)

        for l in self.n:                # Coverts number into list
            self.lst.append(l)
            if self.debug_mode_on:
                print(self.lst)

        self.counter = 5                # Sets counter back to 5
        print("Ready to play! If you want to quit, do Ctrl + C to exit the game\n\n")

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
                self.put_num_into_list()
                self.check()
            else:
                print("You need to input a 4 pin number")

    def put_num_into_list(self):
        for f in self.inp1:         # Coverts guess into list
            self.lst1.append(f)
            if self.debug_mode_on:
                print(self.lst1)      # Checks if numbers made it on list

    def show_answer(self):
        if self.debug_mode_on:
            print(self.n)
        else:
            print("You cheater! You are not going to get the answer!")

    # Checks the guessed number

    def check(self):
        print("\nResults:")
        try:
            total_correct = 0
            for i in range(1, 5):    # Changes number
                number_on_list = i - 1

                if self.lst[number_on_list] == self.lst1[number_on_list]:
                    print("#", i, " Correct!")
                    total_correct += 1
                elif self.lst[number_on_list] < self.lst1[number_on_list]:
                    print("#", i, " Less")
                elif self.lst[number_on_list] > self.lst1[number_on_list]:
                    print("#", i, " More")

                if self.debug_mode_on:
                    print(total_correct)

            del self.lst1[0:]
            self.counter -= 1         # Counter minus one

            if total_correct == 4:  # If you win
                print("\nWow, you're so good at this.")
                sleep(5)
                self.win += 1
                self.score()
                sleep(2)
                print("But lets see if you are good at this one...")
                sleep(1)
                print("Generating new pin...")
                sleep(1)
                del self.lst1[0:4]    # deletes guessing list
                del self.lst[0:4]     # deletes automated list
                self.switchnums()

            elif self.counter == 0:   # If you run out of guesses
                print("Game over...")
                sleep(2)
                print("The correct numbers for this is ", self.n)
                sleep(2)
                self.loss += 1
                self.score()
                sleep(3)
                print("Restarting list...")
                del self.lst[0:4]
                self.switchnums()

            else:
                del self.lst1[0:4]      # deletes guessing list
                if self.debug_mode_on:
                    # prints and checks if list is deleted
                    print(self.lst1)

        # User didn't put enough numbers for the pin
        # guess() should now handle this error
        # This is left in here just in case if some error were to happen internally
        except IndexError:
            print("\nPlease use a 4 number guess.\n")
            # deletes input guessing list to start a new one
            del self.lst1[0:]

        # User wants to quit
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            exit

        except:
            print("We don't know what happened...")

    def score(self):        # Prints scoreboard
        print("\nScoreboard\n", "_"*10, "\n Wins:", self.win,
              "\n Losses:", self.loss, "\n", "_"*10)



while __name__ == '__main__':
  obj = pin_game()
  obj.switchnums()
  obj.guess()
