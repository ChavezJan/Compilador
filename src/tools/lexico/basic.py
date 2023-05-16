"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    ID: 0199414
    ID: 0214778
"""
from src.tools.Manager.errorManager import Error,IllegalCharError

##############
# CONSTANTES # 
##############

DIGITS = '0123456789'


##############
# TOKENS DIC # 
##############

TT_INT = 'ENTERO'
TT_FLOAT = 'REAl'
TT_STRING = 'ALFANUMERICO'
TT_BOOL = 'LOGICO'

# OPERADORES ARITMETICOS #
TT_PLUS = 'SUMA'
TT_MINUS = 'RESTA'
TT_MUL = 'MULTIPLICACION'
TT_DIV = 'DIVISION'
TT_MOD = 'MODULO'
TT_POW = 'POTENCIA'

# DELIMITADORES #
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_LBRA = 'LBRA'
TT_RBRA = 'RBRA'
TT_NL = 'NL'
TT_TAB = 'TAB'
TT_DOT = 'DOT'
TT_COMA = 'COMA'
TT_DOBDOT = 'DOBDOT'
TT_SEMCOMA = 'SEMCOMA'

# OPERADORES RELACIONALES #
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_LBRA = 'LBRA'
TT_RBRA = 'RBRA'
TT_NL = 'NL'
TT_TAB = 'TAB'
TT_DOT = 'DOT'
TT_COMA = 'COMA'
TT_DOBDOT = 'DOBDOT'
TT_SEMCOMA = 'SEMCOMA'

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
            if self.current_char in ' \t':
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
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '%':
                tokens.append(Token(TT_MOD))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW))
                self.advance()
            
            ################# 
            # DELIMITADORES #
            ################# 

            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()

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
            return Token(TT_INT, int(num_srt))
        else:
            return Token(TT_FLOAT, float(num_srt ))
        
#####################
# EXECUTE BASIC LEX # 
#####################

def runBasicLex(text):
    lexico = Lexico(text)
    tokens, error = lexico.make_token()
    
    return tokens, error