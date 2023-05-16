from src.tools.lex.dataLexico import *
import re

def getFirstWord(file):
    pass
   

def rid(file):
    file = re.sub(pattern="\t+",string=file,repl=" ")
    file = re.sub(pattern="(?<=\n)\s+",string=file,repl="")
    file = file.split("\n")
    print(file)