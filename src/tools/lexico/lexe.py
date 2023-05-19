"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""
from src.tools.Manager.errorManager import Error,IllegalCharError
from src.tools.Manager.lexemasManager import *

##############
# CONSTANTES # 
##############

DIGITS = '0123456789'


##############
# TOKENS DIC # 
##############

TT_INT = 'ENTERO'
TT_FLOAT = 'REAl'
TT_STRING = 'ALFANUMERICO' # Pendiente
TT_BOOL = 'LOGICO'         # Pendiente

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

# OPERADORES RELACIONALES <OpRel> # 
TT_IGUAL = 'IGUAL'
TT_DIF = 'DIFERENTE'
TT_MENQ = 'MENORQUE'
TT_MAYQ = 'MAYORQUE'
TT_MENIG = 'MENOR_IGUAL'
TT_MAYIG = 'MAYOR_IGUAL'

# OPERADORES LOGICOS <OpLog> #
TT_Y = 'Y'
TT_O = 'O'
TT_NO = 'NO'

# OPERADOR DE ASIGNACION <OpAsig> #
TT_ASIG = 'ASIGNACION'


##########
# TOKENS # 
##########

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
############
# POSITION # 
############

class Position:
    def __init__(self,idx,ln,col,text):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.text = text

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char ==  '\n':
            self.ln += 1 
            self.col = 0
        
        return self
    
    def copy(self):
        return Position(self.idx,self.ln,self.col)

##########
# LEXICO # 
##########

class Lexico:
    def __init__(self, text):
        self.text = text
        self.pos = Position(-1,0,-1,text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_token(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' ':
                self.advance()
            elif self.current_char == '\t':
                writeLexTitle(lex='\_t',token='Delim')
                tokens.append(Token(TT_TAB))
                self.advance()
            
            ###########
            # DIGITOS #
            ###########

            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            ########################## 
            # OPERADORES ARITMETICOS #
            ########################## 

            elif self.current_char == '+':
                writeLexTitle(lex='+',token='OpArit')
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                writeLexTitle(lex='-',token='OpArit')
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                writeLexTitle(lex='*',token='OpArit')
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                writeLexTitle(lex='/',token='OpArit')
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '%':
                writeLexTitle(lex='%',token='OpArit')
                tokens.append(Token(TT_MOD))
                self.advance()
            elif self.current_char == '^':
                writeLexTitle(lex='^',token='OpArit')
                tokens.append(Token(TT_POW))
                self.advance()
            
            ################# 
            # DELIMITADORES #
            ################# 

            elif self.current_char == '(':
                writeLexTitle(lex='(',token='Delim')
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                writeLexTitle(lex=')',token='Delim')
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '[':
                writeLexTitle(lex='[',token='Delim')
                tokens.append(Token(TT_LBRA))
                self.advance()
            elif self.current_char == ']':
                writeLexTitle(lex=']',token='Delim')
                tokens.append(Token(TT_RBRA))
                self.advance() 
            elif self.current_char == '\n':
                writeLexTitle(lex='\_n',token='Delim')
                tokens.append(Token(TT_NL))
                self.advance()
            # elif self.current_char == '.':
            #     writeLexTitle(lex='.',token='Delim')
            #     tokens.append(Token(TT_DOT))
            #     self.advance()
            elif self.current_char == ',':
                writeLexTitle(lex=',',token='Delim')
                tokens.append(Token(TT_COMA))
                self.advance()
            elif self.current_char == ':':
                writeLexTitle(lex=':',token='Delim')
                tokens.append(Token(TT_DOBDOT))
                self.advance()
            elif self.current_char == ';':
                writeLexTitle(lex=';',token='Delim')
                tokens.append(Token(TT_SEMCOMA))
                self.advance()

            ################################### 
            # OPERADORES RELACIONALES <OpRel> #
            ###################################

            elif self.current_char == '=' and self.current_char != '<=':
                writeLexTitle(lex='=',token='OpRel')
                tokens.append(Token(TT_IGUAL))
                self.advance()

            # elif self.current_char in DIGITS:
            #     tokens.append(self.make_number())

            elif self.current_char == '<':
                tokens.append(self.Op_Log())
                
            #  #
            # Agregar los identificadores de:
            #       <=
            #       >=
            #       <>
            #       <
            #       >
            #  #
            
            ##############################
            # OPERADORES LOGICOS <OpLog> #
            ##############################
            
            # Agregar funcion para identificar -> Tienen que  tener espacios  ( _ es igua a espacio ' ')
            # _y_
            # _o_
            # _no_

            # elif self.current_char == 'y':
            #     tokens.append(Token(TT_IGUAL))
            #     self.advance()

            ###################################
            # OPERADOR DE ASIGNACION <OpAsig> #
            ###################################

            # Agregar funcion de deteccion de operador de asignacion -> :=

            #########
            # ERROR #
            #########

            else:
                line = self.pos.ln + 1
                char = self.current_char
                self.advance()
                # line, error, description, codeError
                return [], IllegalCharError(line,error=char,description="<Lexico>Error ALFANUMERICO",codeError=self.pos.text)
                


        return tokens, None

        # Agregar los identificadores de:
        #       <=
        #       <>
        #       <
    def Op_Log(self):
        opLog = ''

        while self.current_char != None and self.current_char != ';':
            if self.current_char == '=':
                print("llego aqui")
                opLog += '<='
                writeLexTitle(lex=opLog,token='OpRel')    
                return Token(TT_MAYQ, opLog)
            elif self.current_char == '>':
                print("llego aqui")
                opLog += '<>'
                writeLexTitle(lex=opLog,token='OpRel')    
                return Token(TT_MAYQ, opLog)
            self.advance()

              


    def make_number(self):
        num_srt = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break #ERROR LEXICO, No se permiten mas de dos decimales
                dot_count += 1
                num_srt += '.'
            else:
                num_srt += self.current_char
            self.advance()

        if dot_count==0:
            writeLexTitle(lex=num_srt,token='CteEnt')
            return Token(TT_INT, int(num_srt))
        else:
            writeLexTitle(lex=num_srt,token='CteReal')
            return Token(TT_FLOAT, float(num_srt ))

#########
# NODES # 
#########

class NumberNode:
    def __init__(self,tok):
        self.tok = tok

    def __repr__(self) -> str:
        return f'{self.tok}'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

##########
# PARSER # 
##########

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tok_idx = 1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    #####################
    def parse(self):
        res = self.expr()
        return res
    
    def factor(self):
        tok = self.current_tok

        if tok.type in (TT_INT,TT_FLOAT):
            self.advance()
            return NumberNode(tok)
        pass

    def term(self):
        return self.bin_op(self.factor,(TT_MUL, TT_DIV))

    def expr(self):
        return self.bin_op(self.term,(TT_PLUS, TT_MINUS))
    
    #####################

    def bin_op(self, func, ops):
        left = func()

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left,op_tok,right)

        return left

#####################
# EXECUTE BASIC LEX # 
#####################

def runBasicLex(text):
    lexico = Lexico(text)
    tokens, error = lexico.make_token()

    # Generate AST 
    # parser = Parser(tokens)
    # ast = parser.parse()
    
    return tokens, error

