"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    Name: Daniel Vasquez Casas
    ID: 0199414
    ID: 0214778
    ID: 0208421
"""
import os
from datetime import date


def output(x,y):
    today = date.today()
    print("Simulation at: ",today)
    print("Universe size: ",x , " X ", y)
    fileLexCreate(x,y)

"""
    Create the new File.
"""
def fileLexCreate() -> None:
    today = date.today()
    if os.path.exists("./out/LexemasFile.lex"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("./out/LexemasFile.lex")
        fileLexCreate()
    else:
        print("The file does not exist.")
        print("Creating...\n")
        newFile = open("./out/LexemasFile.lex","x")
        text = "Lexemas Manager - "+str(today) + "\n"
        text += "------------------------------\n"
        text += "|    Lexema    |    Token    |\n"
        text += "------------------------------\n"
        
        newFile.write(text)


def writeLexTitle(lex,token):
    file = open("./out/LexemasFile.lex","a")
    text = f"| {lex} | {token} |\n"
    file.write(text)
    file.close()