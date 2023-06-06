l = []

def preenche_lista(lista: list) -> None:
    i = 0
    a = 10
    while i < 10:
        lista.append(a)
        i = i + 1
        a = a + 1
    print(f"O seu vetor é: {lista}")
preenche_lista(l)

def exibe_lista(lista: list) -> None:
    i = 0
    for i in range(len(lista)):
        print(lista[i])
exibe_lista(l)

def conta_elementos(lista: list) -> int:
    return len(lista)

print("Tamanho:", conta_elementos(l))

def busca(lista: list, elemento: int) -> int:
    qtd = lista.count(elemento)
    print(f"O número: {elemento} aparece um total de {qtd} vez")
busca(l, 15)

def retorna_indice(lista: list, elemento: int) -> str:
    x = elemento
    if x in lista:
        indice = int(lista.index(x))
        return (indice)
    else:
        return print("-1")



print("O número escolhido está no índice: " , retorna_indice(l, 19))


def conta_inteiro(lista: list) -> int:
    inte = lista.count(12)
    print(inte)
conta_inteiro(l)