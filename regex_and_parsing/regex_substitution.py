import re

if __name__ == "__main__":
    TXT = "\n".join([input() for i in range(int(input()))])
    txt = re.sub(r"(?<=\s)&&(?=\s)", "and", TXT)
    txt = re.sub(r"(?<=\s)[|]{2}(?=\s)", "or", txt)
    print(txt)

"""
(?<=\s): Esto es una "búsqueda de retroceso positivo" (positive lookbehind). 
Significa que la coincidencia debe estar precedida por un espacio en blanco (\s). 
Sin embargo, el espacio en blanco no se incluirá en la coincidencia. 
Es una restricción en la parte izquierda de la cadena que quieres encontrar.

(?=\s): Esto es una "búsqueda positiva hacia adelante" (positive lookahead). 
Significa que la coincidencia debe estar seguida por un espacio en blanco (\s). 
Al igual que en el caso de la búsqueda positiva hacia atrás, el espacio en blanco 
no se incluirá en la coincidencia. Es una restricción en la parte derecha de la cadena 
que quieres encontrar.
"""
