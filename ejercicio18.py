import math


class Empleado:
    def __init__(self, codigo, nombres, horas_mes, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_mes = horas_mes
        self.valor_hora = valor_hora
        self.retencion = retencion
        self.salario_bruto = 0
        self.salario_neto = 0
       
    def salarios(self):
        self.salario_bruto = (self.horas_mes* self.valor_hora)
        self.salario_neto = int((self.horas_mes * self.valor_hora) - (self.horas_mes * self.valor_hora) * (self.retencion/100))
   
   
    def mostrar_resultados(self):
        self.salarios()
        print("informacion basica del empleado ante la DIAN es: ")
        print(f"codigo: {self.codigo}, nombres: {self.nombres}, salario bruto: {self.salario_bruto}, salario neto: {self.salario_neto}")
       


codigo = input("ingrese codigo del empleado: ")
nombres = input("ingrese nombres del empleado: ")
horas_mes = int(input("ingrese horas trabajadas por mes: "))
valor_hora = int(input("ingrese cual es la ganancia por hora: "))
retencion = float(input("ingrese el porcentaje de retencion en la fuente: "))


empleado = Empleado(codigo, nombres, horas_mes, valor_hora, retencion)
empleado.mostrar_resultados()
