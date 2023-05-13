"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""

import os
from datetime import date

def createErrorFile():
    print("holw")


def output(x,y):
    today = date.today()
    print("Simulation at: ",today)
    print("Universe size: ",x , " X ", y)
    fileErrCreate(x,y)

"""
    Create the new File.
"""
def fileErrCreate() -> None:
    today = date.today()
    if os.path.exists("./data/ErrorFile.err"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("./data/ErrorFile.err")
        fileErrCreate()
    else:
        print("The file does not exist.")
        print("Creating...\n")
        newFile = open("./data/ErrorFile.err","x")
        text = "Error Manager - "+str(today) + "\n"
        text += "-----------------------------------------------------------------------------\n"
        text += "| Linea | Error |        Descripción        |        Linea del Error        |\n"
        text += "-----------------------------------------------------------------------------\n"
        
        newFile.write(text)


def writeErrTitle(line,error,description,codeError):
    file = open("./data/ErrorFile.err","a")
    text = f"| {line} | {error} | {description} | {codeError}\n"
    file.write(text)
    file.close()