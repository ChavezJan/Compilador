#include <stdlib.h>
#include <stdio.h>
typedef struct nulo
{
	struct nulo * sig;
	char nombre [20];
	char tipo;
	union
	{
		char valor_char;
		int valor_int;
	}info;
} simbolo;
simbolo * crear()
{
	return NULL;
};


void insertar(p_t,s)
simbolo **p_t;
simbolo * s;`
{
	s->sig = (*p_t);
	(*p_t) = s;
};


simbolo * buscar(t,nombre)
simbolo * t;
char nombre[20];
{
	while ( (t != NULL) && (strcmp(nombre, t->nombre)) )
		t = t->sig;
	return (t);
};





void imprimir(t)
simbolo * t;
{
	while (t != NULL)
	{
		printf("%s\n", t->nombre);
		t = t->sig;
	}
};