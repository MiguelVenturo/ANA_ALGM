print ("*********Bienvenido********")
def busquedabi_iterativa(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        x = (izquierda + derecha) 
        if lista[x] == objetivo:
            return x
        elif lista[x] < objetivo:
            izquierda = x + 1
        else:
            derecha = x - 1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
objetivo = 2
numero = busquedabi_iterativa(lista, objetivo)  
print("Busqueda iterativa: ", numero)
print(" ")

def busquedabi_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    x = (izquierda + derecha) 
    if lista[x] == objetivo:
        return x
    elif lista[x] < objetivo:
        return busquedabi_recursiva(lista, objetivo, x + 1, derecha)
    else:
        return busquedabi_recursiva(lista, objetivo, izquierda, x - 1)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
objetivo = 6
resultado = busquedabi_recursiva(lista, objetivo, 0, len(lista) - 1)  
print("Busqueda recursiva: ", resultado)
