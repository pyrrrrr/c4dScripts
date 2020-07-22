import c4d

class GridSizeGui(c4d.gui.GeDialog):
    
    GUI_GROUP = 2000
    GUI_STATICTEX = 2001
    GUI_INT_GRID = 2002
    GUI_BUTTON_EXCECT = 2003


    def CreateLayout(self):

        self.SetTitle('Grid It')

        self.GroupBegin(self.GUI_GROUP, c4d.BFH_CENTER, 1, 3, "Options", initw=200, inith=50)     

        self.AddEditNumber(self.GUI_INT_GRID, c4d.BFH_RIGHT, initw=200, inith=20)

        self.AddButton(self.GUI_BUTTON_EXCECT, c4d.BFV_FIT, name="GRIT IT")

        self.GroupEnd()

        return True

    def InitValues(self):
        bc = doc.GetDocumentData(self.GUI_INT_GRID)
        for index, value in bc:
            print "Index: %i, Value: %s" % (index, str(value))
        return True

    def Command(self, id, msg):

        if id == self.GUI_BUTTON_EXCECT:
            
            selection = doc.GetSelection()
            
            
            doc.StartUndo()  
               
                   
               
        
            for item in selection:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE,item)
                   
                pc = len(item.GetAllPoints())
                np = []
                for i in range(0,pc):
                    v = item.GetPoint(i)
                    np.append(c4d.Vector(intRound(v.x),intRound(v.y),intRound(v.z)))
                item.SetAllPoints(np)
                item.CreatePhongNormals()
                
            c4d.CallCommand(14039)
            
            
            
            c4d.EventAdd(c4d.EVENT_ENQUEUE_REDRAW)
            bc = c4d.BaseContainer()
            bc.SetData(self.GUI_INT_GRID,self.GetInt32(self.GUI_INT_GRID))
            doc.SetDocumentData(self.GUI_INT_GRID, bc)
            doc.EndUndo()
            self.Close()
            
            
            
        return True



    def main(self):

        self.dialog = GridSizeGui()
        self.dialog.Open(dlgtype=c4d.DLG_TYPE_MODAL, defaultw=100, defaulth=10)
        return True


def intRound(x, base=5):
    return int(base * round(float(x)/base))

def main():
    
    i = 0
    g = GridSizeGui()
    g.main()
    
   
    
    
    
    
if __name__=='__main__':
    main()
