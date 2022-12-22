import numpy as np
from random import randint
win_on_start = np.array([7, 11])
lose_on_start = np.array([2, 3, 12])


def roll_dices():
    return randint(1, 6) + randint(1, 6)


def play_game():
    roll = roll_dices()
    if roll in win_on_start:
        return True
    elif roll in lose_on_start:
        return False
    else:
        rolled_values = np.array([roll])
        while True:
            roll = roll_dices()
            if roll == 7:
                return False
            elif roll in rolled_values:
                return True
            # add new roll to rolled_values
            rolled_values = np.append(rolled_values, roll)


# count win-rate using Monte-Carlo method
def monte_carlo(n):
    wins = 0
    for i in range(n):
        if play_game():
            wins += 1
    return wins / n


print("%i" % (monte_carlo(100000) * 100) + '%')