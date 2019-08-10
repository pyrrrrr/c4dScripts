import c4d
from c4d import gui
import random

#Welcome to the world of Python


def main():
    bd = doc.GetActiveBaseDraw()
    bd[c4d.BASEDRAW_DATA_TINTBORDER_OPACITY] = 0.5
    bd[c4d.BASEDRAW_DATA_TINTBORDER_COLOR] = c4d.Vector(random.random(),random.random(),random.random())
    bd[c4d.BASEDRAW_DATA_TINTBORDER] = not bd[c4d.BASEDRAW_DATA_TINTBORDER]
    
    c4d.EventAdd()
if __name__=='__main__':
    main()
