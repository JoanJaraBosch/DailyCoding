def first_positive_integer_missing(lista):
    if len(lista) == 0:
        print("First positive integer missing is: ",1)
    else:
        num = 0
        for a in lista:
            if num + (-1*a) != -1:
                print("First positive integer missing is: ",num+1)
                break
            num = a

if __name__ =='__main__':
    lista = [-3, -5, -6, -7]
    lista2 = [1, 2, 34]
    lista3 = [-4, 0, 4, 2, -3, 1]

    first_positive_integer_missing(sorted(filter(lambda x: x > 0, lista)))
    first_positive_integer_missing(sorted(filter(lambda x: x > 0, lista2)))
    first_positive_integer_missing(sorted(filter(lambda x: x > 0, lista3)))