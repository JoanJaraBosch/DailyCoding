from functools import reduce

def multList(lista):
    if len(lista) <= 0:
        return lista
    else:
        numZeros = lista.count(0)
        newLista = []
        if numZeros >= 1 :
            if numZeros > 1:
                for i in lista:
                    newLista.append(0)
            else:
                resultado = reduce(lambda x, y: x * y, filter(lambda x: x != 0, lista), 1)
                for i in lista:
                    if i == 0:
                        newLista.append(resultado)
                    else:
                        newLista.append(0)
        else:
            resultado = reduce(lambda x, y: x * y, lista)
            for i in lista:
                newLista.append(resultado//i)
        return newLista
    

if __name__ == '__main__':
    lista = [1, 0, 3, 4]
    lista2 = []
    lista3 = [1, 0, 3, 4, 0]
    lista4 = [1, 2, -9, 3, 4, 18]

    k=9

    print(multList(lista))
    print(multList(lista2))
    print(multList(lista3))
    print(multList(lista4))