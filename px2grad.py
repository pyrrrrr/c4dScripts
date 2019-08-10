import c4d
from c4d import bitmaps, gui, storage
import random
import colorsys

def main():
    
    path = storage.LoadDialog(type=c4d.FILESELECTTYPE_IMAGES, title="Please Choose a 32 Bit Image:")
    #path = "C:\\Users\\tobi\\Desktop\\test.jpg"
    if not path: return

    # Create and initialize selected image
    orig = bitmaps.BaseBitmap()
    if orig.InitWith(path)[0] != c4d.IMAGERESULT_OK:
        gui.MessageDialog("Cannot load image \"" + path + "\".")
        return

    width, height = orig.GetSize()
    bits = orig.GetBt()
    pxColl = []
    
    for x in range (0,width):
        for y in range (0,height):
            pxColl.append( orig.GetPixel(x,y) )

    
    samples = 16
    seed = 500
    pxColl.sort()

        
     
            
    i = 0
    for x in range (0,width):
        for y in range (0,height):
            
            orig.SetPixel(x,y,int(pxColl[i][0]),int(pxColl[i][1]),int(pxColl[i][2]))
            
            i += 1  
            
    bitmaps.ShowBitmap(orig)
    
    
    copy = bitmaps.BaseBitmap() 
    copy.Init(samples, 1, bits)
    collPic = []
    for x in range(0,samples):
        
        #random.seed(x+seed)
        rgb =len(pxColl)/samples*x
        newcoll = pxColl[rgb][0],pxColl[rgb][1],pxColl[rgb][2]
        #print newcoll
        collPic.append( newcoll )

    collPic.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))

    i = 0
    #print collPic
    for item in collPic:
        copy.SetPixel(i,0,item[0],item[1],item[2])        
        
        i += 1
    
    
    
    
    

    
    
    #bitmaps.ShowBitmap(copy)


if __name__=='__main__':
    main()

