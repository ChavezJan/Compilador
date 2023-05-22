"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    Name: Daniel Vasquez Casas
    ID: 0199414
    ID: 0214778
    ID: 0208421
"""

from src.tools.Manager.errorManager import *

##############
# CONSTANTES # 
##############

DIGITS = '0123456789'

##############
# TOKENS DIC # 
##############

TT_INT = 'ENTERO'
TT_FLOAT = 'REAL'
TT_STRING = 'ALFANUMERICO' # Pendiente
TT_BOOL = 'LOGICO'         # Pendiente

CONSTA = [TT_INT,TT_FLOAT,TT_BOOL,TT_STRING]

# OPERADORES ARITMETICOS <OpArit> # -> Listo
TT_PLUS = 'SUMA'
TT_MINUS = 'RESTA'
TT_MUL = 'MULTIPLICACION'
TT_DIV = 'DIVISION'
TT_MOD = 'MODULO'
TT_POW = 'POTENCIA'

# DELIMITADORES <Delim> # -> Listo
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_LBRA = 'LBRA' # -> [
TT_RBRA = 'RBRA' # -> ]
TT_NL = 'NL' 
TT_TAB = 'TAB'
TT_DOT = 'DOT'
TT_COMA = 'COMA'
TT_DOBDOT = 'DOBDOT'    # -> :
TT_SEMCOMA = 'SEMCOMA'  # -> ;
Delim = ['(',')','[',']','\t','\n','.',',',':',';']

# OPERADORES RELACIONALES <OpRel> # 
TT_IGUAL = 'IGUAL'
TT_DIF = 'DIFERENTE'
TT_MENQ = 'MENORQUE'
TT_MAYQ = 'MAYORQUE'
TT_MENIG = 'MENOR_IGUAL'
TT_MAYIG = 'MAYOR_IGUAL'
OPREL = '<>='

# OPERADORES LOGICOS <OpLog> #
TT_Y = 'Y'
TT_O = 'O'
TT_NO = 'NO'

# OPERADOR DE ASIGNACION <OpAsig> #
TT_ASIG = 'ASIGNACION'
TT_IDNT = 'IDENTIFICADOR'

# Palabras reservadas <PalRes>
TT_PALRES = 'PALRES'
PalRes = ["constantes", "variables", "real", "alfabetico", "logico", "entero", "funcion", "inicio", "fin", "de", "procedimiento", "regresa", "si", "hacer", "sino", "cuando", "el", "valor", "sea", "otro", "desde", "hasta", "incr", "decr", "repetir", "que", "mientras", "se", "cumpla", "continua", "interrumpe", "limpia", "lee", "imprime", "imprimenl", "verdadero", "falso", "programa", "fin de programa.", "fin de procedimiento","fin de funcion"]

# Extras #
TT_EOF = 'ENDOFFILE'

from src.tools.lexico.lexe import *
from src.tools.Manager.errorManager import *

class TableSim:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    def createTable(self):
        tempList=[]
        # var / const
        id =''
        value = ''
        tipo = ['V','C','F','P']
        
        while self.current_tok.type != TT_EOF:
            if self.current_tok.type == TT_PALRES:
                print(self.current_tok)
                if self.current_tok.value == 'constantes':
                    self.advance()
                    if self.current_tok.type == TT_IDNT:
                        id = self.current_tok.value
                    self.advance()
                    self.advance()
                    if self.current_tok.type in CONSTA:
                        value = self.current_tok.value
                        tempList.append([id,tipo[1],type(value),0,0,value])
                    
                    else:
                        IllegalSyntaxError(self.current_tok.line,self.current_tok.type,"SimTable ERROR, no fue posible crear la tabla", self.current_tok.value)
                    




            self.advance()
        return tempList

def makeSimTable(tokens):
    simTable = TableSim(tokens)
    # print(tokens)
    print(simTable.createTable())
