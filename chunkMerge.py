import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    bs = c4d.BaseSelect()
    obj = doc.GetFirstObject()
    chunk = 0
    i = 0 
    while obj:
        i+=1
        obj = obj.GetNext()
    obj = doc.GetFirstObject()
    j = 0
    save = 0
        
    while obj:
        
        j+=1
        if chunk < 256:            
            doc.SetActiveObject(obj,c4d.SELECTION_ADD)
            chunk += 1
        else:
            save += 1
            c4d.CallCommand(16768)
            print 100.0/float(i)*j, i,j
            doc.SetActiveObject(obj)
            chunk = 0
            
        if save == 8:
            save = 0
            c4d.documents.SaveDocument(doc,doc.GetDocumentName(),c4d.SAVEDOCUMENTFLAGS_0,c4d.FORMAT_C4DEXPORT)
        obj = obj.GetNext()
        

if __name__=='__main__':
    main()
