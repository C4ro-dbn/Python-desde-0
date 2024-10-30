# Los ciclos FOR, sirven para recorrer areglos

# mediante un ciclo for, recorreremos 10 veces, ya que fue el rango dado o el numero de vieltas a hacer
for i in range(10):
    print (i)

# Ejemplos:

# 1. recorrer el siguiente arreglos
# 2. generarle un indice acada valor del array

persons = ['Pedro','Juan','Marcelo','Felipe','Alejandro','Simon','Lex','Julian']
#recorremos todo la array
for pers in range(len(persons)):
    #imprimimos el numero nombres que se envuentran en la array
    #llamando el a la variable persons e incliyendo pers, nos generarra el indice de cada valor
    print (pers, persons[pers])
