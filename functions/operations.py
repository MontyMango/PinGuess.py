from random import randrange

class gameplayNumber:
    def __init__(self):
        self.number = 0
        self.correct_num_list = []
        self.debug_mode = False

        # Game Settings
        self.difficulty = 0


    def generateNewNumber(self):
        self.number = randrange(1000, 9999)

        if self.debug_mode:
            print(self.number)

        # Coverts the number into list
        for l in str(self.number):
            self.correct_num_list.append(l)
            if self.debug_mode:
                print(self.correct_num_list)


    def getDifficulty(self):
        """ Difficulties:
        - 0 = easy (5 guesses)
        - 1 = medium (4 guesses)
        - 2 = hard (3 gueses))
        """
        return self.difficulty
    

    def setDifficulty(self, newDifficulty):
        if newDifficulty in [0, 1, 2]:
            self.difficulty = newDifficulty
            return True
        else:
            return False
