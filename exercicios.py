l = []

def preenche_lista(lista: list) -> None:
    i = 0
    a = 10
    while i < 10:
        lista.append(a)
        i = i + 1
        a = a + 1
    print(lista)
preenche_lista(l)

def exibe_lista(lista: list) -> None:
    i = 0
    for i in range(len(lista)):
        print(lista[i])
exibe_lista(l)

def conta_elementos(lista: list) -> int:
    return len(lista)

print("Tamanho:", conta_elementos(l))


"""  --- TERMINAR EM CASA ---

def retorna_indice(elemento: int) -> None:
    x = elemento
    indice = int(l.index(x))
    print(indice)

retorna_indice(10)

"""

