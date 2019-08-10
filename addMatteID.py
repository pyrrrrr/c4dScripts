### postwendend.com ###
### tobias hoffmann ###
### kontakt@postwendend.com ###

import  c4d
from    c4d.documents   import GetActiveDocument

def GetNextObject(op):
    if op==None: return None
 
    if op.GetDown(): return op.GetDown()
    while not op.GetNext() and op.GetUp():
        op = op.GetUp() 
    return op.GetNext()


def add_channel(tagname, tagchannel):
    
    buffer = c4d.BaseList2D(c4d.Zmultipass)
    buffer.GetDataInstance()[c4d.MULTIPASSOBJECT_TYPE] = c4d.VPBUFFER_OBJECTBUFFER
    # check nach vorhandenen MPs
    rd = doc.GetActiveRenderData()
    vp = rd.GetFirstMultipass()
    exist_buffer = 0
    
    while vp:
        if vp.GetTypeName() == "Object Buffer":
           
           if vp[c4d.MULTIPASSOBJECT_OBJECTBUFFER] == tagchannel:
               print "channel "+ str(tagchannel) + " vorhanden"
               exist_buffer = 1

        vp = vp.GetNext()    
    
    if exist_buffer == 0:
        
        buffer.SetName ( tagname  )
        buffer[c4d.MULTIPASSOBJECT_OBJECTBUFFER] = int(tagchannel)
        # hier auskommentieren
        rd.InsertMultipass (buffer)
        
        
    

def main():
    doc  = GetActiveDocument()
    all_op   = doc.GetFirstObject()
    

    while all_op:
        tags  = all_op.GetTags()
        for tag in tags:  
           if tag.CheckType(c4d.Tcompositing):
               
               
               if tag[c4d.COMPOSITINGTAG_ENABLECHN0] == 1:
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN0]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN1] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN1]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN2] == 1:
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN2]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN3] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN3]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN4] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN4]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN5] == 1:
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN5]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN6] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN6]
                   add_channel (tagname, tagchannel) 
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN7] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN7]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN8] == 1:
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN8]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN9] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN9]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN10] == 1:                                                                                     
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN10]
                   add_channel (tagname, tagchannel)
               elif tag[c4d.COMPOSITINGTAG_ENABLECHN11] == 1:
                   tagname = all_op.GetName()
                   tagchannel = tag[c4d.COMPOSITINGTAG_IDCHN11]
                   add_channel (tagname, tagchannel)
               ######### print gibt tagname und kanal aus:: 
               print str(tagname) + "=" + str(tagchannel)

        all_op = GetNextObject(all_op)  

    c4d.EventAdd()   

if __name__=='__main__':
    main()