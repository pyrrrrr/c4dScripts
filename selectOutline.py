import c4d

def GetEdgePoints(op, i):
    global polygons
    
    polygonindex = i/4    
    edgeindex = i-polygonindex*4
    
    poly = polygons[polygonindex]
    
    if   edgeindex == 0: return poly.a, poly.b
    elif edgeindex == 1: return poly.b, poly.c
    elif edgeindex == 2: return poly.c, poly.d
    elif edgeindex == 3: return poly.d, poly.a
    
    
def main():    
    global polygons
    polygons = op.GetAllPolygons()
    
    if not op or not op.CheckType(c4d.Opolygon): return

    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_CHANGE_SELECTION, op)
        
    neighbors = c4d.utils.Neighbor()
    neighbors.Init(op)
    
    edgeselection = op.GetEdgeS()
    edgeselection.DeselectAll()
    
    polygonselection = op.GetPolygonS()
    
    
    for i in xrange(op.GetPolygonCount()*4):        
       
        point1, point2 = GetEdgePoints(op, i)
        face1,  face2  = neighbors.GetEdgePolys(point1, point2)
        if polygonselection.IsSelected(face1) ^ polygonselection.IsSelected(face2): edgeselection.Select(i)
        
           
    doc.EndUndo()
    doc.SetMode(c4d.Medges)   
    c4d.EventAdd()
    
    


if __name__=='__main__':
    main()