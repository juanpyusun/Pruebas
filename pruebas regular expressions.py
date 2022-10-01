import re
polinomio=input("ingrese el polinomio: ")
""" funcion que devuelve la cantidad de terminos, falla si empieza con signo + o -
def get_cantidad_terminos_polinomio(polinomio:str)->int:
    terminos=re.split(pattern =r"[-\+]",
                      string= polinomio)
    cantidad_terminos=len(terminos)
    return cantidad_terminos
"""
def get_grado_polinomio(polinomio:str)->int:
    polinomio=polinomio.lower()
    polinomio=polinomio.replace("^1","")
    polinomio.find("+"or"-")
    

string = '-10x^100   +    3x^5-4x^3+5x-10'    
print(re.sub(r'\s?([+-])\s?', lambda x: ' -' if x.group(1) == '-' else ' ', string).split())
#que hace group(1) ???? Please note that unlike string indexing, which always starts at 0, group numbering always starts at 1. https://pynative.com/python-regex-capturing-groups/
'''
expresiones regulares
re.findall("^palabra",string)   busca al principio de la cadena
re.findall("palabra$",string)   busca al final de la cadena
re.findall("[c]",string)        busca si contiene el caracter c en cualquier parte de la cadena
re.findall("[o-t]",string)      busca si dentro del string contiene caracteres entre la o y la t
re.findall("[o-t]$",string)     busca si al final del string contiene caracteres entre la o y la t
re.findall("niñ[oa]s", string)  busca si dentro del string posee la palabra niños o niñas
re.search(r"\d",texto)		busca el primer emparejamiento de digitos en la cadena
\d	digitos 0-9
\D 	no digitos
\w	caracteres (a-z, A-Z,0-9, _)   
\W	no caracteres
\s	espacio en blanco, tab, nueva linea
\S	no espacio en blanco, tab o linea
.	cualquier caracter excepto nueva linea
\ 	cancela caracteres especiales
^ 	en el comienzo de la cadena
$ 	al final de la cadena
*	0 o mas del ultimo caracter tomado findall(r"python!*","python!!!!")
+	1 o mas del ultimo caracter tomado findall(r"python!+","python!!!!")
?	toma 0 o 1 valor del ultimo caracter tomado (r"python!?","python!!!!")
{3}	toma 3 del ultimo caracter tomado findall(r"python!{3}","python!!!!")
{Valmin,Valmax}	toma Valminimo hasta Valmaximo del ultimo caracter tomado findall(r"python!{2,4}","python!!!!")
()	Grupos
[]	encuentra caracteres dentro de corchetes
[^]	encuentra caracteres distintos a los del corchete
|	condicional or
\b	caracteres (a-z, A-Z,0-9, _)     con limite a la derecha de otro caracter
\B	caracteres (a-z, A-Z,0-9, _)     SIN limite a la derecha de otro caracter
\1
'''

