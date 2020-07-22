import c4d, subprocess,os,sys
from c4d import gui
  
# Get Cinemas Process ID for murder
PID = str(os.getpid())
  
# Cinema's EXE file for restart
app = ("'"+c4d.storage.GeGetStartupApplication()+"'")
  
# Get users document path
DocPath = c4d.storage.GeGetC4DPath(c4d.C4D_PATH_MYDOCUMENTS)
  
# Check and create a powershell file in your documents path
if not os.path.exists(DocPath+"\C4D_Restart.ps1") :
    f = open(DocPath+"\C4D_Restart.ps1","w")
    f.write("")
    f.close()
else:
    pass
  
# Path to Powershell program
PSPath = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'
  
# path to the created code.
Wpath = r""+DocPath+"\C4D_Restart.ps1"
  
# Code to write into the Powershell file.
ps1 = r"Stop-Process "+PID+"\nStart-Sleep -Seconds 2\n\nStart-Process "+app+"\n"
  
# Write to powershell file
f = open(Wpath,"w")
f.write(ps1)
f.close()
  
# Run powershell
subprocess.Popen([PSPath,'-ExecutionPolicy','Unrestricted',Wpath])