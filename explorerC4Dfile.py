import c4d
import subprocess


def main():
    subprocess.Popen('explorer "'+ c4d.documents.GetActiveDocument().GetDocumentPath() + '"')

if __name__=='__main__':
    main()
