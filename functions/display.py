from random import choice

positive_messages = [
    "Wow, you're so good at this!",
    "Yay! Nice job!",
    "Congrats you won! :)"
]

loss_messages = [
    "Ah! Darn. You'll get it next time!",
    "Rats!!! That was a hard one. Don't give up! You got the next one!"
]

# Chooses a positive message to print out onto the console when the user wins
def printPositiveMessage():
    return choice(positive_messages)


# Chooses a loss message to print out when the user losses
def printLossMessage():
    return choice(loss_messages)


# def score(self):        # Prints scoreboard
#     print("\nScoreboard\n", "_"*10, "\n Wins:", self.win,
#             "\n Losses:", self.loss, "\n",
#             "Ratio:", self.calculate_ratio(), "\n", "_"*10)
