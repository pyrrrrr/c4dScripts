import c4d
import math
from c4d import utils


# Calculate a polygons' face normal
def CalcFaceNormal(op, polyIndex):
    poly = op.GetPolygon(polyIndex)


    v0 = op.GetPoint(poly.a)
    v1 = op.GetPoint(poly.b) 
    v3 = op.GetPoint(poly.d) # point c==d, only 3 points needed to calculate a face normal
    
    return (v1 - v0).Cross(v3 - v0) # return cross product of point vectors
    
# Calculate face area
def CalculateFaceArea(op, polyIndex):
    poly = op.GetPolygon(polyIndex)
    v0 = op.GetPoint(poly.a)
    v1 = op.GetPoint(poly.b)
    v2 = op.GetPoint(poly.c)
    v3 = op.GetPoint(poly.d)
    
    if poly.IsTriangle():
        return (0.5 * ((v1-v0) % (v2-v0)).GetLength())
    else: # if quad
        return (0.5 * ((v1-v0) % (v2-v0))).GetLength() + (0.5 * ((v3-v2) % (v0-v2)).GetLength())
  


# Calculate the face angle of the corner and shared edges
def CalculateFaceAngle(op, polyIndex, point):
    poly = op.GetPolygon(polyIndex)


    v0 = op.GetPoint(poly.a)
    v1 = op.GetPoint(poly.b)
    v3 = op.GetPoint(poly.d)
    
    fv0, fv1, fv3 = v0, v1, v3
    
    # TODO: Assemble shared triangles to quads
    
    if poly.IsTriangle():
        if point == poly.b:
            fv0 = v1
            fv1 = v0
            fv3 = v3
            
        if point == poly.d:
            fv0 = v3
            fv1 = v1
            fv3 = v0
        
    return utils.VectorAngle((fv0-fv3), (fv0-fv1))  


# Calculate a point's average vertex normal, based on neighboring face normals
def CalculateVertexNormal(op, pointIndex, polyIndex, nbr):
    normal = c4d.Vector()
    nPolys = nbr.GetPointPolys(pointIndex) #get neighbor poly array
    
    for neighborPolyIndex in nPolys:
        normal = normal + CalcFaceNormal(op, neighborPolyIndex) * CalculateFaceArea(op, neighborPolyIndex) * CalculateFaceAngle(op, neighborPolyIndex, pointIndex) # add up neighbors normals
    
    return normal.GetNormalized() # normalized arithmetic middle of neighbored normals


def main():
    doc.StartUndo()
    nbr = utils.Neighbor() # involve neighbors
    
    tag = c4d.VariableTag(c4d.Tnormal, op.GetPolygonCount()) # create/override tag
    normals = [] # the HighLevelData Container (sequentially written vectors for each point component)
    
    nbr.Init(op)
    for polyIndex in xrange(op.GetPolygonCount()):
        poly = op.GetPolygon(polyIndex)
        
        # Calculate vertex normal for each point
        pointIndexArray = [poly.a, poly.b, poly.c, poly.d] 
        
        for pointIndex in pointIndexArray: # append vectors sequentially split
            vNorms = CalculateVertexNormal(op, pointIndex, polyIndex, nbr)
            normals.append(vNorms.x*32000)
            normals.append(vNorms.y*32000)
            normals.append(vNorms.z*32000)
            
    op.InsertTag(tag) # Apply tag
    tag.SetAllHighlevelData(normals) # write normal container to tag
    
    c4d.EventAdd()
    doc.AddUndo(c4d.UNDOTYPE_NEW, tag)
    


if __name__=='__main__':
    main()