class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas


    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas


    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            print(self.nombre, int(salario_mensual))
        else:
            print(self.nombre)


nombre = input("Ingrese el nombre del empleado: ")
salario_por_hora = int(input("Ingrese el salario básico por hora: "))
horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))


empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
empleado.mostrar_informacion()

