import  c4d
import random
from    c4d.documents   import GetActiveDocument

def GetNextObject(op):
    if op==None: return None

    if op.GetDown(): return op.GetDown()
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
    return op.GetNext()

def main():


    doc  = GetActiveDocument()

    all_op   = doc.GetFirstObject()

    while all_op:

        r_ran = random.random()
        g_ran = random.random()
        b_ran = random.random()

        white = (c4d.Vector(1.0, 1.0, 1.0))
        color = (c4d.Vector(r_ran, g_ran,b_ran))


        if all_op.GetType()== c4d.Onull:
            all_op[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 1

        if all_op[c4d.ID_LAYER_LINK]:
            curr_layer =  all_op[c4d.ID_LAYER_LINK]
            color_layer = curr_layer[c4d.ID_LAYER_COLOR]
            color = color * 0.2 + color_layer * 0.8
            if all_op.GetType()==  1018544: #mograph cloner
                all_op[c4d.ID_MG_TRANSFORM_COLOR] = color
        else:
            color = color * 0.4 + white * 0.6

            if all_op.GetType()==  1018544: #mograph cloner
                all_op[c4d.ID_MG_TRANSFORM_COLOR] = color

        all_op[c4d.ID_BASEOBJECT_COLOR] = color
        all_op[c4d.ID_BASEOBJECT_USECOLOR] = 1
        all_op = GetNextObject(all_op)

    c4d.EventAdd()


if __name__=='__main__':
    main()