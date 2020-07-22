import c4d
from c4d import gui
#Welcome to the world of Python

def GetNextObject(op):
    if op==None: return None
 
    if op.GetDown(): return op.GetDown()
    while not op.GetNext() and op.GetUp():
        op = op.GetUp() 
    return op.GetNext()

def main():
     
   
    
    all_op   = doc.GetFirstObject()
    toggle = None
    while all_op:
        if all_op.GetType() == 1007455:
            if toggle == None:
                toggle = bool(all_op[c4d.ID_BASEOBJECT_GENERATOR_FLAG])
                
        
            all_op[c4d.ID_BASEOBJECT_GENERATOR_FLAG] =  not toggle
           
        all_op = GetNextObject(all_op)
        
    c4d.EventAdd()

if __name__=='__main__':
    main()
