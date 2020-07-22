import c4d
from c4d import gui
import winsound
import os
import random

#Welcome to the world of Python


def main():
    p = "X:\\Temp\\Tobi3d\\Soundboard\\"
    s = os.listdir(p)    
    random.shuffle(s)
    winsound.PlaySound(p+s[0], winsound.SND_FILENAME | winsound.SND_ASYNC)


if __name__=='__main__':
    main()