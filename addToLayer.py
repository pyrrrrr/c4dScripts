### postwendend.com ###
### tobias hoffmann ###
### kontakt@postwendend.com ###

import c4d
from c4d import gui
from c4d.documents   import GetActiveDocument
from c4d import utils

def main():

    for op in doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE):
        layer_name = op.GetName()
        doc.SetSelection(op)
        c4d.CallCommand(100004768) # Select Children
        c4d.CallCommand(100004809) # Add to New Layer
        newLayer = op[c4d.ID_LAYER_LINK]
        newLayer.SetName(layer_name)

if __name__=='__main__':
    main()