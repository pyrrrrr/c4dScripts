### postwendend.com ###
### tobias hoffmann ###
### kontakt@postwendend.com ###

import c4d
from c4d import gui
from c4d.documents   import GetActiveDocument
from c4d import utils

def create_new_layer (name):

    layer = c4d.documents.LayerObject()
    layer.SetName(name)
    layerRoot = doc.GetLayerObjectRoot()
    layer.InsertUnder(layerRoot)

def main():

    selection     = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)

    i = 0
    for item in selection:
        layer_name = selection[i].GetName()
        doc.SetSelection(selection[i])
        c4d.CallCommand(100004768)
        c4d.CallCommand(100004809) # Add to New Layer
        new_layer = selection[i][c4d.ID_LAYER_LINK]
        new_layer.SetName(layer_name)
        i = i + 1

if __name__=='__main__':
    main()