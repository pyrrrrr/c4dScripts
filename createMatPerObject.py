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
        

        if all_op.GetType() == 5100:

            if all_op[c4d.ID_LAYER_LINK] != None:

                r = random.uniform(0.5,1)
                g = random.uniform(0.5,1)
                b = random.uniform(0.5,1)
                
                opName = all_op.GetName()
                
                newMat = c4d.BaseMaterial(c4d.Mmaterial)
                newMat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(r,g,b)
                newMat.SetName(opName)
                doc.InsertMaterial(newMat)
                
                tag = all_op.MakeTag(c4d.Ttexture)
                tag[c4d.TEXTURETAG_MATERIAL] = newMat


        all_op = GetNextObject(all_op)

        
main()