def sumUpList(lista, k):
    seen = set()
    for num in lista:
        if k - num in seen:
            return True
        seen.add(num)
    return False
    

if __name__ == '__main__':
    lista = [1, 2, 3, 4]
    lista2 = []
    lista3 = [1, 2, 3, 4, 5]
    lista4 = [1, 2, -9, 3, 4, 18]

    k=9

    print(sumUpList(lista, k))
    print(sumUpList(lista2, k))
    print(sumUpList(lista3, k))
    print(sumUpList(lista4, k))