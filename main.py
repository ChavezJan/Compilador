"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""

from src.assets.test import *
from src.tools.Manager.fileReader import *
from src.tools.Manager.errorManager import *
from src.tools.Manager.lexemasManager import *


from src.tools.semantico.semanticPass import * 

# TEST
from src.tools.lexico.basic import *



if __name__ == "__main__":
    fileErrCreate()
    fileLexCreate()
    
    fileNoComments, numOfLines = fileReader()
    
    # Pase Lexico
    
    text = input('basic > ')
    result, error, = runBasicLex(text)

    if error: print(error.as_string())
    else: print(result)
    # Pase Sintactico

    # Pase Semantico
    # SemanticPass(fileNoComments)


    # TEST
    # writeErrTitle(10,"14.","<lexico>Se esparaba <digito>", "a:=b+14;")
    # writeLexTitle("alfa","<Ident>")
    
    # print(fileNoComments)
    # print(numOfLines)
