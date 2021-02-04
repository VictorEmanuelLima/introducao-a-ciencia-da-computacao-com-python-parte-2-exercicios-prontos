def incomodam(n):
    if n < 1:
        return ''
    else:
        return 'incomodam ' + incomodam(n - 1)
def elefantes(n, inicio = 1, n2 = 1 ):
    inici = inicio
    if n < 1:
        return ""
    elif n == 1:
        return ("Um elefante incomoda muita gente")
    else:
        if inici == 1:
            inici += 1
            n2 = n
            return "Um elefante incomoda muita gente" + "\n" + elefantes(inici, inici, n2)
        if inici < n2:
            inici += 1
            return (str(n) +" elefantes "+incomodam(n) + "muito mais" + "\n" + str(n) +" elefantes incomodam muita gente" + "\n" + elefantes(inici, inici, n2))
        else:
            return (str(n) +" elefantes "+incomodam(n) + "muito mais")
