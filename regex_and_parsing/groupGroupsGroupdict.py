import re

if __name__ == "__main__":
    S = input()
    m = re.match(r".*?([A-Za-z0-9])\1.*", S)

    if m:
        print(m.group(1))
    else:
        print("-1")

"""
Esta expresión regular tiene una estructura similar a la anterior, pero con algunas diferencias. Vamos a desglosar cada parte:

    1.- '.*?': Esto representa cualquier número (incluyendo cero) de caracteres (.*), pero el 
    cuantificador ? hace que la coincidencia sea "no codiciosa" o "perezosa", buscando la coincidencia más
    corta posible.

    2.- '(\w)': Captura un único carácter de palabra (\w). \w coincide con cualquier carácter alfanumérico 
    (letras, números y guiones bajos).

    3.- '\1': En este caso, '\1' es una referencia al primer grupo de captura. Indica que se espera encontrar
    el mismo carácter que fue capturado anteriormente en el grupo de captura.

    4.- '.*': Finalmente, cualquier número (incluyendo cero) de caracteres al final.
"""
