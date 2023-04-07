def get_line(x0, y0, x1, y1):
    points = [] # lista para almacenar puntos generados
    # 1er paso: dx, dy
    dx = x1 - x0
    dy = y1 - y0
    # variables para iterar xk, yk
    xk = x0
    yk = y0
    y_inc = 1

    if dy < 0:
        dy = -1 * dy
        y_inc = -1

    # 2do paso: parametro de decision Pk
    Pk = 2 * dy - dx

    # 3er paso: iterar hasta el punto final:
    while xk <= x1:
        # agregar punto a la lista
        points.append((xk, yk))
        xk += 1
        # decido en base a Pk si y incrementa o no
        if Pk < 0:
            Pk += 2 * dy
        else:
            Pk += 2 * dy - 2 * dx
            yk += y_inc
    
    return points

if __name__ == "__main__":
    print(get_line(0, 3, 6, 5))
    #print(get_line(6, 5, 0, 3)) #no quiere hacia atras
    print(get_line(1, 5, 5, 2))
    #print(get_line(0, 3, -6, -3)) #no quiere hacia atras
    print(get_line(1, 2, 3, 6)) #no quiere subir mas
