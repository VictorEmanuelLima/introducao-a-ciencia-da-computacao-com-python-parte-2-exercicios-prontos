def maiusculas(frase):
    i = 0
    letras_m = ""
    while i < len(frase):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 91:
            letras_m = letras_m + frase[i]
        i += 1
    return letras_m
        
        
    
