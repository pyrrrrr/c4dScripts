import c4d

def main():
    doc.StartUndo()  
    selection = doc.GetSelection()
    
    i = 0
    for item in selection:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,item)
        bs = op.GetPointS()
        sel = bs.GetAll(op.GetPointCount())
        np = []
        yPos = 0
        yList = []
        
        for index, selected in enumerate(sel):
            if selected:
                v = item.GetPoint(index)
                yList.append(v.y)
        
        
        yPos = (min(yList)+max(yList))/2.0
                
        for index, selected in enumerate(sel):
            if not selected:
                np.append(item.GetPoint(index))
            else:
                v = item.GetPoint(index)
                np.append(c4d.Vector(v.x,yPos,v.z))
        
  
        item.SetAllPoints(np)
        item.CreatePhongNormals()
        c4d.CallCommand(14039)
        c4d.EventAdd(c4d.EVENT_ENQUEUE_REDRAW)
    
    
    doc.EndUndo()
    
if __name__=='__main__':
    main()
