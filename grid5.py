import c4d


def intRound(x, base=5):
    return int(base * round(float(x)/base))

def main():
    selection = doc.GetSelection()
    i = 0
    for item in selection:
        pc = len(item.GetAllPoints())
        np = []
        for i in range(0,pc):
            v = item.GetPoint(i)
            np.append(c4d.Vector(intRound(v.x),intRound(v.y),intRound(v.z)))
        item.SetAllPoints(np)
        item.CreatePhongNormals()
    c4d.CallCommand(14039)
    
    c4d.EventAdd(c4d.EVENT_ENQUEUE_REDRAW)
    
    
if __name__=='__main__':
    main()
