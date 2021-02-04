def encontra_impares(lista):
    lista1 = []
    if len(lista) == 1 and lista[0] % 2 != 0:
        return lista
    elif len(lista) == 1 and lista[0] % 2 == 0:
        pass
    else:
        meio = len(lista) // 2
        lista1.extend(encontra_impares((lista[:meio])))
        lista1.extend(encontra_impares((lista[meio:])))

    return lista1
