## RoadMap - Retos de programacion Creado con
## 🤍 (y gracias a ti) por MoureDev by Brais Moure.

## https://retosdeprogramacion.com/roadmap/

## 01 Operadores y estructuras de control

"""
/*
 * EJERCICIO:
 * # Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * # Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * # Debes hacer print por consola del resultado de todos los ejemplos.
 *

 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
##

# Estos son los diferentes tipos de operadores en Python:

# Operadores aritméticos
sums = 2 + 2
print(sums)
subtract = 3 - 5
print(subtract)
multi = 3 * 7
print(multi)
div = 4 / 8
print(div)
mod = 16 % 3
print(mod)
poten = 12**4
print(poten)
div_resul_num_entero = 18 // 5
print(div_resul_num_entero)

# Operadores relacionales
may = 26>3
print (may)
men = 4<15
print (men)
igl = 5==5
print (igl)
may_ugl = 120>=0
print (may_ugl)
men_ugl = 0<=120
print (men_ugl)
dif = 6!=35
print (dif)

# Operadores Bit a Bit
y = 10&11
o = 10|11
xor = 10 ^11
bina= ~(1000000) = (11111101)

# Operadores de asignación
a = a + 5
a = a - 5
a = a * 3
a = a / 3
a = a % 3
a = a ** 3
a = a // 3
a = a & 3
a = a | 3
a = a ^ 3
a = a >> 3
a = a << 3

# Operadores lógicos
y = a and b
o = a or b
no = not a

# Operadores de pertenencia
a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print (3 in a) # Muestra True 
#No está 12 en la lista a?
print (12 not in a) # Muestra True

# Operadores de identidad
a = 3
b = 3  
c = 4
print (a is b) # muestra True
print (a is not b) # muestra False
print (a is not c) # muestra True

## Estructuras de control

edad = 18
if edad < 18:
    print("Menor de edad")
elif edad >= 18:
    print("Mayor de edad")
else:
    print("Este código nunca se ejecutará")
# --
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
# --
contador = 0
while contador < 3:
    print("Dentro del bucle")
    contador += 1

##

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for num in range(10, 55):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print (num)
