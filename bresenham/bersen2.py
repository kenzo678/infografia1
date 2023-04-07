def get_line(x0, y0, x1, y1):
    points = [] # lista para almacenar puntos generados



    #para ir atras (1)
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    # 1er paso: dx, dy
    dx = x1 - x0
    dy = y1 - y0

    # variables para iterar xk, yk
    xk = x0
    yk = y0
    y_inc = 1
    x_inc = 1

    if dy < 0:
        dy = -1 * dy
        y_inc = -1

    if dx < 0:
        dx = -1 * dx
        x_inc = -1 

    m = dy/dx

    # 2do paso: parametro de decision Pk
    Pk = 2 * dy - dx

    # 3er paso: iterar hasta el punto final:

    # -1<=m<=1
    if(-1<=m<=1):
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

    # 1 < m  OR  m > -1
    if(1<m or m>-1):
     while yk <= y1:
         # agregar punto a la lista
         points.append((xk, yk))
         yk += 1
         # decido en base a Pk si y incrementa o no
         if Pk < 0:
             Pk += 2 * dx
         else:
             Pk += 2 * dx - 2 * dy
             xk += x_inc
     return points


if __name__ == "__main__":
    print(get_line(0, 3, 6, 5))

    print(get_line(0, 3, 4, 8)) #big slope ??

    #prioridad 1, ir hacia atras. -- V
    #prioridad 2, arriba de 45deg.
    #prioridad 3, abajo de -45deg.
