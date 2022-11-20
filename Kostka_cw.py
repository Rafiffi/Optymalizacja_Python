import random

import numpy as np
import random as r
import matplotlib.pyplot as plt



# dwie kostki i ich rozkład - przypkład dla for loop 



def two_dice_f(x, typ_kostki=6):
    ilosc = list(range(0,x))
    wynik = np.repeat(0,x)
    dice1 = np.repeat(0,x)
    dice2 = np.repeat(0, x)

    for i in ilosc:
        dice1[i] = r.randint(1, typ_kostki)
        dice2[i] = r.randint(1, typ_kostki)
        wynik[i] = dice1[i] + dice2[i]
        i = i + 1
    plt.hist(wynik)
    plt.show()

two_dice_f(1000)





