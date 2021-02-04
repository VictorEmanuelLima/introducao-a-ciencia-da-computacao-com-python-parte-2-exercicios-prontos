def soma_matrizes(m1, m2):
    x = []
    y = []
    if len(m1) == len(m2) and len(m2) == len(m1) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1[0])):
            if len(m1) == 2:
                x.append(m1[0][i] + m2[0][i])
                y.append(m1[1][i] + m2[1][i])
            else:
                x.append(m1[0][i] + m2[0][i])
        if len(y) !=  0:
            u = [x, y]
        else:
            u = [x]
        return u
    else:
        return False
        
        
        
