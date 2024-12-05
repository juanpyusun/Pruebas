# Indice
1. **Introducción a Python**
   - Caracteristicas del lenguaje frente a otros
   
2. **Sintaxis básica**
   - PEP 8
   - Palabras reservadas
   - Comentarios
   - Comandos especiales

3. **Variables y tipos de datos**
   - Variables
   - Conversión de tipos

4. **Operadores**
   - Operadores aritméticos
   - Operadores de asignación
   - Operadores relacionales
   - Operadores lógicos

5. **Entrada y salida de datos**
   - Entrada por teclado
   - Salida por pantalla

6. **Control de flujo**
   - Estructuras condicionales
   - Estructuras cíclicas

7. **Funciones**
   - Definición y uso de funciones
   - Parámetros y retorno de valores
   - Funciones Built-In
   - Funciones lambda
   - Decoradores
   - Paradigma Funcional

8. **Manejo de errores y excepciones**
   - Introducción a excepciones
   - Manejo de errores

9. **Estructuras de datos**
    - Listas, tuplas, conjuntos, conjunto congelado y diccionarios
    - Generadores
    - Iteradores e iterables
    - Linked List
    - Double Linked List
    - Cola
    - Pila
    - Arbol
    - Heap

10. **Programación Orientada a Objetos (POO)**
    - Clases y objetos
    - Herencia y polimorfismo

11. **Manejo de librerías**
    - Importación de librerías
    - Bibliotecas útiles

12. **Otros**
    - REGEX
    - Entornos virtuales

***
# 1. Introduccion a Python
- **Interpretado**: Python se ejecuta línea por línea, lo que facilita la depuración y el desarrollo interactivo.
- **Tipado dinámico**: Permite que las variables cambien de tipo en tiempo de ejecución, lo que brinda flexibilidad al programador.
- **Fuertemente tipado**: No se permite la conversión implícita entre tipos incompatibles, lo que ayuda a evitar errores sutiles.
- **Multiparadigma**: Soporta diferentes estilos de programación, incluyendo programación orientada a objetos y programación funcional.
- **Multiplataforma**: Python se puede ejecutar en diferentes sistemas operativos sin necesidad de modificar el código.
- **Multipropósito**: Es utilizado en diversas áreas como desarrollo web, ciencia de datos, automatización, inteligencia artificial, entre otros.
- **Alto nivel**: Ofrece una sintaxis más abstracta y fácil de usar en comparación con lenguajes de bajo nivel.
- **TODO ES UN OBJETO**: En Python, casi todo es un objeto, lo que permite un enfoque orientado a objetos en todos los aspectos del lenguaje.
- **Indentación**: La correcta indentación es crucial, ya que define la estructura del código en Python.
- **Revisar las PEP**: Familiarízate con las Python Enhancement Proposals, que ofrecen guías y estándares para la mejora del lenguaje.

***
# 2. Sintaxis Basica

## PEP 8
las Python Enhancement Proposals, son guías y estándares para la mejora del lenguaje, en el caso particular de la octava guia (PEP-8) se define todos los principios de buenas practicas y el estandar del codigo python, entre las que menciona la correcta identificacion de objetos y la identacion, asi como otros detalles del uso de espacios entre todos los simbolos usados

## Palabras Reservadas
Al usar identificadores en python, se deben evitar el uso de las siguientes palabras:
| Colum1 | Colum2 | Column3 | Column4 |
| :-: | :-: | :-: | :-: |
| False | class | from | or |
| None | continue | global | pass |
| True | def | if | raise |
| and | del | import | return |
| as | else  | in | try |
| assert | except | is | while |
| async | elif | not | with |
| await | finally | lambda | yield |
| break | for | nonlocal | |

## Comentarios
- De una linea: `# Usando numeral`
- De varias lineas, usando comillas simples o dobles
```python
'''
de varias lineas
'''
```
```python
"""
de varias lineas
"""
```

## Comandos especiales
* `help()` o `help(comando/objeto)`: Ayuda en general o de algun comando
* `type(objeto)`: Clase del objeto
* `dir(objeto)`
* `repr(objeto)`
* `coerce(var1, var2)`: En que tipo de datos quedara la operacion entre ambos
* `id(objeto)`: Direccion en memoria del objeto
* `hash(objeto)`: Valor Hash del objeto
* `isinistance(objeto, clase)`: Comprueba si el objeto pertenece a la clase
* `del(objeto)`: Eliminar objeto
* `import this`: Zen de python

***
# 3. Variables y tipos de datos
Toda variable en python requiere un identificador que cumpla las siguientes reglas, ademas de las buenas practicas de camelCase:
- No usar palabras reservadas
- Se diferencian entre mayusculas y minusculas
- Se puede usar letras, numeros y guion bajo
- Debe empezar en letra o guion bajo
- Seguir recomendacios en PEP8

Ademas cumple la siguiente estructura:  
`identificador = valor`  
`variable:tipo`  
`variable:tipo = valor`

### **Tipos de variables**
| Nombre | Tipo | Ejemplos |
| :-: | :-: | :-: |
| Booleano | bool | `True or False` |
| Entero | int | `21, 200, 34_500` |
| Flotante | float | `3.14, 1.5e3, 1.93e-3` |
| Complejo | complex | `3 + 4j` |
| Cadena | str | `"hola mundo", 'hola python'` |

Para las cadenas de texto, python reconoce los caracteres UNICODE

## Conversión Implícita
Es el proceso donde Python convierte automáticamente un tipo de dato a otro sin necesidad de que el programador lo especifique. Ocurre principalmente entre tipos compatibles, como entre enteros (`int`) y flotantes (`float`), lo cual facilita operaciones aritméticas y combinaciones de tipos en ciertas situaciones. Pero puede llegar a generar errores si no se sabe como funciona correctamente, se puede usar la funcion `coherce(var1, var2)` para determinar si existe una conversion implicita entre ambas variables, y saber como quedara el resultado.

## Conversion explicita
Es el proceso donde el programador especifica explícitamente la conversión de un tipo de dato a otro utilizando funciones de conversión. Se utiliza cuando es necesario cambiar un tipo de dato incompatible a un tipo compatible.Aumenta la claridad del código al hacer evidente la intención del programador.
Entre las conversiones explicitas mas comunes, estan:
- `int(objeto)`
- `float(objeto)`
- `int(objeto)`

***
# 4. Operadores
## Operadores aritmeticos
  - Suma: `+`
  - Resta: `-`
  - Producto: `*`
  - Division: `/`
  - Division entera: `//`
  - Residuo / modulo: `%`
  - Potencia: `**`

## Operadores de asignacion
Los mas usados son:
- Asignacion simple: `x = 1`
- Asignacion multiple `x, y = 1`
- Asignacion multiple, multiple valores (Desempacamiento): `x, y = 1, 2`
  - Puede usarse para intercambiar valores sin necesidad de una variable temporal: `x, y = y, x`
- Asignacion del tipo: `pi:float`
- Asignacion de valor y tipo: `pi:float = 3.14`
- Walrus operador: asigna a la vez que "ejecuta la linea"
```
x = 10
y = 20
print(x + y) # Muestra la suma normal
print(suma := x + y) # Muestra la suma normal y ademas, almacena en variable suma el resultado
print(f"{suma = }") # comprobamos que suma si pudo guardar el valor
```
entonces, permite asignar y no "interrumpe" la ejecucion de la linea, toda expresion walrus debe ir entre parentesis, con la siguiente estructura:
```
(variable := expresion)
```
- Asignacion aumentada
  - Suma: `x += a`
  - Resta: `x -= a`
  - Producto: `x *= a`
  - Division: `x /= a`
  - Division entera: `x //= a`
  - Residuo / modulo: `x %= a`
  - Potencia: `x **= a`

## Operadores logicos
- De elemento a contenedor
  - `in`
  - `not in`
- De objeto a objeto
  - `is`
  - `is not`
- Negacion `not`
- Conjuncion `and`
- Disyuncion `or`

## Operadores de relacion
Se tienen que tomar como preguntas
- es A mayor que B `A > B`
- es A mayor o igual que B `A >= B`
- es A menor que B `A < B`
- es A menor o igual que B `A <= B`
- es A igual a B `A == B`
- es A distinto a B `A != B`

## Operadores logicos y de relacion combinados
la operacion `x > 0 or x < 10` , se puede ver como `0 < x < 10`

## Jerarquia de operadores logicos
De mayor a menor:
1. Parentesis
2. Negacion
3. Conjuncion
4. Disyuncion

***
# 5. Entrada y salida de datos
- Entrada de datos `inpunt(prompt)`
- Salida de datos `print(object)`

En ambos casos se suelen usar caracteres de escape o formatos de cadenas

## Caracteres de escape
- `\n`: Salto de linea
- `\t` : Tabulacion
- `\r` : Retroceso
- `\` : Salto de lineas largas
- `\" or \'`: Muestra las comillas dobles o simples
- `r" "`: raw text
- `f" "`: formated text

## Formato
- con `%`
  - `%s` : cadena u objeto iterable
  - `%d` : decimales
  - `%f` : numero coma flotante

- Con el metodo string.format() : `"dentro de las comillas poner {} y {}".format(var1, var2)`

- Con f-string: `f"cadena de texto {variable:formato}"`
    - `f"{variable=}"` muestra el identificador y el valor almacenado
    - `f"{variable!r}"` igual que tener `repr(variable)`
    - `f"{variable!s}"` igual que tener `str(variable)`
    - `f"{variable!a}"` igual que tener `ascci(variable)`
    - `f"{variable:<}"` left align
    - `f"{variable:>}"` right align
    - `f"{variable:=}"` center align
     - `f"{variable:+}"` usar signo positivo
    - `f"{variable:-}"` usar signo negativo
    - `f"{variable: }"` Deja vacio para positivos, usa - para negativos
    - `f"{variable:,}" or f"{variable:_}"` Usa separadores de miles
    - Ejemplo:  
    `f"{resultado:>10.2f}"` Alineara a la derecha con 10 caracteres, mostrando dos decimales unicamente

## Input from shell
Se puede ejecutar directamente desde consola el script y pasarle argumentos
```sh
!python3 miDocumento.py "primer argumento" "segundo argumento" 3 4 5 6 7 8 9 10
```

y se importa la ***Libreria `sys`***
Entre los metodos y atributos que posee esta libreria, tenemos a:
```py
sys.args
```
Este argumento recibira los parametros con los que se llame al script python desde consola, siendo:
```py
sys.args[0]
```
el nombre del script **miDocumento.py**, los siguientes elementos de la lista son los que acompañan, en este ejemplo seria:
```py
sys.args[1] -> "primer argumento"
sys.args[2] -> "segundo argumento"
sys.args[3] -> 3
sys.args[4] -> 4
sys.args[5] -> 5
sys.args[6] -> 6
sys.args[7] -> 7
sys.args[8] -> 8
sys.args[9] -> 9
sys.args[10] -> 10
```

***
# 6. Control de flujo
## Estructuras condicionales
- Operador ternario
```python
variable = valorTrue if condicion else valorFalse
```
- if-elif-else
```python
if condicion1 :
  # proceso
elif condicion2 :
  # proceso
else :
  # proceso
```
- match - case
```python
match variable:
  case val1:
    # codigo
  case val2:
    # codigo
  case _:
    # codigo si no se cumplen las anteriores
```

## Estructuras ciclicas
- For
```python
for elemento in iterable:
  #codigo
else:
  #codigo
```
- While
```python
while condicion:
  #codigo
else:
  #codigo
```

En ambas estructuras se pueden usar tanto `break` como `continue`, los cuales cortan en la iteracion actual u omiten la iteracion actual respectivamente, y en ambas casos se activara el bloque `else` mientras el ciclo termine normalmente sin usar estas dos palabras reservadas

***
# 7. Funciones
Bloques de codigo que reciben (o no) argumentos, ejecuta lineas y luego retorna (o no) un valor u objeto
## Estructuras comunes de las funciones
- Estructura basica
```python
def nombreFuncion(parametros):
  return objeto
```
- Cantidad definida de parametros
```python
def nombreFuncion(par1, par2, ... , par_n):
  return objeto
```
- Cantidad indefinida de parametros
```python
def nombreFuncion(*args):
  return objeto
```
- Con una llave-valor (o valor por default)
```python
def nombreFuncion(val = a):
  return objeto
```
- Con una cantidad indefinida de llave-valor
```python
def nombreFuncion(**kwargs):
  return objeto
```
- Con buenas practicas
```python
def nombreFuncion(val1:int, val2:int = 0)->int:
  return objeto
```


## Funciones anonimas
```python
variable = lambda parametros : expresion_de_salida
cuadrado = lambda x : x**2
```
## Funciones sobre iterables
- `filter(funcion, iterable)`: Devuelve los valores que cumplen True la conidicion de la funcion
- `map(funcion, iterable)`: Modifica cada elemento segun la funcion
- `zip(iterable1, iterable2)`: Combina los elementos de las mismas posiciones
- `reduce(funcion, iterable)`: Sirve como acumulador dentro de un iterable

## Decoradores
Son funciones que añaden funcionalidades a otras funciones, "decoran" otras funciones, su estructura es:
```python
def funcion_decoradora(funcion_parametro):
  def funcion_interna():
    # Codigo
    return funcion_parametro()
  return funcion_interna
```
Que con decoradores queda:
```python
@funcion_decoradora
def funcion_decorada():
  # Codigo
```
Se necesitan tres funciones A, B y C, tal que, A recibe como parametro a B para devolver C, ademas se retorna funcion_interna sin parentesis, dado que al poner los parentesis la ejecuta, se desea devolver sin ejecutarla.

El arroba indica que la funcion exactamente inferior se decorara

***
# 8. Estructuras de datos
![Untitled-2024-07-31-1039.png](data:image/png;base64,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)

## Tipos de contenedores
| Nombre | Tipo | Ordenado | Indexable | Mutable | iterable | Admite repetidos | Ejemplos |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Lista | list | SI | SI | SI | SI | SI | `[2,3,4,5]` |
| Tupla | tuple | SI | SI | NO | SI | SI | `(2,3,4,5)` |
| Conjunto | set | NO | NO | SI | SI | NO | `{2,3,4,5}` |
| Diccionario | dict | SI | NO | SI | SI | NO | `{"nombre": "Juan", "edad": 30}` |
| Cadena | str | SI | SI | NO | SI | SI | `"esta es una cadena"` |
| Conjunto Congelado | frozenset | NO | NO | NO | SI | NO | `frozenset({2,3,4,5})` |

## Operadores con contenedores
| Tipo | Operadores |
| :-: | :-: |
| Lista | [i], [::], +, *, in / not in , <, <=, >, >=, ==, !=, len(), max(), min(), sum() |
| Tupla | igual que en listas |
| Conjunto | \|, c, -, ^, in / not in, los que siguen de listas... |
| Diccionario | igual que listas excepto slicing y mayor/menor|
| Cadena | igual que listas |
| Conjunto Congelado | igual que conjuntos |

## Generadores

```python
# Ejemplo de un Generador
def squares(n):
  for i in range(1, n+1):
    yield i**2

squares_gen = squares(5)

for num in squares_gen:
  print(num)
```

## Iterables e Iteradores
Se usan comunmente para:
- Procesamiento de grandes Datasets
- Data Streaming
- Secuencias infinitas

```python
# Ejemplo de objeto iterable
fruits = ["apple", "banana", "cherry"]

fruits_iter = iter(fruits)

# Ejemplo de iteracion dentro del objeto
print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))
# print(next(fruits_iter))
```

```python
# Ejemplo de un iterador infinito
def count(start):
  while True:
    yield start
    start += 1

count_gen = count(1)

for num in count_gen:
  print(num)
  if num >= 5:
    break
```

***
# 9. Manejo de errores y excepciones

***
# 10. POO
La Programacion Orientada a Objetos es un paradigma, un estilo de solucion de problemas, enfocada en Objetos, en los conjuntos de ___comportamientos___ y ___atributos___ repetidos en las distintas estructuras.

Componentes principales de una clase
- Identificador que cumpla las PEP8
- Atributos
- Metodos (OBLIGATORIO el constructor)

Teniendo en cuenta que **TODO** en Python es un objeto, es decir, en este contexto, toda clase es una subclase de la clase Objeto, por ende, heredara todos sus atributos y metodos por defecto, incluido el constructor.

## Pilares de la POO
- Encapsulamiento
- Abstraccion
- Herencia
- Polimorfismo

## Reglas y Principios aplicados en POO
Sigue una serie de reglas y principios para poder estructurar el codigo en forma de Clases (conjuntos) y Objetos (elementos) de manera efectiva, aumentando su legibilidad, mantenibilidad y reutilización., entre los cuales se encuentra:

- SOLID: Es un acrónimo que representa cinco principios fundamentales de diseño que ayudan a crear software más entendible y mantenible.
    - **S** - **Single Responsibility Principle (SRP)**:  Una clase debe tener una sola razón para cambiar, lo que significa que debe tener una única responsabilidad o función. Esto evita que una clase se vuelva demasiado compleja y difícil de mantener.
    
    - **O** - **Open/Closed Principle (OCP)**: Las clases deben estar abiertas para su extensión, pero cerradas para su modificación. Esto permite que el comportamiento de una clase se amplíe sin alterar el código existente, generalmente mediante la herencia.
    
    - **L** - **Liskov Substitution Principle (LSP)**: Los objetos de una clase base deben ser reemplazables por objetos de una clase derivada sin alterar las propiedades deseadas del programa. Esto asegura que las subclases puedan ser utilizadas sin problemas en lugar de sus clases base.
    
    - **I** - **Interface Segregation Principle (ISP)**: Los clientes no deben estar obligados a depender de interfaces que no utilizan. Esto significa que es mejor tener varias interfaces específicas en lugar de una única interfaz general.
    
    - **D** - **Dependency Inversion Principle (DIP)**:Las dependencias deben ser abstraídas. Los módulos de alto nivel no deben depender de módulos de bajo nivel; ambos deben depender de abstracciones (por ejemplo, interfaces).

- DRY (Don't Repeat Yourself): Este principio establece que la duplicación de código debe evitarse en la medida de lo posible. Cada pieza de conocimiento debe tener una representación única en el sistema. Esto mejora la mantenibilidad del código, ya que cualquier cambio solo necesita realizarse en un lugar.

- KISS (Keep It Simple, Stupid): Este principio aboga por la simplicidad en el diseño y la implementación. La idea es que los sistemas complejos deben ser evitados y que las soluciones deben ser lo más simples posible, ya que la complejidad puede llevar a errores y a un mayor costo de mantenimiento.

- YAGNI (You Aren't Gonna Need It): Este principio sugiere que no se debe agregar funcionalidad hasta que sea necesaria. Esto evita la sobrecarga de características en el sistema y ayuda a mantener el código limpio y fácil de entender.

- Composition Over Inheritance: Este principio sugiere que se debe preferir la composición de objetos en lugar de la herencia para extender funcionalidades. La composición permite crear clases más flexibles y reutilizables, evitando la rigidez que a veces puede introducir la herencia.


## Operador de acceso a atributos y metodos de un objeto
En python, para acceder se usa el `.` punto
```py
objeto.atributo
objeto.metodo()
```

## Metodos Dunder: Double underscore
Estos métodos son utilizados para implementar funcionalidades especiales en las clases de Python.
- `__str()__`: Permite la representacion informal en cadena de texto
- `__repr()__`: Permite la representacion formal en cadena de texto

***
# 11. Manejo de librerias
## Importacion absoluta
  - Para instalar  
  `pip install <directorio>`
  - Para instalar varios desde un txt  
  `pip install -r requirements.txt`
  - Para desinstalar  
  `pip uninstall <directorio>`
  - Para actualizar  
  `pip install <directorio> --upgrade`
  - Para usar  
  `import <directorio>`
  - Para usar con alias  
  `import <directorio> as <alias>`
  - Para usar sin nombrar directorio  
  `from <directorio> import <modulo>`
  - Formato general para importar directorios en python con alias y sin nombrar el modulo  
  `from <directorio> import <modulo> as <alias>`
## Importacion Relativa
Se usa el punto, solo son validas dentro de modulos, es decir, directorios que contienen `__init__.py` y no funcionara en scripts independientes  
`from . import <modulo>` desde el mismo directorio  
`from .. import <modulo>` desde el directorio padre
***

# 12. Otros
## Entorno virtual
Es un sistema simulado e independiente con librerias cuyas versiones pueden ser aisladas de la instalacion global de python, de esta manera se evitan conflictos de librerias.
- `pip install virtualenv`
- `virtualenv venv`
- `.\venv\Scripts\activate`
- `.\venv\Scripts\deactivate`
