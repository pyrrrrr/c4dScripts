import c4d
from c4d import gui
from c4d.documents   import GetActiveDocument
from c4d import utils


def create_display_tag(myobject):
    mytag = myobject.MakeTag(c4d.Tdisplay)
    mytag[c4d.DISPLAYTAG_AFFECT_TEXTURES] = 1
    return


def main():

    selection     = doc.GetSelection()
    selection_len = len(selection)
    i = 0
    for item in selection:
        create_display_tag(selection[i])
        i = i + 1
    c4d.EventAdd()
    c4d.DrawViews()

if __name__=='__main__':
    main()
