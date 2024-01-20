import re

cadena = "..12345678910111213141516171820212223"

# Definir la expresión regular para encontrar grupos de dígitos iguales
expresion_regular = re.compile(r"(\d)\1*")

# Usar findall para obtener todos los grupos
grupos = expresion_regular.findall(cadena)

print(grupos)
