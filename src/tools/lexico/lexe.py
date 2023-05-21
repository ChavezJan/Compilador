"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    Name: Daniel Vasquez Casas
    ID: 0199414
    ID: 0214778
    ID: 0208421
"""
from src.tools.Manager.errorManager import *
from src.tools.Manager.lexemasManager import *
from src.tools.TablaSim.simTable import makeSimTable
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
Delim = [
    '(',
    ')',
    '[',
    ']',
    '\t',
    '\n',
    '.',
    ',',
    ':',
    ';']

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



##########
# TOKENS # 
##########

class Token:
    def __init__(self, type_, line=None ,value=None):
        self.type = type_
        self.value = value
        self.line = line 


    def __repr__(self) -> str:
        if self.value: return f'[{self.type}:{self.value}:{self.line}]'
        return f'[{self.type}:{self.line}]'
    
############
# POSITION # 
############

class Position:
    def __init__(self,idx,ln,col,text):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.text = text

    def advance(self, current_char=None):
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
        line = self.pos.ln + 1
        char = self.current_char

        while self.current_char != None:
            # print(self.current_char)
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '\t':
                writeLexTitle(lex='\_t',token='Delim')
                tokens.append(Token(TT_TAB, line=line))
                self.advance()

            ###########
            # DIGITOS #
            ###########

            elif self.current_char in DIGITS:
                tokens.append(self.make_number(line,char))

            ########################## 
            # OPERADORES ARITMETICOS #
            ########################## 

            elif self.current_char == '+':
                writeLexTitle(lex='+',token='OpArit')
                tokens.append(Token(TT_PLUS, line=line))
                self.advance()
            elif self.current_char == '-':
                writeLexTitle(lex='-',token='OpArit')
                tokens.append(Token(TT_MINUS, line=line))
                self.advance()
            elif self.current_char == '*':
                writeLexTitle(lex='*',token='OpArit')
                tokens.append(Token(TT_MUL, line=line))
                self.advance()
            elif self.current_char == '/':
                writeLexTitle(lex='/',token='OpArit')
                tokens.append(Token(TT_DIV, line=line))
                self.advance()
            elif self.current_char == '%':
                writeLexTitle(lex='%',token='OpArit')
                tokens.append(Token(TT_MOD, line=line))
                self.advance()
            elif self.current_char == '^':
                writeLexTitle(lex='^',token='OpArit')
                tokens.append(Token(TT_POW, line=line))
                self.advance()
            
            ###################################
            # OPERADOR DE ASIGNACION <OpAsig> #
            ###################################
            ################# 
            # DELIMITADORES #
            ################# 

            elif self.current_char == '(':
                writeLexTitle(lex='(',token='Delim')
                tokens.append(Token(TT_LPAREN, line=line))
                self.advance()
            elif self.current_char == ')':
                writeLexTitle(lex=')',token='Delim')
                tokens.append(Token(TT_RPAREN, line=line))
                self.advance()
            elif self.current_char == '[':
                writeLexTitle(lex='[',token='Delim')
                tokens.append(Token(TT_LBRA, line=line))
                self.advance()
            elif self.current_char == ']':
                writeLexTitle(lex=']',token='Delim')
                tokens.append(Token(TT_RBRA, line=line))
                self.advance() 
            elif self.current_char == '\n':
                writeLexTitle(lex='\_n',token='Delim')
                tokens.append(Token(TT_NL, line=line))
                self.advance()
                line += 1
            elif self.current_char == '.':
                writeLexTitle(lex='.',token='Delim')
                tokens.append(Token(TT_DOT, line=line))
                self.advance()
            elif self.current_char == ',':
                writeLexTitle(lex=',',token='Delim')
                tokens.append(Token(TT_COMA, line=line))
                self.advance()
            elif self.current_char == ':':
                tokens.append(self.delAsig(line,char))
            elif self.current_char == ';':
                writeLexTitle(lex=';',token='Delim')
                tokens.append(Token(TT_SEMCOMA, line=line))
                self.advance()

            ################################### 
            # OPERADORES RELACIONALES <OpRel> #
            ###################################

            elif self.current_char in OPREL:
                tokens.append(self.Op_Log(line,char))

            ##############################
            # OPERADORES LOGICOS <OpLog> #
            ##############################
            
            elif self.current_char == 'y':
                writeLexTitle(lex='y',token='OpLog')
                tokens.append(Token(TT_Y, line=line))
                self.advance()

            elif self.current_char == 'o':
                writeLexTitle(lex='o',token='OpLog')
                tokens.append(Token(TT_O, line=line))
                self.advance()          

            ##############
            # ID, CtaAlf #
            ##############

            else:
                tokens.append(self.genString(line,char))

                

        tokens.append(Token(TT_EOF, line=line))
        return tokens, None

    def delAsig(self,line,char):
        opDelAsig = ''
        while self.current_char != None and self.current_char != TT_EOF and self.current_char != ' ':
            if self.current_char == ":":
                opDelAsig += self.current_char
            elif self.current_char == "=":
                opDelAsig += self.current_char
                writeLexTitle(lex=opDelAsig,token='OpAsig')    
                self.advance()
                return Token(TT_ASIG, line=line)   
            else:
                break
            self.advance()
        
        
            
        if opDelAsig == ":": 
            writeLexTitle(lex=opDelAsig,token='Delim')
            # self.advance()
            return Token(TT_DOBDOT, line=line)
        else: ########### QUITAR RETURN ###############
            IllegalCharError(line,error=char,description="<Lexico>Error ALFANUMERICO",codeError=opDelAsig)#break #ERROR LEXICO, No se permiten mas de dos decimales

    def genString(self,line,char):
        op_String = ''
        conString = False

        while self.current_char != None and self.current_char not in Delim and self.current_char != ' ':
            if (self.current_char in Delim):
                print(self.current_char)

            # Retorna los alfanumericos (Strings)
            if self.current_char == '"' :
                op_String += self.current_char
                conString = True
                self.advance()
                while self.current_char != '"' and self.current_char != None: # None se tiene que cambir a \n
                    op_String += self.current_char
                    self.advance()
                if self.current_char == '"' and conString == True:
                    op_String += self.current_char
                    self.advance()
                    writeLexTitle(lex=op_String,token='CteAlfa')    
                    return Token(TT_STRING,value=op_String, line=line)
                    break
                else:
                    # ERROR 
                    pass
            else:
                op_String += self.current_char
            self.advance()

        if op_String in PalRes:
            writeLexTitle(lex=op_String,token='PalRes')    
            return Token(TT_PALRES,value=op_String, line=line)
        elif op_String == "no":
            writeLexTitle(lex=op_String,token='OpLog')    
            return Token(TT_NO,value=op_String, line=line)
        elif op_String == "verdadero" or op_String == "falso":
            writeLexTitle(lex=op_String,token='CteLog')    
            return Token(TT_BOOL,value=op_String, line=line)
        else:
            writeLexTitle(lex=op_String,token='Ident')    
            return Token(TT_IDNT,value=op_String, line=line)
      
    def Op_Log(self,line,char):
        opLog = ''

        while self.current_char != None and self.current_char != TT_EOF and self.current_char != ' ':
            if self.current_char == '=':
                opLog += self.current_char
            elif self.current_char == '>':
                opLog += self.current_char
            elif self.current_char == '<':
                opLog += self.current_char
            else:                
                opLog += self.current_char
            self.advance()

        if opLog == "=":
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_IGUAL, line=line)
        elif opLog == "<":
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_MENQ, line=line)
        elif opLog == ">":
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_MAYQ, line=line)
        elif opLog == "<>":
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_DIF, line=line)
        elif opLog == "<=": 
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_MENIG, line=line)
        elif opLog == ">=": 
            writeLexTitle(lex=opLog,token='OpRel')    
            return Token(TT_MAYIG, line=line)
        else:
            IllegalCharError(line,error=char,description="<Lexico>Error ALFANUMERICO",codeError=opLog)#break #ERROR LEXICO, No se permiten mas de dos decimales

    def make_number(self,line,char):
        num_srt = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':

            if self.current_char == '.':
                if dot_count == 1: 
                    dot_count += 1
                    char = self.current_char
                    while self.current_char == '.':
                        self.advance()
                    IllegalCharError(line,error=char,description="<Lexico>Error ALFANUMERICO: No esperado el '.'",codeError=self.pos.text)

                dot_count += 1
                num_srt += '.'
            else:
                num_srt += self.current_char
            self.advance()

        if dot_count==0:
            writeLexTitle(lex=num_srt,token='CteEnt')
            return Token(TT_INT, value=int(num_srt), line=line)
        elif dot_count == 1:
            writeLexTitle(lex=num_srt,token='CteReal')
            return Token(TT_FLOAT, value=float(num_srt ), line=line)

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
    
class UnaryOpNode:
    def __init__(self,op_tok,node):
        self.op_tok = op_tok
        self.node = node

    def __repr__(self) -> str:
        return f'({self.op_tok},{self.node})'
        
#################
# PARSER RESULT # 
#################

class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, ParserResult):
            if res.error: self.error = res.error
            return res.node
        
        return res

    def success(self, node):
        self.node = node
        return self


    def fail(self, error):
        self.error = error
        return self

##########
# PARSER # 
##########

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    #####################
    def parse(self):
        res = self.expr()
        if not res.error and self.current_tok.type != TT_EOF:
            return res.fail(IllegalSyntaxError(line=1,error="error",description="IllegalSyntaxError: Esperado '+', '-', '*', '/', '^', '%',",codeError="test"))
        return res
    
    def factor(self):
        res =  ParserResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS,TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok,factor))
        
        elif tok.type in (TT_INT,TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))
        
        elif tok.type == TT_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.fail(IllegalSyntaxError(line=1,error="error",description="IllegalSyntaxError: Esperado ')'",codeError="test"))   
            
        return res.fail(IllegalSyntaxError(line=1,error="error",description="IllegalSyntaxError: Esperado Entero o Real",codeError="test"))

    def termPow(self):
        return self.bin_op(self.factor,(TT_MOD, TT_POW))

    def term(self):
        return self.bin_op(self.termPow,(TT_MUL, TT_DIV))

    def expr(self):
        return self.bin_op(self.term,(TT_PLUS, TT_MINUS))
    
    #####################

    def bin_op(self, func, ops):
        res =  ParserResult()
        left = res.register(func())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinOpNode(left,op_tok,right)

        return res.success(left)

#####################
# EXECUTE BASIC LEX # 
#####################

def runBasicLex(text):
    lexico = Lexico(text)
    tokens, error = lexico.make_token() 

    #tokens.remove(None)
    # print(tokens)

    # print(tokens)

    if len(tokens) <= 1:
        writeErrTitle("#"," - ", "<FatalError>","No se generaron tokens")
        # return None,None,None

    if error: return None, error

    #send data to the table
    makeSimTable(tokens)


    # Generate AST 
    # parser = Parser(tokens)
    # ast = parser.parse()
    # # return tokens, ast.node ,ast.error

    # print(ast.node)
    # print(ast.error)
    
    # return tokens, None ,None
