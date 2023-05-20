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
    if os.path.exists("./out/ErrorFile.err"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("./out/ErrorFile.err")
        fileErrCreate()
    else:
        print("The file does not exist.")
        print("Creating...\n")
        newFile = open("./out/ErrorFile.err","x")
        text = "Error Manager - "+str(today) + "\n"
        text += "-----------------------------------------------------------------------------\n"
        text += "| Linea | Error |        Descripción        |        Linea del Error        |\n"
        text += "-----------------------------------------------------------------------------\n"
        
        newFile.write(text)


def writeErrTitle(line,error,description,codeError):
    file = open("./out/ErrorFile.err","a")
    text = f"| {line} | {error} | {description} | {codeError}\n"
    file.write(text)
    file.close()

class Error:
    def __init__(self,line,error,description,codeError):
        self.line = line
        self.error = error 
        self.description = description
        self.codeError = codeError
        writeErrTitle(line, error, description, codeError)

    def as_string(self):
        result = f'| {self.line} | {self.error} | {self.description} | {self.codeError}'
        return result
    
class IllegalCharError(Error):
    def __init__(self, line, error, description, codeError):
        super().__init__(line, error, description, codeError) 

class IllegalSyntaxError(Error):
    def __init__(self, line, error, description, codeError):
        super().__init__(line, error, description, codeError) 


        
        