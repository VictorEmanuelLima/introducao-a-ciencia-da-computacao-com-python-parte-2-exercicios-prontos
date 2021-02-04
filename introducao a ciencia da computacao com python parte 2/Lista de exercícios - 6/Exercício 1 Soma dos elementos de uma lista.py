def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        meio = len(lista) // 2

        lado_esquerdo = soma_lista((lista[:meio]))
        lado_direito = soma_lista((lista[meio:]))

    return (lado_direito + lado_esquerdo)
    
