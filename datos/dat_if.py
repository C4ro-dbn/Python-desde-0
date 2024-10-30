# declaracion IF, sirve para validar instrucciones

#ingreso de un valor entero
vl = int (input("ingrese un numero"))
#validacion; si el valor es menor que 5 o igual que 0
if vl < 5:
    vl = 0
    # Se imprimira
    print ("Dato correcto")
#si el valor no es correcto
else:
    print ("Es diferente del resto")
