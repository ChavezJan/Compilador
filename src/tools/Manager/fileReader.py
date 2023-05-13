"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""

def fileReader():

    #print("Enter the file to test:\n1) input1\n2) input2\n3) input3\n4) input4\n5) input5\n6) input6\n7) input7")
    #inputFile = str(inputManager((input()),("1","2","3","4","5","6","7")))
    try:
        fileR = open("./data/ArchivoPrueba.up","r")
    except:
        print("ERROR: Archivo buscado no encontrado")
        return "ERROR"

    fileR = fileR.read().split("\n")
    fileNocomments = ""

    numOfLines = 0
    for line in fileR:
        comentario = 0
        for char in line:
            if(comentario == 2):
                print("Comentario")
            else:
                if (char == "/"):
                    comentario += 1
                else:
                    fileNocomments += char
        numOfLines += 1
        fileNocomments += "\n"

    return fileNocomments, numOfLines