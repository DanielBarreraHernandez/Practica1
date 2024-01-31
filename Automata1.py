from sys import exit
import re


simbolo = None
Fin = None

def caracter(character):
	global simbolo
	simbolo=""
	global Fin
	Fin=""
	digito="[0-9]"
	operador="(\+|\-|\*|\/)"
	
	if (re.match(digito,character)):
		simbolo="Digito"
		return 0
	else:
		if (re.macth(operador,character)):
			simbolo="operador"
			return 1
		else (character==Fin):
			return 2
		print ("Error el caracter:",character,"no es valido")
		exit()

def encabezado():
	print("""| Edo. Actual | Caracter | simbolo | Edo. Siguiente |""")
	body()

def contenido (estadossig,character,simbolo,estado):
	print("| ",estadosig," | ",character," | ",simbolo," | ",estado," |")
	body()

def body() :
	print("+-------------+-----------------+------------+----------+")
	
	tabla=[[1,"E","E"], ["E",2,"E"], [3,"E","E"], ["E","E","A"]]
	estado = 0

	print("""+------------------+
	|ingrese una cadena a evaluar: |
	+--------------------------+""")

cadena = input()
body()
encabezado()
	
for character in cadena:
	estadosig=estado
	charcaracter=carater(character)
	estado=tabla[estado][charcaracter]

	if (estado=="E"):
		print("| ",estadosig," | ",character," | ",simbolo," | ",estado," |")
		body ()
		print("""|cadena no valida:(
		+-----------------------------------+""")
		exit
	contenido(estadosig,character,simbolo,estado)
if(estado!=3) :
	print("""|cadena no valida:(
	+-------------------------+""")

if (estado==3):
	print("| ",estado," | | Fin Cadena | |")
	body()
	print ("""cadena valida
	+---------------------------------+""")