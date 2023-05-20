"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    Name: Daniel Vasquez Casas
    ID: 0199414
    ID: 0214778
    ID: 0208421
"""

from src.assets.test import *
from src.tools.Manager.fileReader import *
from src.tools.Manager.errorManager import *
from src.tools.Manager.lexemasManager import *


from src.tools.semantico.semanticPass import * 

# TEST
from src.tools.lexico.lexe import *



if __name__ == "__main__":
    fileErrCreate()
    fileLexCreate()
    
    fileNoComments, numOfLines = fileReader()
    
    # Pase Lexico
    
    text = input('basic > ')
    try:
        result, ast ,error = runBasicLex(text)
        if error: print(error.as_string())
        else: print(f'{result} \n{ast}')
    except:
        print(f'ERROR')
        


    # Pase Sintactico

    # Pase Semantico
    # SemanticPass(fileNoComments)


    # TEST
    # writeErrTitle(10,"14.","<lexico>Se esparaba <digito>", "a:=b+14;")
    # writeLexTitle("alfa","<Ident>")
    
    # print(fileNoComments)
    # print(numOfLines)
