"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""

from src.assets.test import *
from src.tools.Manager.fileReader import *
from src.tools.Manager.errorManager import *
from src.tools.Manager.lexemasManager import *



if __name__ == "__main__":
    fileErrCreate()
    fileLexCreate()
    
    newFile, numOfLines = fileReader()

    # TEST
    writeErrTitle(10,"14.","<lexico>Se esparaba <digito>", "a:=b+14;")
    writeLexTitle("alfa","<Ident>")
    
    print(newFile)
    print(numOfLines)
