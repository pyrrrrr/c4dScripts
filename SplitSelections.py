import c4d


def main():
    
    selection = doc.GetSelection()    
    doc.StartUndo()  
    doc.AddUndo(c4d.UNDOTYPE_DELETE,selection[0])
    tag = selection[0].GetFirstTag()
    
    while tag:
        rmTag = []
        matName = None
        
        if tag.GetType() == c4d.Tpolygonselection:
            
            #deselect current polygonselection
            polyselection = op.GetPolygonS()
            polyselection.DeselectAll()
        
            #select polygons from selectiontag
            tagselection  =  tag.GetBaseSelect()
            tagselection.CopyTo(polyselection)
          
            sec = c4d.utils.SendModelingCommand(command=c4d.MCOMMAND_SPLIT,list=[selection[0]],mode=c4d.MODELINGCOMMANDMODE_POLYGONSELECTION,doc=doc)
            matTag = sec[0].GetFirstTag()
            while matTag:
                if matTag.GetType() == c4d.Ttexture:                   
                    if matTag[c4d.TEXTURETAG_RESTRICTION] == tag[c4d.ID_BASELIST_NAME]:
                        matTag[c4d.TEXTURETAG_RESTRICTION] = ""
                        matName = matTag.GetMaterial()[c4d.ID_BASELIST_NAME]
                    else:
                        rmTag.append(matTag)
                elif matTag.GetType() == c4d.Tpolygonselection:
                    
                    rmTag.append(matTag)
                matTag = matTag.GetNext()
            
            for t in rmTag:
                t.Remove()
            
            sec[0][c4d.ID_BASELIST_NAME] += "_" + matName
            if not sec: return                     
            sec[0].InsertAfter(op)
            doc.AddUndo(c4d.UNDOTYPE_NEW,sec[0])
            
            #delete the polygons from selectiontag
            c4d.utils.SendModelingCommand(command=c4d.MCOMMAND_DELETE,list=[selection[0]],mode=c4d.MODELINGCOMMANDMODE_POLYGONSELECTION,doc=doc)

        tag = tag.GetNext()

    selection[0].Remove()    
    doc.EndUndo()    
    c4d.EventAdd(c4d.EVENT_ENQUEUE_REDRAW)      
    
    

if __name__=='__main__':
    main()
