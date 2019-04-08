# Obtener una lista de "repetidos" que sólo
# tenga los elementos repetidos de una lista inicial.
# Reto: hacerlo en una sola línea...

# Asignamos la lista de prueba
lista = [1, 3, 1, 2, 4, 5, 3, 6, 2, 7, 7, 8]

# Obtener los repetidos:
# 1. exec("tmp=lista[:]") para trabajar con un duplicado...
# ...y como "exec" devuelve None, usamos "or" para evaluar a la derecha
# 2. tmp.remove(item): va eliminando items de la lista...
# ...sacando cada item a eliminar del conjunto de items únicos...
# ...al terminar, en "tmp" sólo quedan items que estaban repetidos...
# ... y con "and" forzamos a evaluar la parte derecha
# 3. "set" nos deja sólo los items repetidos...
# ...y con "list" nos quedamos con una lista (por si el set estuviera vacío)
repes = exec("tmp=lista[:]") or\
    [tmp.remove(item) for item in set(tmp)] and\
    list(set(tmp))
print(repes)
