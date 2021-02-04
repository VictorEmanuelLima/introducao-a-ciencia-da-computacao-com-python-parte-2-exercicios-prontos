class Triangulo:
    def __init__ (t, a, b, c):
        t.a = a
        t.b = b
        t.c = c
    def perimetro(t):
        return t.a + t.b + t.c
    def  tipo_lado(t):
        lados = [t.a, t.b, t.c]
        quan_i = 1
        for i in range(len(lados)):
            for j in range(i + 1 , len(lados)):
                if lados[i] == lados[j]:
                    quan_i += 1

        if quan_i > 2:
            return 'equilátero'
        if quan_i == 2:
            return 'isósceles'
        if quan_i == 1:
            return 'escaleno'
