import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # Se ingresa la cantidad de n intervalos que se poseen
b = float(input("Último límite de integración: " ))  # Se ingresa el número del último límite de integración (eje x normalmente)
a = float(input("Primer límite de integración: " ))  # Se ingresa el númerl del primer límite de integración (eje x normalmente)
delta_x = (b-a)/n  # Se cálcula delta de x
diccionario = {}  # En este diccionario van a estar todas las parejas ordenadas
Resultado = 0  # Se asigna un resultado con una variable para poder manipular a futuro

for i in range(n+1):  # Se pide que se repita la acción de pedir datos n número de veces
    x = input("Valor x de la pareja ordenada: " ) # Se pide la coordenada x
    try:     #Verificación del x para ver si es una fracción o no
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO SE ENCUENTRA EN EL DOMINIO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # Se pide la coordenada y
    try:    #Verificación del y para ver si es una fracción o no
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # x and y se almacenan en el diccionario

#OPERACIÓN PARA LA REGLA DEL TRAPECIO
diccionario.pop(b)
for i in diccionario.values():
    Resultado += i

Resultado *= delta_x
print(Resultado)