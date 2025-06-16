#Un METODO es una función de programación que ejecuta una tarea específica

# El método DIR nos indica todos los métodos disponibles con el tipo de dato
print(dir(str))


# capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii'
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
# 'swapcase', 'title', 'translate', 'upper', 'zfill'

nombre = 'bryan rivas'
asignatura = 'INTRODUCCION A LA PROGRAMACION'

print(nombre.capitalize())  #Devuelve texto donde solo la primera letra será mayuscula

print(nombre.title())       #Devuelve texto donde la primera letra será en Mayus y el resto no

print(nombre.upper())       #Devuelve una copia del texto en MAYUS

print(nombre.count('e'))    #Devuelve el número de veces que un elemento específico aparece en una secuencia (como una lista, cadena o tupla)

print(nombre.find('b'))     #Se utiliza para buscar la primera aparición de una subcadena dentro de una cadena dada.
                            #Si encuentra la subcadena, devuelve el índice de inicio de la misma; si no la encuentra, devuelve -1.

print(nombre.endswith('s')) #Se usa para verificar si una cadena termina con un sufijo específico. 
print(nombre.endswith('y')) #Devuelve TRUE or FALSE, segun sea el caso.   

print(nombre.join(asignatura)) #se utiliza para concatenar los elementos de un iterable (como una lista, tupla, etc.)
                               #en una sola cadena, utilizando un separador especificado. Básicamente, une varios strings en uno solo



