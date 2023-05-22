"""
    Name: Jorge Alejandro Chavez Nuñez
    Name: Sebastian Garcia Aguirre
    Name: Daniel Vásquez Casas
    ID: 0199414
    ID: 0214778
    ID: 0208421
"""
from src.tools.lexico.lexe import *
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
PalRes = ["constantes", "variables", "real", "alfabetico", "logico", "entero", "funcion", "inicio", "fin", "de", "procedimiento", "regresa", "si", "hacer", 
	  "sino", "cuando", "el", "valor", "sea", "otro", "desde", "hasta", "incr", "decr", "repetir", "que", "mientras", "se", "cumpla", "continua", "interrumpe",
	    "limpia", "lee", "imprime", "imprimenl", "verdadero", "falso", "programa", "fin de programa.", "fin de procedimiento","fin de funcion"]

# Extras #
TT_EOF = 'ENDOFFILE'









class Variables: #Variables
	def __init__(self):
		pass

	def variables(self, tokens): #<variables>::= variables <GpoVars>
		return self.gpoVars(tokens)

	def gpoVars(self, tokens): #<GpoVars>::=<GpoIds>:<tipo>;[<GpoVars>]
		GpoVars = []
		varInit = False
		valor = 0
		Tipo = ''
		GpoIds = self.gpoIds(tokens)		
		aux = tokens[0]
		#print(aux)
		#if(aux.type is not 'DOBDOT'):			
		#	IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba delimitador", aux.value)
		Tipo = self.tipo(tokens)	
		
		aux = tokens.pop(0)
		if(aux.type is not 'SEMCOMA'):			
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba delimitador", aux.value)
		
		while True:
			aux = tokens[0]
			if aux.type == 'NL' or aux.type == 'TAB':
				tokens.pop(0)
				continue
			else:
				break
	
		#GpoVars.append(self.gpoVars(tokens))

		return GpoIds, Tipo, GpoVars

	def gpoIds(self, tokens):#<GpoIds>::=Id[<Dimens>][:= CteEnt|Id][,<GpoIds>]
		Dimens = None
		Id = ''
		valor = None
		GpoIds = []

		#Obtener Id
		aux = tokens.pop(0)
		#print(len(tokens))

		if(aux.type is not 'IDENTIFICADOR'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba identificador", aux.value)
		else:
			Id = aux.value

		#Obtener Dimensiones, si es que tiene
		aux = tokens.pop(0)
		if(aux.type is 'LBRA'):
			Dimens = self.dimensiones(tokens)
			aux = tokens.pop(0)


	
		if(aux.type is 'ASIGNACION' or aux.type is 'IGUAL'):
			aux = tokens.pop(0)
		
			#if(aux.type is 'IDENTIFICADOR' or )
			valor = aux.value
		
		if(aux.type is 'COMA'):
			GpoIds.append(self.gpoIds(tokens))
		
		return Id, Dimens, valor, GpoIds


	
	def dimensiones(self, tokens):#<Dimens>::=[CteEnt|Id][<Dimens>]
		varDim = None
		aux = tokens.pop(0)		
		if(aux.type is not 'ENTERO' and aux.type is not 'IDENTIFICADOR'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba entero o identificador", aux.value)
		else:
			varDim = aux.value
		aux = tokens.pop(0)		
		if(aux.type is not 'RBRA'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba un delimitador", aux.value)


		aux = tokens[0]
		if(aux.type is 'LBRA'):
			tokens.pop(0)
			return '[' + str(varDim) + ']' + self.dimensiones(tokens)
		else:
			return '[' + str(varDim) + ']'



	def tipo(self, tokens):
		varTipo = ''
		aux = tokens.pop(0)
		if(aux.value != 'entero' and aux.value != 'real' and aux.value != 'alfanumerico' and aux.value != 'logico'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba asignacion de tipo", aux.value)
		else:
			varTipo = aux.value
		#entero|real|alfabetico|logico
		#TT_INT|TT_FLOAT|TT_STRING|TT_BOOL
		return varTipo






class Constantes: 
	def __init__(self):
		pass
	#def __repr__(self):


	def gpoConst(self, tokens):#<GpoConst>::= id:=<cte>
		Id = ''
		valor = 0

		aux = tokens.pop(0)
		if(aux.type is not 'IDENTIFICADOR'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba identificador", aux.value)
		else: 
			Id = aux.value

		aux = tokens.pop(0)
		if(aux.type is not 'ASIGNACION'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba operador de asignacion", aux.value)
		
		aux = tokens.pop(0)
		if(aux.type is not 'ENTERO' and aux.type is not 'REAL' and aux.type is not 'ALFANUMERICO' and aux.type is not 'LOGICO'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba asignacion de tipo", aux.value)
		else:
			valor = aux.value

		aux = tokens.pop(0)
		if(aux.type is not 'SEMCOMA'): # ;
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba un delimitador", aux.value)
		return Id, valor

	def constantes(self, tokens):#<constantes>::=constantes <GpoConst>
		return self.gpoConst(tokens)


class FuncProcedimiento:
	def __init__(self):
		pass

	def tipo(self, tokens):
		varTipo = ''
		aux = tokens.pop(0)
		if(aux.value != 'entero' and aux.value != 'real' and aux.value != 'alfanumerico' and aux.value != 'logico'):
			IllegalSyntaxError(aux.line, "Sintactico", "Se esperaba asignacion de tipo", aux.value)
		else:
			varTipo = aux.value
		#entero|real|alfabetico|logico
		#TT_INT|TT_FLOAT|TT_STRING|TT_BOOL
		return varTipo

	def params(self, tokens):#<Params>::=<GpoPars>:<tipo>[;<Params>]
		Params = []
		GpoPars = self.gpoPars(tokens)
		Tipo = self.tipo(tokens)
		Params.append(self.params( tokens))
		return GpoPars, Tipo, Params

	def gpoPars(self):#<GpoPars>::=Id[, <GpoPars>]
		#if()
		Pars = []
		Id = ''
		Pars.append(self.gpoPars)
		return Id, Pars

	def procedimiento(self):#. <procedimiento>::=procedimiento Id([<Params>])[<variables>] inicio [<Block>] fin de procedimiento;
		Id = ''
		Params = self.params()
		Vars = Variables.variables()
		Block = self.block()
		return Id, Params, Vars, Block

	def funcion(self):#<funcion>::=funcion Id([<Params>]):<tipo>[<variables>] inicio [<Block>] fin de funcion;
		Id = ''
		Params = self.params()
		varTipo = self.tipo()
		Vars = Variables.variables()
		Block = self.block()
		return Id, Params, varTipo, Vars, Block 
	
	def block(self):#<Block>::=[<estatuto>]; [<Block>]
		Block = []
		varEstatuto = self.estatuto()
		Block.append(self.block)
		return varEstatuto, Block
	
	def estatuto(self):#<estatuto>::=<si>|limpiar|<desde>|<repetir>|<mientras>|<cuando>|<regresa>|
					   #<asigna>|<lproc>|<imprime>|<imprimenl>|<leer>|interrumpe|continua
		varEstatuto = ''
		return varEstatuto

	def si(self):#<si>::=si(<Exprlog>) hacer [<BckEsp>] [sino[<BckEsp>]]
		varIf = self.exprLog()
		varDo = self.bckEsp()
		varElif = self.exprLog()
		return varIf, varDo, varElif

	def bckEsp(self):#<BckEsp>::=[<estatuto>]|inicio [<Block>] fin
		varEstatuto = self.estatuto()
		varBlock = self.block()
		return varEstatuto, varBlock

	def desde(self):#<desde>::=desde el valor de <asigna> hasta <exp> [inc|decr CteEnt] [<BckEsp>]
		Asigna = self.asigna()
		Exp = self.exp()
		incremento = 0
		BackEsp = self.bckEsp()
		return Asigna, Exp, incremento, BackEsp

	def repetir(self):#<repetir>::=repetir [<Block>] hasta que (<Exprlog>)
		Block = self.block()
		ExprLog = self.exprLog()
		return Block, ExprLog

	def mientras(self):#<mientras>::=mientras se cumpla que (<Exprlog>) [<BckEsp>]
		ExprLog = self.exprLog()
		BckEsp = self.bckEsp()
		return ExprLog, ExprLog

	def asigna(self):#<asigna>::= Id[<Udim>]:=< Exprlog >
		Id = ''
		Udim = self.udim()
		ExprLog = self.exprLog()
		return Id, Udim, ExprLog

	def cuando(self):#<cuando>::=cuando el valor del Id inicio <GpoSea>[otro:[<BckEsp>]] fin
		Id = ''
		GpoSea = self.gpoSea()
		BckEsp = self.bckEsp()
		return Id, GpoSea, BckEsp

	def gpoSea(self):#<GpoSea>::=sea<GpoConst>:[<BckEsp>][<GpoSea>]
		GpoSea = []
		GpoConst = self.gpoConst()
		BckEsp = self.bckEsp()
		GpoSea.append(GpoSea())
		return GpoConst, BckEsp, GpoSea

	def gpoConst(self):#<GpoConst>::=<cte>[,<GpoConst>]
		GpoConst = []
		cte = ''
		GpoConst.append(self.gpoConst())
		return cte,GpoConst

	def udim(self):#<Udim>::=[<Expr>][<Udim>]
		Udim = []
		Expr = self.expr()
		Udim.append(self.udim())
		return Expr, Udim

	def regresa(self):#<regresa>::=regresa[(<Exprlog>)]
		ExprLog = self.exprLog()
		return ExprLog
	
	def exprLog(self):#<Exprlog>::=<Opy>[o <Exprlog>]
		ExprLog = []
		varOpy = self.opY()
		ExprLog.append(self.exprLog)
		return varOpy, ExprLog
	
	def opY(self):#<Opy>::=<Opno> [y <Opy>]
		OpY = []
		OpNo = self.opNo()
		OpY.append(self.opY)
		return OpNo, OpY

	def OpNo(self): #<Opno>::=[no] <Oprel>
		OpRel = self.opRel()
		return OpRel

	def opRel(self): #<Oprel>::=<Expr>[<|>|<=|>=|<>|=<Oprel>]
		OpRel = []
		Expr = self.expr()
		OpRel.append(self.opRel)
		return Expr, OpRel

	def expr(self):#<Expr>::=<Multi>[+|-<Expr>]
		Expr = []
		Multi = self.multi()
		Expr.append(self.expr())
		return Multi, Expr

	def multi(self):#<Multi>::=<Expo>[*|/|%<Multi>]
		Multi = []
		Expo = self.expo()
		Multi.append(self.multi)
		return Expo, Multi

	def expo(self):#<Expo>::=<signo>[^<Expo>]
		Expo = []
		Signo = self.signo()
		Expo.append(self.expo())
		return Signo, Expo

	def signo(self):#<signo>::=[-]<termino>
		Signo = ''
		Termino = self.termino()
		return Signo, Termino

	def termino(self):#<termino>::=Id[lfunc|<Udim>]|(<Exprlog>)|CteEnt|CteReal|CteAlfa|verdadero|falso
		Id = ''
		varDim = ''
		ExprLog = self.exprLog()
		valor = ''
		return Id, varDim, ExprLog, valor

	def lproc(self):
		Id = ''
		Uparams = self.uParams()
		return Id, Uparams

	def lfunc(self):
		Id = ''
		Uparams = self.uParams()
		return Id, Uparams

	def imprime(self):
		GpoExp = self.gpoExp()
		return GpoExp

	def imprimeNL(self):
		GpoExp = self.gpoExp()
		return GpoExp + "\n"

	def gpoExp(self):
		GpoExp = []
		ExprLog = self.exprLog()
		GpoExp.append(self.gpoExp())
		return ExprLog, GpoExp

	def uParams(self):
		Uparams = []
		ExprLog = self.exprLog()
		Uparams.append(self.uParams)
		return ExprLog, Uparams

	def limpia(self):
		limpia = ''

	def leer(self):
		Id = ''
		Udim = self.udim()
		return Id, Udim









class ProtoFuncionProc():
	def __init__(self):
		pass

	def tipo(self):
		varTipo = ''
		#entero|real|alfabetico|logico
		#TT_INT|TT_FLOAT|TT_STRING|TT_BOOL
		return varTipo

	def params(self):
		Params = []
		GpoPars = self.gpoPars()
		Tipo = self.tipo()
		Params.append(self.params)
		return GpoPars, Tipo, Params

	def gpoPars(self):
		#if()
		Pars = []
		Id = ''
		Pars.append(self.gpoPars)
		return Id, Pars

	def procedimiento(self):
		Id = ''
		Params = self.params()
		Vars = Variables.variables()
		Block = self.block()
		return Id, Params, Vars, Block

	def funcion(self):
		Id = ''
		Params = self.params()
		varTipo = self.tipo()
		Vars = Variables.variables()
		Block = self.block()
		return Id, Params, varTipo, Vars, Block

	def protFunc(self):
		Id = ''
		Params = self.params()
		varTipo = self.tipo()
		return Id, Params, varTipo

	def protProc(self):
		Id = ''
		Params = self.params()
		return Id, Params

	def ProtFuncProc(self):
		ProtFuncProc = []
		ProtOpc = ''
		ProtFuncProc.append(ProtFuncProc)
		return ProtOpc, ProtFuncProc


def runSyntax(tokens):
	aux = tokens.copy()
	varConst = Constantes()
	varVariables = Variables()
	varFunciones = FuncProcedimiento()
	while True:
		auxToken = aux[0]
		if auxToken.type == 'PALRES':
			if auxToken.value == 'constantes':
				aux.pop(0)
				while True:
					auxToken = aux[0]
					if auxToken.type == 'IDENTIFICADOR':
						varConst.constantes(aux)
					elif auxToken.type == 'NL' or auxToken.type == 'TAB':
						aux.pop(0)
						continue
					elif auxToken.type == 'PALRES' and auxToken.value != 'constantes':
						break
					else:
						IllegalSyntaxError(auxToken.line, "Sintactico", "Se esperaba identificador", auxToken.value)
						break
					aux.pop(0)
				continue
			elif auxToken.value == 'variables':
				aux.pop(0)
				while True:
					auxToken = aux[0]
					if auxToken.type == 'NL' or auxToken.type == 'TAB':
						aux.pop(0)
						continue
					else:
						break
				varVariables.variables(aux)
				varVariables.variables(aux)	
				varVariables.variables(aux)	
				varVariables.variables(aux)	

			elif auxToken.value == 'Funcion':
				aux.pop(0)
				while True:
					auxToken = aux[0]
					if auxToken.type == 'NL' or auxToken.type == 'TAB':
						aux.pop(0)
						continue
					else:
						break
				varFunciones.funcion(aux)		

		aux.pop(0)
		if len(aux) == 0:
			break



		

