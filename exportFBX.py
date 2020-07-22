import c4d
from c4d import gui
import os
#Welcome to the world of Python


class GUIsceneSelector(gui.GeDialog):
   
    GUI_GROUP = 2000
    GUI_STATICTEX = 2001
 
    GUI_BUTTON_SAVE = 2003
    GUI_BOOL_SELECTED = 2004
    
   
    def save(self,selection):
        
        
        container = c4d.plugins.GetWorldPluginData(1026370)
        for id, value in container:
            if id == c4d.FBXEXPORT_ASCII:  container[id] = 0
            elif id == c4d.FBXEXPORT_BAKE_ALL_FRAMES: container[id] = 1
            elif id == c4d.FBXEXPORT_SAVE_NORMALS: container[id] = 1
            elif id == c4d.FBXEXPORT_TRACKS: container[id] = 1
            elif id == c4d.FBXEXPORT_BAKE_ALL_FRAMES: container[id] = 1
            elif id == c4d.FBXEXPORT_TEXTURES: container[id] = 1
            elif id == c4d.FBXEXPORT_EMBED_TEXTURES: container[id] = 0
            elif id == c4d.FBXEXPORT_PLA_TO_VERTEXCACHE: container[id] = 0
        
        newdoc = doc
        newDocName = ""
        if selection is True:
            null = doc.GetSelection()
            if len(null) == 0:
                gui.MessageDialog('Your selection is bad und you should feel bad about it!')
                self.Close()
                return
            if len(null) > 1:
                gui.MessageDialog('Multiple objects selected')
                self.Close()
                return
            
            newdoc = c4d.documents.IsolateObjects(doc,null)
            
            newdoc.SetFps(doc.GetFps())
            newdoc.SetMinTime(doc.GetMinTime())
            newdoc.SetMaxTime(doc.GetMaxTime())
            
            newDocName = "_" +newdoc.GetFirstObject().GetName()
            print newDocName
        
        docPath =  doc.GetDocumentPath()
        docName =  docPath +"\\"+ doc.GetDocumentName().replace(".c4d",newDocName + ".fbx")  
        print docPath
        print docName  
       
       
        c4d.documents.SaveDocument(newdoc,docName,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,1026370)
        self.Close()
        
   
    def CreateLayout(self):
    
        self.SetTitle('Default')
        
        self.GroupBegin(self.GUI_GROUP,c4d.BFH_CENTER,1,3,"Options",initw = 200, inith= 200)
        
        self.AddCheckbox(self.GUI_BOOL_SELECTED,c4d.BFH_LEFT, name="Export Selected",initw=200,inith=20)
        
        self.AddButton(self.GUI_BUTTON_SAVE,c4d.BFV_FIT, name="Save")
        
        self.GroupEnd()

        return True
        
    def InitValues(self):            
        
       # do stuff
        return True

    def Command(self, id, msg):
        
        if id == self.GUI_BUTTON_SAVE:
            self.save(self.GetBool(self.GUI_BOOL_SELECTED))
       
        return True

        
    def main(self):

        self.dialog = GUIsceneSelector()
        self.dialog.Open(dlgtype=c4d.DLG_TYPE_MODAL, defaultw=100, defaulth=100)
        return True





def main():

    g = GUIsceneSelector()
    g.main()
    
    
    
    
if __name__=='__main__':
    main()
