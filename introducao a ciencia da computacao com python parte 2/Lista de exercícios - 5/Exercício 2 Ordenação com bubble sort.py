def bubble_sort(lista):
    fim = len(lista)
    trocou = False
    for i in range(fim-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if not trocou:
            return
    return lista
