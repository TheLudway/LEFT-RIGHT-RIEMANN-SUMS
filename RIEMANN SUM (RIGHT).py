import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # n number of couples
b = float(input("Último límite de integración: " ))  # Last integration limit x axis
a = float(input("Primer límite de integración: " ))  # first integration limit y axis
delta_x = (b-a)/n  # Get Delta x
diccionario = {}  # Dictionary where there are all the couples
Resultado = 0  # Variable equal to 0 and in a future it can be manipulate

for i in range(n+1):  
"""Add to the dictionary all the couples"""
    x = input("Valor x de la pareja ordenada: " ) # x coordenate
    try:     # See if x is a fraction
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO SE ENCUENTRA EN EL DOMINIO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # y coordenate
    try:    # See if y is a fraction
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # x and y get updated in the dictionary

# Sum all the values and print the solution of the integral
diccionario.pop(a)
for i in diccionario.values():
    Resultado += i

Resultado *= delta_x
print(Resultado)

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""
