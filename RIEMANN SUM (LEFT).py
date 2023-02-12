import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # n range of couples
b = float(input("Último límite de integración: " ))  # Last integration limit
a = float(input("Primer límite de integración: " ))  # First integration limite
delta_x = (b-a)/n  # Get Delta x
diccionario = {}  # Dictionary where all the couples are.
Resultado = 0  # Set variable equal to 0 to manipulate in the future

for i in range(n+1): 
"""Captures all the couples and add them in the dictionary"""
    x = input("Valor x de la pareja ordenada: " ) # Get x axis
    try:     # See if x is a fraction
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO SE ENCUENTRA EN EL DOMINIO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # Get y axis
    try:    # See if y is a fraction
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # x and y get updated in the dictionary

#Sum all the values and print the result of the integral
diccionario.pop(b)
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
