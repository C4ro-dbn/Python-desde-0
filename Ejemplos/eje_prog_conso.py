#Ejemplo de programa consola
#validaion de un valor (numero entero)
x = int(input("Please enter an integer: "))
#validacion; si el valor ingresado (x) es menor o igual
if x < 0:
    x = 0
    #Imprimir valor
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')