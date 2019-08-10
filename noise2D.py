import c4d
from c4d import gui
from c4d import bitmaps, documents
from random import shuffle


size = 64
n = size*size

s = (float(1)/float(n))

px = []
bmp = bitmaps.BaseBitmap()
bmp.Init(size, size, depth=32)
for i in xrange(0,n): px.append(i*s)

x = 0
y = -1
i = 0
shuffle(px)
for p in px:
    
    if (x % size == 0):
        y+=1
        x =0
    bmp.SetPixel(x, y, p*255,p*255 ,p*255 )
    x +=1


bitmaps.ShowBitmap(bmp)
    

