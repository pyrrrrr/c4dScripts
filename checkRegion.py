import c4d

rvalue = True
if doc.GetActiveRenderData()[c4d.RDATA_RENDERREGION] == 1:
    rvalue = c4d.gui.QuestionDialog("Region render rendern?") 
if rvalue:
    c4d.CallCommand(12099)