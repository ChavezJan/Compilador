"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""

def fileReader():

    try:
        fileR = open("./data/test.up","r")
    except:
        print("ERROR: Archivo buscado no encontrado")
        return "ERROR"

    return fileR.read().lower()

    fileR = fileR.read().split("\n")

    fileNocomments = ""
    for i in fileR:
        fileNocomments += i

    return fileNocomments
    changeSpace = False

    numOfLines = 0
    for line in fileR:
        comentario = 0
        for char in line:
            if(comentario == 2):
                # print("Comentario")
                comentario = comentario
            else:
                if (char == "/"):
                    comentario += 1
                elif(char == " "):
                    changeSpace = True
                    fileNocomments += char
                elif(changeSpace == True and char == " "):
                    changeSpace = True
                else:
                    changeSpace = False
                    fileNocomments += char
        numOfLines += 1
        fileNocomments += "\n"

    return fileNocomments, numOfLines