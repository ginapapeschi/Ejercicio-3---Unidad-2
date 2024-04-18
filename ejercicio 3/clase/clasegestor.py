class GestorVenta:
    __venta = [5]
    __cantfarm = int
    __cantdias = 7

    def __init__(self):
        cantfarm = 5
        for i in range (cantfarm):
           self.__venta.append([0] * self.__cantdias)

    def acumular (self, num_dia, num_suc, importe):
        self.__venta[num_suc-1][num_dia-1] += importe

    def total_fact_suc (self, num_suc):
        importe = 0
        num_suc = input ("Ingrese una sucursal: ")
        for i in range (self.__cantdias):
            importe += self.__venta[num_suc-1][i]
        return importe
    
    def mayor_fact (self, num_dia):
        max = 0
        for i in range (self.__cantfarm):
            if (self.__venta[i][num_dia-1]) > max:
                max = i+1
        return max

    def menor_fact (self):
        min = 99999999999
        for i in range (self.__cantfarm):
            acum = 0
            for j in range (self.__cantdias):
                acum += self.__venta[i][j]
            if (acum < min):
                min = i+1
        return min
    
    def total_fact (self):
        acum = 0
        for i in range (self.__cantfarm):
            for j in range (self.__cantdias):
                acum += self.__venta[i][j]
        return acum





