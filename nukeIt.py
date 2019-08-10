import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    selection     = doc.GetSelection()
    i = 0
    
    minTime = doc.GetMinTime()
    maxTime = doc.GetMaxTime()
    
    print minTime.GetFrame(doc.GetFps())
    print maxTime.GetFrame(doc.GetFps())
    
    for t in range (minTime.GetFrame(doc.GetFps()),maxTime.GetFrame(doc.GetFps())):
        
        frame = c4d.BaseTime(t/float(doc.GetFps()))
        
        for item in selection:
            
            trackPos = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, item.GetType()))
            trackRot = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, item.GetType()))
            
            xPos = item.GetVectorTracks(trackPos)[1].GetValue(doc,frame)
            yPos = item.GetVectorTracks(trackPos)[2].GetValue(doc,frame)
            zPos = item.GetVectorTracks(trackPos)[3].GetValue(doc,frame)
            
            xRot = item.GetVectorTracks(trackRot)[1].GetValue(doc,frame)
            yRot = item.GetVectorTracks(trackRot)[2].GetValue(doc,frame)
            zRot = item.GetVectorTracks(trackRot)[3].GetValue(doc,frame)
            
            print xPos,yPos,zPos
            print xRot,yRot,zRot
            
            
            
            #print item.GetVectorTracks(trackRot)
    
    
        
        
    c4d.EventAdd()
    c4d.DrawViews()
    
if __name__=='__main__':
    main()
