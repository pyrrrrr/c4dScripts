import c4d
from c4d import gui
#Welcome to the world of Python

bd = doc.GetActiveBaseDraw()
bd[c4d.BASEDRAW_DATA_POINT_HANDLE_SIZE] += 1
c4d.EventAdd()