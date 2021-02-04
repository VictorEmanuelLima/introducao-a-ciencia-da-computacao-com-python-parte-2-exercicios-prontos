def menor_nome(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].strip()
    menor = lista[0]
    for j in range(len(lista)):
        if len(menor) > len(lista[j]):
            menor = lista[j]
    menor = menor.capitalize()
    return menor
        
