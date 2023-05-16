"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""

#Funcion para hacer algo cuando se encuentre la palabra
def evalKey():
    print("Si existe")

#verificar si existe la palabra
def checkMap(string):
    if(string in PalRes):
        PalRes[string]()
    else:
        print("no existe")

#Palabras Reservadas
PalRes = {"constantes": evalKey, "variables": evalKey, "real": evalKey, "alfabetico": evalKey, "logico": evalKey, "entero": evalKey, "funcion": evalKey, "inicio": evalKey, "fin": evalKey, "de":evalKey, "procedimiento": evalKey, "regresa": evalKey, "si": evalKey, "hacer": evalKey, "sino": evalKey, "cuando": evalKey, "el": evalKey, "valor": evalKey, "sea": evalKey, "otro": evalKey, "desde": evalKey, "hasta": evalKey, "incr":evalKey, "decr": evalKey, "repetir": evalKey, "que": evalKey, "mientras": evalKey, "se": evalKey, "cumpla": evalKey, "continua": evalKey, "interrumpe": evalKey, "limpia": evalKey, "lee": evalKey, "imprime": evalKey, "imprimenl": evalKey, "verdadero": evalKey, "falso": evalKey, "programa": evalKey, "fin de programa": evalKey}

#Operador de asignación
OpAsig = {":=": evalKey}

#Delimitadores
Delim = {".": evalKey, ",": evalKey, ";": evalKey, "(": evalKey, ")": evalKey, "[": evalKey, "]": evalKey, ":": evalKey, "\n": evalKey, "\t": evalKey}

#Operadores Aritméticos
OpArit = {"+": evalKey, "-": evalKey, "*": evalKey, "/": evalKey, "%": evalKey, "^": evalKey}

#Operadores Relacionales
OpRel = {"=": evalKey, "<>":evalKey, "<": evalKey, ">": evalKey, "<=": evalKey, ">=": evalKey}

#Operadores Lógicos
OpLog = {"y": evalKey, "o": evalKey, "no": evalKey}

string = "Inicio"
checkMap(string)


