import c4d
from c4d import gui
from c4d import bitmaps, documents
from random import shuffle
#Welcome to the world of Python


def main():
    

    size = 256
   
    
    bmp = bitmaps.BaseBitmap()
    bmp.Init(size, size, depth=32)
    bmp.SetData(c4d.BASEBITMAP_DATA_GAMMA,2.2)
  
    
    for x in xrange(0,(size)):
        
        for y in xrange(0,(size)):
            
            bmp.SetPixel(x, y,  x*(float(1)/float(size))*255   ,   y*(float(1)/float(size))*255*-1+255    ,   0    )

    bitmaps.ShowBitmap(bmp)
    

if __name__=='__main__':
    main()
