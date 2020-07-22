import c4d
from c4d import gui

def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output




def main():
    pcnt = doc.GetSelection()[0].GetPointCount()
    
    for o in get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(c4d.Opoint), []):
        if o.GetPointCount() == pcnt:
            o.SetBit(c4d.BIT_ACTIVE)
        
    
    

# Execute main()
if __name__=='__main__':
    main()