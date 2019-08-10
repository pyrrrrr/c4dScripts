import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    bd = doc.GetActiveBaseDraw()
    if bd[c4d.BASEDRAW_DATA_WIREFRAMESELECTION] == 1: bd[c4d.BASEDRAW_DATA_WIREFRAMESELECTION] = 0
    else: bd[c4d.BASEDRAW_DATA_WIREFRAMESELECTION] = 1
    c4d.EventAdd()
    

if __name__=='__main__':
    main()
