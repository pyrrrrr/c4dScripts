import c4d
from c4d import gui

def main():

    obj = doc.GetFirstObject()
    if not obj: return True
    doc.StartUndo()
    olist = []
    while obj:
        olist.append([-obj.GetMg().off.z,obj])
        obj = obj.GetNext()

    olist.sort()
    olist.reverse()

    for i,o in enumerate(olist):
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,o[1])
        o[1].Remove()
        doc.InsertObject(o[1],None,None)

    c4d.EventAdd()
    doc.EndUndo()

if __name__=='__main__':
    main()