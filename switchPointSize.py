import c4d
from c4d import gui
#Welcome to the world of Python

bd = doc.GetActiveBaseDraw()
if bd[c4d.BASEDRAW_DATA_POINT_SELECTED_SIZE] == 10:
    bd[c4d.BASEDRAW_DATA_POINT_HANDLE_SIZE] = 4
    bd[c4d.BASEDRAW_DATA_POINT_SELECTED_SIZE] = 4
else:
    bd[c4d.BASEDRAW_DATA_POINT_HANDLE_SIZE] = 10
    bd[c4d.BASEDRAW_DATA_POINT_SELECTED_SIZE] = 10
c4d.EventAdd()