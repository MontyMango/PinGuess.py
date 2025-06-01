class scoreboard:
    def __init__(self):
        # Guesses
        self.counter = 0

        # win / loss count (Safe to change, but if you do, you are a cheater!)
        self.win = 0
        self.loss = 0

        # Ratio (caclulated via getWinLossRatio())
        self.ratio = 0

        # debug (input -1 to activate)
        self.debug_mode = False

    def appendCounter(self):
        self.counter += 1
        return True

    def appendWin(self):
        self.win += 1
        return True

    def appendLoss(self):
        self.loss += 1
        return True

    def getWinLossRatio(self):
        return self.ratio

    # win / loss | Don't change to it! You will get divide by 0 error!
    def calculateWinLossRatio(self):
        # Set losses
        if self.loss <= 0:
            losses = 1
        else:
            losses = self.loss

        return True
