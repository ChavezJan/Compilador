----------------------------------------------------
	TOKEN			LEXEMA
----------------------------------------------------
	PalRes			constantes
	Ident			PI
	OpAsig			:=
	CteReal			3.141592
	Delim			;
	Ident			MAX
	OpAsig			:=
	CteEnt			30
	Delim			;
	PalRes			variables
	Ident			i
	Delim			,
	Ident			j
	Delim			,
	Ident			k
	Delim			,
	Ident			n
	Delim			:
	PalRes			Entero
	Delim			;
	Ident			Alfa
	Delim			,
	Ident			Beta
	Delim			:
	PalRes			Alfabetico
	Delim			;
	PalRes			Funcion
	Ident			FacRec
	Delim			(
	Ident			n
	Delim			:
	PalRes			Entero
	Delim			)
	Delim			:
	PalRes			Entero
	Delim			;
	PalRes			Funcion
	Ident			FacIter
	Delim			(
	Ident			n
	Delim			:
	PalRes			Entero
	Delim			)
	Delim			:
	PalRes			Entero
	Delim			;
	PalRes			Procedimiento
	Ident			Selecciona
	Delim			(
	Delim			)
	PalRes			variables
	Ident			opc
	Delim			:
	PalRes			alfabetico
	Delim			;
	PalRes			Inicio
	PalRes			Repetir
	PalRes			Imprime
	Delim			(
	CteAlfa			"Dame un numero: "
	Delim			)
	Delim			;
	PalRes			lee
	Delim			(
	Ident			n
	Delim			)
	Delim			;
	PalRes			Imprime
	Delim			(
	CteAlfa			"Factorial R]ecursivo I]nteractivo S]alir: "
	Delim			)
	Delim			;
	PalRes			Lee
	Delim			(
	Ident			opc
	Delim			)
	Delim			;
	PalRes			Cuando
	PalRes			el
	PalRes			valor
	PalRes			de
	Ident			opc
	PalRes			Inicio
	PalRes			Sea
	CteAlfa			"R"
	Delim			,
	CteAlfa			"r"
	Delim			:
	PalRes			imprimenl
	Delim			(
	CteAlfa			"Factorial Recursivo de "
	Delim			,
	Ident			n
	Delim			,
	CteAlfa			" es= "
	Delim			,
	Ident			FacRec
	Delim			(
	Ident			n
	Delim			)
	Delim			)
	PalRes			Sea
	CteAlfa			"I"
	Delim			,
	CteAlfa			"i"
	Delim			:
	PalRes			imprimenl
	Delim			(
	CteAlfa			"Factorial Iterativo de "
	Delim			,
	Ident			n
	Delim			,
	CteAlfa			" es= "
	Delim			,
	Ident			Faciter
	Delim			(
	Ident			n
	Delim			)
	Delim			)
	PalRes			Otro
	Delim			:
	PalRes			Si
	Delim			(
	Ident			opc
	OpRel			<>
	CteAlfa			"S"
	OpLog			y
	Ident			opc
	OpRel			<>
	CteAlfa			"s"
	Delim			)
	PalRes			hacer
	PalRes			Imprimenl
	Delim			(
	CteAlfa			"Opcion Invalida!!!"
	Delim			)
	PalRes			Fin
	Delim			;
	PalRes			hasta
	PalRes			que
	Delim			(
	Ident			opc
	OpRel			=
	CteAlfa			"S"
	OpLog			o
	Ident			opc
	OpRel			=
	CteAlfa			"s"
	Delim			)
	Delim			;
	PalRes			Fin
	PalRes			de
	PalRes			Procedimiento
	Delim			;
	PalRes			Funcion
	Ident			FacRec
	Delim			(
	Ident			n
	Delim			:
	PalRes			entero
	Delim			)
	Delim			:
	PalRes			Entero
	PalRes			Inicio
	PalRes			Si
	Delim			(
	Ident			n
	OpRel			<
	CteEnt			2
	Delim			)
	PalRes			hacer
	PalRes			regresa
	Delim			(
	CteEnt			1
	Delim			)
	PalRes			sino
	PalRes			regresa
	Delim			(
	Ident			FacRec
	Delim			(
	Ident			n
	OpArit			-
	CteEnt			1
	Delim			)
	OpArit			*
	Ident			n
	Delim			)
	Delim			;
	PalRes			Fin
	PalRes			de
	PalRes			Funcion
	Delim			;
	PalRes			Funcion
	Ident			FacIter
	Delim			(
	Ident			n
	Delim			:
	PalRes			Entero
	Delim			)
	Delim			:
	PalRes			Entero
	PalRes			Variables
	Ident			Facto
	Delim			:
	PalRes			Entero
	Delim			;
	PalRes			Inicio
	Ident			Facto
	OpAsig			:=
	CteEnt			1
	Delim			;
	PalRes			Desde
	PalRes			el
	PalRes			valor
	PalRes			de
	Ident			i
	OpAsig			:=
	Ident			n
	PalRes			hasta
	CteEnt			2
	PalRes			decr
	CteEnt			1
	Ident			Facto
	OpAsig			:=
	Ident			Facto
	OpArit			*
	Ident			i
	Delim			;
	PalRes			regresa
	Delim			(
	Ident			facto
	Delim			)
	Delim			;
	PalRes			Fin
	PalRes			de
	PalRes			Funcion
	Delim			;
	PalRes			Programa
	PalRes			limpia
	Delim			;
	Ident			k
	OpAsig			:=
	CteEnt			3
	Delim			;
	Ident			Selecciona
	Delim			(
	Delim			)
	Delim			;
	PalRes			Imprime
	Delim			(
	CteAlfa			"Dame tu nombre: "
	Delim			)
	Delim			;
	PalRes			Lee
	Delim			(
	Ident			alfa
	Delim			)
	Delim			;
	PalRes			Imprime
	Delim			(
	CteAlfa			"Dame tu Apellido: "
	Delim			)
	Delim			;
	Ident			beta
	OpAsig			:=
	CteAlfa			"Villalvazo"
	Delim			;
	PalRes			Imprimenl
	Delim			(
	Ident			beta
	Delim			)
	Delim			;
	PalRes			Imprimenl
	Delim			(
	Ident			k
	Delim			)
	Delim			;
	PalRes			Fin
	PalRes			de
	PalRes			programa
	Delim			.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      