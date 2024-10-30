# Impresion de datos en formato texto

# Se pueden imprimir con '' comillas simples o "" comillas dobles
print("Se pueden imprimir con comillas simples o comillas dobles")
print("Hola Mundo!")
print("Hola Mundo!")

# Para generar el salto de linea en textos -- alt+92 y n (\n)
print("Hola\nMundo!", "Para generar el salto de linea en textos")

# Para evitar alteracion en llamar una ruta de una carpeta utilizar la r al principio
print(
    r"C:\\User\name",
    "#Para evitar alteracion en llamar una ruta de una carpeta utilizar la r al principio",
)

# Para cadenas de texto muy grande se utliza la comilla triple mas backslash \
print(
    """\
User: Pepe [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
)

##   ---------

## cadenas de caracteres (posicionamiento de un valor en una cadena)

# se desea imprimir el segundo indice de Python
# el cual es la letra T, ya que para recorrerlo arranca desde el 0 al 5, para este caso
cadn = "Python"
cadn[2]

## Para caracteres negativos es para contar de derecha a izq
cadn[-1]

## Para segementar varias cadenas se utiliza
cadn[0:3]
cadn[2:5]

# Segmentacion positiva y negativa
"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1


La primera fila de números da la posición de los índices 0... 6 en la cadena; 
La segunda fila muestra los índices negativos correspondientes. 
El segmento de i a j consta de todos los caracteres entre los bordes etiquetados como 
i y j, respectivamente.

En el caso de los índices no negativos, la longitud de un segmento es la diferencia 
entre el índices, si ambos están dentro de los límites. 

"""
