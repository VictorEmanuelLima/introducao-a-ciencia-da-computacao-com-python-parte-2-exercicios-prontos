def ordenada(lista):    
    fim = len(lista)
    orde = True
    for i in range(fim - 1):
        for j in range(i+1, fim):            
            if lista[i] > lista[j]:
                orde = False
    return orde    
