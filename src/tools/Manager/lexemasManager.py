"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import time
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
    if os.path.exists("./data/LexemasFile.lex"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("./data/LexemasFile.lex")
        fileLexCreate()
    else:
        print("The file does not exist.")
        print("Creating...\n")
        newFile = open("./data/LexemasFile.lex","x")
        text = "Lexemas Manager - "+str(today) + "\n"
        text += "------------------------------\n"
        text += "|    Lexema    |    Token    |\n"
        text += "------------------------------\n"
        
        newFile.write(text)


def writeLexTitle(lex,token):
    file = open("./data/LexemasFile.lex","a")
    text = f"| {lex} | {token} |\n"
    file.write(text)
    file.close()