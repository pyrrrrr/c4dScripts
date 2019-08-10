import c4d
from c4d import gui


def get_all_objects(op, filter, output):
    while op:
        if filter(op): output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

def main():
    bd = doc.GetActiveBaseDraw()
    cam = bd.GetSceneCamera(doc)
    szeneCam = cam.GetDocument()
    
    cams = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(c4d.Ocamera), [])
    menu = c4d.BaseContainer()
    
    
    
    if szeneCam: 
        
        editCam = bd.GetEditorCamera()        
        editCam.SetData(cam.GetData())
        editCam.SetMg(cam.GetMg())
        bd.SetSceneCamera(editCam)
        
    else: 
        
        menu.InsData(1000, 'Perspective Camera&c&')    
        for i in range(len(cams)): 
            
            if cam == cams[i]:
                menu.InsData(i+1001, cams[i].GetName()+'&c&') 
            else:
                menu.InsData(i+1001, cams[i].GetName()) 
            
    
        
        
        result = gui.ShowPopupDialog(cd=None, bc=menu, x=c4d.MOUSEPOS,y=c4d.MOUSEPOS,flags=c4d.POPUP_LEFT)
        
        if result != 0: 
            bd.SetSceneCamera(cams[result-1001])
    c4d.EventAdd()
        
        
if __name__=='__main__':
    main()