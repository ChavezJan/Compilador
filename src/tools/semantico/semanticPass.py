"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""

from src.tools.semantico.UnicityCheck import *

def SemanticPass(file):

    palRes = ["constantes","variables"]
    constantes = False
    variables = False

    listConst = []
    listVar = []
    

    file = file.replace("\t"," ")
    file = file.replace("\n"," ")
    #print(file)
    file = file.split(" ")
    for line in file:
        if(line != ""):
            if (line == "constantes"):
                constantes  =  True
                variables = False
            print("-----")
            print(line)
            print("-----")
            if (line == "variables"):
                variables = True   
                constantes = False

            if(constantes == True): 
                listConst.append()
                print("son constantes")
            if(variables == True):
                print("son variables")

            



        
    # # test()