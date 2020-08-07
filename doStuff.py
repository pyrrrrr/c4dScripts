import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    selection  = doc.GetActiveObjects()
    i = 0
    for item in selection:
        l = c4d.BaseObject(c4d.Olight)
        l.InsertUnder(item)
       
        
        
    c4d.EventAdd()
    c4d.DrawViews()
    
if __name__=='__main__':
    main()
