import c4d
import subprocess
import os


def main():
    path = doc.GetActiveRenderData()[c4d.RDATA_PATH]
    m = os.path.dirname(path).split("\\")
    

    
    p = '\\'.join([str(x) for x in m ])
    print p
    if os.path.exists(p):
        
        subprocess.Popen('explorer "'+p + '"')
    
            

if __name__=='__main__':
    main()
