class Empresa:
    @staticmethod
    def salarios(ventas, salarios):
        total_ventas = sum(ventas)
        porcentaje_ventas = 0.33 * total_ventas
        if ventas[0] > porcentaje_ventas or ventas[1] > porcentaje_ventas or ventas[2] > porcentaje_ventas:
            salario_1 = int(salarios + 0.2 * salarios)
        else:
            salario_1 = salarios
        if ventas[1] > porcentaje_ventas:
            salario_2 = int(salarios + 0.2 * salarios)
        else:
            salario_2 = salarios
        if ventas[2] > porcentaje_ventas:
            salario_3 = int(salarios + 0.2 * salarios)
        else:
            salario_3 = salarios
           
        print(f"salarios vendedores depto. 1 {salario_1}, salarios vendedores depto. 2 {salario_2}, salarios vendedores depto. 3 {salario_3}")


ventas_depart = input("ingrese ventas de cada departamento separado por un espacio: ").split(" ")
ventas_depart_formateadas = list(map(int, ventas_depart))


print(ventas_depart_formateadas)
ventas_ejemplo = Empresa()
ventas_ejemplo.salarios(ventas_depart_formateadas[:-1], ventas_depart_formateadas[-1])
