import c4d
from c4d import gui
#Welcome to the world of Python


mat = doc.GetActiveMaterials()
if len(mat) == 0:
    gui.MessageDialog('Nothing selected!')     
else:     

    for m in mat:
            irs = c4d.modules.render.InitRenderStruct()
            shader =  m[c4d.MATERIAL_TRANSPARENCY_SHADER]
            if shader.InitRender(irs)==c4d.INITRENDERRESULT_OK:
                print shader[c4d.BITMAPSHADER_FILENAME],shader.GetBitmap().GetChannelCount()
            shader.FreeRender()
            
