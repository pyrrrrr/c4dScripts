import c4d


def main():
    selection = doc.GetSelection()
    doc.StartUndo()  
    
    for item in selection:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,item)
        
        sec = c4d.utils.SendModelingCommand(command=c4d.MCOMMAND_SPLIT,list=[item],mode=c4d.MODELINGCOMMANDMODE_POLYGONSELECTION,doc=doc)
             
        if not sec: return                     
        sec[0].InsertUnder(op)
        
        #delete the polygons from selectiontag
        c4d.utils.SendModelingCommand(command=c4d.MCOMMAND_DELETE,list=[item],mode=c4d.MODELINGCOMMANDMODE_POLYGONSELECTION,doc=doc)
       
        sec[0].SetMl(c4d.Matrix())
        c4d.CallCommand(100004773)
        c4d.CallCommand(14039)
        
        
    doc.EndUndo()
    
    c4d.EventAdd(c4d.EVENT_ENQUEUE_REDRAW)      
    
    

if __name__=='__main__':
    main()
