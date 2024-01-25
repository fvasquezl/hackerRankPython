import re

<<<<<<< HEAD
cadena = "..12345678910111213141516171820212223"

# Definir la expresión regular para encontrar grupos de dígitos iguales
expresion_regular = re.compile(r"(\d)\1*")

# Usar findall para obtener todos los grupos
grupos = expresion_regular.findall(cadena)

print(grupos)
=======
if __name__ == "__main__":
    S = "__commit__"

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
>>>>>>> d98ce89bdc4c928db459b6f1c69d7fefb38243da
